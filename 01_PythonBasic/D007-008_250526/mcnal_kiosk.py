from datetime import datetime, time

# 진행 레벨 상수
START = 0
EAT_PLACE = 1
CATEGORY = 2
SIDE_MENU = 3
BEVERAGE_MENU = 4
BURGUR_MENU = 5
BURGUR_CATEGORY = 6
SINGLE_OR_SET = 7
SET_SIZE = 8
SET_SIDE_MENU = 9
SET_BEVERATE_MENU = 10
SELECTED = 11
BASKET = 12
PAYMENT = 13

# 버거 데이터 { ID:[이름, 세트 가격, 단품 가격, 구분(기본: 0, 맥런치 가능: 1, 맥모닝: 2), 소분류(비프: b, 치킨: c, 불고기:bg, 씨푸드:s)] }
menu_burgers = {
    101:["빅맥", 6500, 5000, 1, "b"],
    102:["맥스파이시 상하이 버거", 6500, 5000, 1, "c"],
    103:["1955 버거", 6800, 5300, 1, "b"],
    104:["더블 불고기 버거", 6300, 4800, 1, "bg"],
    105:["베이컨 토마토 디럭스 버거", 6800, 5300, 1, "b"],
    106:["쿼터파운더 치즈 버거", 7000, 5500, 0, "b"],
    107:["슈슈버거", 6000, 4500, 0, "s"],
    108:["치즈버거", 5000, 3500, 0, "b"],
    109:["햄버거", 4500, 3000, 0, "b"],
    100:["베이컨 토마토 맥머핀", 4500, 3000, 2, ""],
    111:["베이컨 에그 맥머핀", 4300, 2800, 2, ""],
    112:["소시지 에그 맥머핀", 4000, 2500, 2, ""],
    113:["에그 맥머핀", 3800, 2300, 2, ""],
}

# 사이드 데이터 { ID:[이름, 가격] }
menu_sides = {
    201:["맥윙", 2400],
    202:["감자튀김", 2000],
    203:["맥너겟", 2000],
    204:["코울슬로", 2300],
    205:["치즈스틱", 2600],
}

# 음료 데이터 { ID:[이름, 가격] }
menu_beverage = {
    301:["아이스 아메리카노", 2000],
    302:["아메리카노", 2000],
    303:["아이스 카페라떼", 3000],
    304:["카페라떼", 3000],
    305:["콜라", 2000],
    306:["제로콜라", 2000],
    307:["스프라이트", 2000],
    308:["환타", 2000],
    309:["쉐이크", 2500],
}

# 문구 출력, 사용자 입력 받기, 입력 값 유효성 체크(\t로 구분)
def kiosk_print(print_str:str, sep_line=True) -> str:
    valid_input_lst = []
    if sep_line:
        print("=" * 30)
    print(print_str)
    for i, s in enumerate(print_str):           # \t 뒤에 있는 문자를 유효 입력값으로 추가
        if s == '\t':
            valid_input_lst.append(print_str[i+1])

    while True:
        user_in = input("입력> ")
        if user_in in valid_input_lst:
            print("="*30)
            return user_in
        else:
            print("\n잘못 입력하셨습니다.")

def selected_menu_print(menu_datas):
    print("=" * 30)
    print("선택하신 메뉴 \n\n", "  이름               가격")
    for menu in menu_datas:
        print(f"  - {menu[0]}               {menu[1]}")

def main():
    progress = START        # 진행 레벨(0:시작/1:식사장소/2:카테고리/3:사이드/4:음료/5:버거/6:소분류/7:단,세트/8:s_사이즈/9:s_사이드/10:s_음료/11:선택내용/12:장바구니/13:결제)
    eat_place = ""          # 0:매장/1:포장
    now_timezone = ""       # 0:일반/1:맥모닝/2:맥런치
    user_in = ""            # 사용자 입력
    items_cart = {}         # { 사이드_ID:수량, 버거_ID:[수량, 사이드_ID, 음료_ID, 사이즈, 맥런치여부], ... }
    now_item = [0, 0, 0, 0, False, False]         # 현재 선택된 아이템. [ ID, 수량, ... ]

    while True:
        # 시작
        if progress == START:
            if kiosk_print("맥도날드에 오신 것을 환영합니다\n\t1. 주문하기") == "1":
                progress = EAT_PLACE

        elif progress == EAT_PLACE:
            user_in = kiosk_print("식사장소를 선택해주세요\n\t0. 이전\n\t1.매장\n\t2.포장")
            if user_in == "0":      # 이전으로
                progress = START
            else:
                eat_place = user_in  # 매장/포장
                progress = CATEGORY

        elif progress == CATEGORY:
            # 맥모닝 시간대일 때
            if time(hour=4, minute=0) <= datetime.now().time() < time(hour=10, minute=30):
                now_timezone = 1
                user_in = kiosk_print("카테고리를 선택해주세요\n\t0. 이전\n\t1. 맥모닝\n\t2. 사이드\n\t3. 음료")

            # 맥런치 시간대일 때
            elif time(hour=10, minute=30) <= datetime.now().time() < time(hour=14, minute=0):
                now_timezone = 2
                user_in = kiosk_print("카테고리를 선택해주세요\n\t0. 이전\n\t1. 맥런치\n\t2. 사이드\n\t3. 음료")

            # 그 외 시간대일 때
            else:
                now_timezone = 0
                user_in = kiosk_print("카테고리를 선택해주세요\n\t0. 이전\n\t1. 버거\n\t2. 사이드\n\t3. 음료")

            if user_in == "0":
                progress = EAT_PLACE
            elif user_in == "1":
                progress = BURGUR_MENU
            elif user_in == "2":
                progress = SIDE_MENU
            elif user_in == "3":
                progress = BEVERAGE_MENU

        # 사이드 메뉴 선택
        elif progress == SIDE_MENU:
            s = "사이드 메뉴를 선택해주세요\n\t0. 이전"
            for k, v in menu_sides.items():
                s += f"\n\t{k - 200}. {v[0]}"
            user_in = kiosk_print(s)
            item_id = int(user_in) + 200

            # 이전으로
            if user_in == "0":
                progress = CATEGORY
            # 메뉴 선택했을 때
            else:
                selected_menu_print([menu_sides[item_id]])
                user_in = kiosk_print("\n\t0. 이전\n\t1. 장바구니에 담기", sep_line=False)
                if user_in == "1":
                    now_item[0] = item_id

                    progress = BASKET

        # 음료 메뉴 선택
        elif progress == BEVERAGE_MENU:
            id_unit = 300
            s = "사이드 메뉴를 선택해주세요\n\t0. 이전"
            for k, v in menu_beverage.items():
                s += f"\n\t{k - id_unit}. {v[0]}"
            user_in = kiosk_print(s)
            item_id = int(user_in) + id_unit

            # 이전으로
            if user_in == "0":
                progress = CATEGORY
            # 메뉴 선택했을 때
            else:
                selected_menu_print([menu_beverage[item_id]])
                user_in = kiosk_print("\n\t0. 이전\n\t1. 장바구니에 담기", sep_line=False)
                if user_in == "1":
                    now_items[item_id] = 1
                    progress = BASKET

        elif progress == BURGUR_MENU:
            pass
        elif progress == CATEGORY:
            pass
        elif progress == SINGLE_OR_SET:
            pass
        elif progress == SET_SIZE:
            pass
        elif progress == SELECTED:
            pass

        elif progress == BASKET:
            # now_items 에 있는 항목을 장바구니에 넣는다.
            item = now_items.popitem()

            # 값의 타입이 list이면 버거이므로 제외
            # item[0]은 key, item[1]은 수량
            if type(item[1]) != list and (item[0] in items_cart.keys()):
                items_cart[now_items.popitem()[0]] += 1     # 수량 증가
            else:
                # 버거, 추가되지 않은 항목을 새로 추가할 것.
                items_cart[item[0]] = item[1]

            # 현재 장바구니 출력
            print("장바구니 \n\n", "  이름               가격               수량")
            for i, v in enumerate(items_cart):
                print(f"  {i + 1}) {v}               {v[0][1]}               {v[0][1]}")

            user_in = kiosk_print("\n\t0. 카테고리\n\t1. 수량 수정\n\t2. 결제", sep_line=False)

            # 카테고리로 이동
            if user_in == "0":
                progress = CATEGORY

            # 수량 수정
            elif user_in == "1":
                tmp_id_lst = list(items_cart.keys())

                while True:
                    idx = input("수량을 수정할 품목의 번호를 입력해주세요> ")

                    # if idx.isdigit() and (0 < int(idx) <= ):
                    #     break
                    # print("잘못 입력하셨습니다.")

                while True:
                    num = input("수량을 입력해주세요> ")
                    if num.isdigit() and int(num) >= 0:
                        break
                    print("잘못 입력하셨습니다.")

                if num == "0":
                    # 삭제
                    #del basket[]
                    pass

                else:
                    # 수량 수정
                    pass

            # 결제
            elif user_in == "2":
                progress = PAYMENT

        elif progress == PAYMENT:
            pass

main()

















