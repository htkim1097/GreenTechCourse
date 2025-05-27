from datetime import datetime, time

# 진행 단계
START = 1000
EAT_PLACE = 1001
CATEGORY = 1002
SIDE_MENU = 1003
BEVERAGE_MENU = 1004
BURGER_MENU = 1005
SINGLE_OR_SET = 1006
SET_SIZE = 1007
SET_SIDE_MENU = 1008
SET_BEVERATE_MENU = 1009
SELECTED = 1010
CART = 1011
PAYMENT = 1012

# 대분류
TYPE_BURGER = 1
TYPE_SIDE = 2
TYPE_BEVERAGE = 3

# 시간대
TIME_NORMAL = 0
TIME_LAUNCH = 1
TIME_MORNING = 2

# 메뉴 데이터 { ID:[이름, 세트 가격, 단품 가격, 구분(기본: 0, 맥런치 가능: 1, 맥모닝: 2), 소분류(비프: b, 치킨: c, 불고기:bg, 씨푸드:s)] }
menu = {
    # 버거 메뉴
    101:["빅맥", 6500, 5000, 1, "a"],
    102:["맥스파이시 상하이 버거", 6500, 5000, 1, "b"],
    103:["1955 버거", 6800, 5300, 1, "a"],
    104:["더블 불고기 버거", 6300, 4800, 1, "c"],
    105:["베이컨 토마토 디럭스 버거", 6800, 5300, 1, "a"],
    106:["쿼터파운더 치즈 버거", 7000, 5500, 0, "a"],
    107:["슈슈버거", 6000, 4500, 0, "d"],
    108:["치즈버거", 5000, 3500, 0, "a"],
    109:["햄버거", 4500, 3000, 0, "a"],
    # 맥모닝 메뉴
    110:["베이컨 토마토 맥머핀", 4500, 3000, 2, ""],
    111:["베이컨 에그 맥머핀", 4300, 2800, 2, ""],
    112:["소시지 에그 맥머핀", 4000, 2500, 2, ""],
    113:["에그 맥머핀", 3800, 2300, 2, ""],

    # 사이드 메뉴
    201:["맥윙", 2400],
    202:["감자튀김", 2000],
    203:["맥너겟", 2000],
    204:["코울슬로", 2300],
    205:["치즈스틱", 2600],

    # 음료 메뉴
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

def menu_print(category:int, timezone=0, burger_category="") -> str:
    s = "메뉴를 선택해주세요\n소분류: \ta. 비프\tb. 치킨\tc. 불고기\td. 씨푸드\n\n\t0. 이전"

    # 대분류(버거/사이드/음료)에 맞는 메뉴만 리스트에 담기
    lst = list(menu.keys())

    if category == TYPE_BURGER:
        if timezone == TIME_MORNING:       # 맥모닝
            lst = [i for i in list(menu.keys()) if str(i)[0] == str(category) and menu[i][3] == 2]
        else:     # 일반, 맥런치 시간대
            if burger_category != "":
                lst = [i for i in list(menu.keys()) if str(i)[0] == str(category) and menu[i][3] != 2 and menu[i][4] == burger_category]
            else:
                lst = [i for i in list(menu.keys()) if str(i)[0] == str(category) and menu[i][3] != 2]

        for i in lst:
            dis = 0
            if timezone == TIME_LAUNCH:     # 맥런치 시간에는 500원 할인
                dis = 500
            s += f"\n\t{i - (category * 100)}. {menu[i][0]}  세트 {menu[i][1] - dis}/ 단품 {menu[i][2] - dis}"
    else:
        for i in [i for i in list(menu.keys()) if str(i)[0] == str(category)]:
            s += f"\n\t{i - (category * 100)}. {menu[i][0]}  {menu[i][1]}"

    return kiosk_print(s)

def main():
    progress = START                    # 진행 레벨(0:시작/1:식사장소/2:카테고리/3:사이드/4:음료/5:버거/6:소분류/7:단,세트/8:s_사이즈/9:s_사이드/10:s_음료/11:선택내용/12:장바구니/13:결제)
    eat_place = ""                      # 0:매장/1:포장
    now_timezone = TIME_NORMAL          # 0:일반/1:맥런치/2:맥모닝
    user_in = ""                        # 사용자 입력
    items_cart = {}                     # { 1:{item1}, 2:{item2} }
    selected_item = {}                  # 현재 선택된 아이템. { ID, 수량, 사이드_ID, 음료_ID, 세트여부, 사이즈여부, 맥런치여부 }
    prev_progress = 0

    while True:
        # 시작
        if progress == START:
            if kiosk_print("맥도날드에 오신 것을 환영합니다\n\t1. 주문하기") == "1":
                progress = EAT_PLACE

        # 식사장소 선택
        elif progress == EAT_PLACE:
            user_in = kiosk_print("식사장소를 선택해주세요\n\t0. 이전\n\t1. 매장\n\t2. 포장")
            if user_in == "0":      # 이전으로
                progress = START
            else:
                eat_place = user_in  # 매장/포장
                progress = CATEGORY

        # 대분류(버거, 사이드, 음료) 선택
        elif progress == CATEGORY:
            # 선택 아이템 초기화
            selected_item = {"id": 0, "quantity": 1, "side_id": 0, "beverage_id": 0, "is_set": False, "large_size": False, "is_launch": False, "price": 0}
            # 맥모닝 시간대일 때
            if time(hour=4, minute=0) <= datetime.now().time() < time(hour=10, minute=30):
                now_timezone = TIME_MORNING
                user_in = kiosk_print("카테고리를 선택해주세요\n\t0. 이전\n\t1. 맥모닝\n\t2. 사이드\n\t3. 음료\n\t4. 장바구니")

            # 맥런치 시간대일 때
            elif time(hour=10, minute=30) <= datetime.now().time() < time(hour=14, minute=0):
                now_timezone = TIME_LAUNCH
                user_in = kiosk_print("카테고리를 선택해주세요\n\t0. 이전\n\t1. 맥런치\n\t2. 사이드\n\t3. 음료\n\t4. 장바구니")

            # 그 외 시간대일 때
            else:
                now_timezone = TIME_NORMAL
                user_in = kiosk_print("카테고리를 선택해주세요\n\t0. 이전\n\t1. 버거\n\t2. 사이드\n\t3. 음료\n\t4. 장바구니")

            if user_in == "0":
                progress = EAT_PLACE
            else:
                prev_progress = CATEGORY
                if user_in == "1":
                    progress = BURGER_MENU
                elif user_in == "2":
                    progress = SIDE_MENU
                elif user_in == "3":
                    progress = BEVERAGE_MENU
                elif user_in == "4":
                    progress = CART

        # 버거 메뉴 선택
        elif progress == BURGER_MENU:
            burger_category = ""

            while True:
                user_in = menu_print(TYPE_BURGER, now_timezone, burger_category)

                if user_in == "0":
                    if burger_category == "":   # 이전으로
                        progress = CATEGORY
                        break
                    else:                       # 버거 전체 카테고리로
                        burger_category = ""
                elif user_in in ["a", "b", "c", "d"]:  # 버거 소분류 카테고리
                    burger_category = user_in
                else:                           # 메뉴 선택
                    selected_item["id"] = int(user_in) + (TYPE_BURGER * 100)  # ID
                    progress = SINGLE_OR_SET
                    break

        # 세트 또는 단품 선택
        elif progress == SINGLE_OR_SET:
            user_in = kiosk_print("세트 여부를 선택해주세요\n\t0. 이전\n\t1. 세트\n\t2. 단품")
            if user_in == "0":              # 이전으로
                progress = BURGER_MENU
            elif user_in == "1":            # 세트
                selected_item["is_set"] = True
                progress = SET_SIZE
            elif user_in == "2":            # 단품
                selected_item["is_set"] = False
                prev_progress = SINGLE_OR_SET
                progress = SELECTED

        # 세트 사이즈 선택
        elif progress == SET_SIZE:
            user_in = kiosk_print("사이즈를 선택해주세요\n\t0. 이전\n\t1. 일반\n\t2. 라지")
            if user_in == "0":              # 이전으로
                progress = SINGLE_OR_SET
            else:
                prev_progress = SET_SIZE
                if user_in == "1":            # 일반
                    selected_item["large_size"] = False
                    progress = SIDE_MENU
                elif user_in == "2":            # 라지
                    selected_item["large_size"] = True
                    progress = SIDE_MENU

        # 사이드 메뉴 선택
        elif progress == SIDE_MENU:
            user_in = menu_print(TYPE_SIDE)

            # 이전으로
            if user_in == "0":
                progress = prev_progress
            # 메뉴 선택했을 때
            else:
                prev_progress = SIDE_MENU
                if selected_item["is_set"]:
                    selected_item["side_id"] = int(user_in) + (TYPE_SIDE * 100)
                    progress = BEVERAGE_MENU
                else:
                    selected_item["id"] = int(user_in) + (TYPE_SIDE * 100)
                    progress = SELECTED

        # 음료 메뉴 선택
        elif progress == BEVERAGE_MENU:
            user_in = menu_print(TYPE_BEVERAGE)

            # 이전으로
            if user_in == "0":
                progress = prev_progress
            # 메뉴 선택했을 때
            else:
                if selected_item["is_set"]:
                    selected_item["beverage_id"] = int(user_in) + (TYPE_BEVERAGE * 100)
                else:
                    selected_item["id"] = int(user_in) + (TYPE_BEVERAGE * 100)
                progress = SELECTED
                prev_progress = BEVERAGE_MENU

        # 선택된 메뉴를 확인
        elif progress == SELECTED:
            print("선택하신 메뉴 \n\n", "  이름", " "*10, "가격")

            item_id = selected_item["id"]
            if str(item_id)[0] == TYPE_BURGER:
                # !!! 세트메뉴 구성, 맥런치에 따른 가격 계산 구현하기 !!!
                print(f"  - {menu.get(item_id)[0]}", " "*10, f"{menu.get(item_id)[1 if selected_item["is_set"] else 2]}")
            else:
                print(f"  - {menu.get(item_id)[0]}", " "*10, f"{menu.get(item_id)[1]}")

            user_in = kiosk_print("\n\t0. 이전\n\t1. 장바구니에 담기", sep_line=False)

            if user_in == "0":
                progress = prev_progress
            elif user_in == "1":
                progress = CART

        # 장바구니
        elif progress == CART:
            # 중복체크
            # id, side_id, be_id 모두 같으면 수량만 올리기
            # 없으면 새로 추가

            # 선택한 아이템을 장바구니에 넣는다.
            n_id = min([i for i in range(1, 99) if i not in [items_cart.keys()]])

            if n_id is not None:
                items_cart[n_id] = selected_item
            else:
                print("ID 오류")

            # 현재 장바구니 출력
            print("장바구니 \n\n", "  이름", " "*10, "가격", " "*10, "수량")

            # 가격 구하기 1) 메뉴를 고를 때마다 계산, 2) 마지막에 한 번에 계산

            for k, v in items_cart.items():
                print(f"  {k}. {menu.get(v["id"])[0]}               {v["price"]}               {v["quantity"]}")

            user_in = kiosk_print("\n\t0. 카테고리\n\t1. 수량 수정\n\t2. 결제", sep_line=False)

            # 카테고리로 이동
            if user_in == "0":
                progress = CATEGORY

            # 수량 설정
            elif user_in == "1":
                idx = 0
                while True:
                    idx = input("수량을 수정할 품목의 번호를 입력해주세요> ")
                    if idx.isdigit() and (0 < int(idx) <= len(items_cart)):
                        break
                    print("잘못 입력하셨습니다.")

                while True:
                    num = input("수량을 입력해주세요> ")
                    if num.isdigit() and int(num) >= 0:
                        break
                    print("잘못 입력하셨습니다.")

                if num == "0":  # 삭제
                    del items_cart[idx] if idx != 0 else print("삭제 오류")
                    pass

                else:       # 수량 수정
                    pass

            # 결제
            elif user_in == "2":
                if len(items_cart) == 0:
                    print("장바구니가 비었습니다. 구매할 음식을 추가해주세요.\n")
                else:
                    progress = PAYMENT

        elif progress == PAYMENT:
            pass

# Start~
main()


# TODO
# 결제
# 수량 설정
# 가격 구하기
# 장바구니에 추가된 아이템 중복체크
# 리팩토링

















