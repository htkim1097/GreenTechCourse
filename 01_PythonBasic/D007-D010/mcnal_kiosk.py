import random
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

# 메뉴 데이터 { ID:[이름, 세트 가격, 단품 가격, 구분(기본: 0, 맥런치 가능: 1, 맥모닝: 2), 소분류(비프: a, 치킨: b, 불고기:c, 씨푸드:d)] }
# => ID:{"name":"빅맥", ... } 이런식으로 했다면 가독성이 더 좋았을 것
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
# => input_validation() 이 이름이 더 적절함
def kiosk_print(print_str:str, sep_line=True) -> str:
    valid_input_lst = []
    if sep_line:
        print("="*30)
    print(print_str)
    for i, s in enumerate(print_str):           # \t 뒤에 있는 문자를 유효 입력값으로 추가
        if s == '\t':
            valid_input_lst.append(print_str[i+1])

    while True:
        user_in = input("입력> ")
        if user_in in valid_input_lst:
            #print("="*30)
            return user_in
        else:
            print("\n잘못 입력하셨습니다.")

def menu_print(category:int, timezone=0, burger_category="") -> str:
    burger_category_str = ""
    string = ""

    # 대분류(버거/사이드/음료)에 맞는 메뉴만 리스트에 담기
    if category == TYPE_BURGER:     # 버거 메뉴
        if timezone == TIME_MORNING:       # 맥모닝
            lst = [i for i in list(menu.keys()) if str(i)[0] == str(category) and menu[i][3] == 2]
        else:     # 일반, 맥런치 시간대
            burger_category_str = "\n소분류: \ta. 비프\tb. 치킨\tc. 불고기\td. 씨푸드"
            if burger_category != "":
                lst = [i for i in list(menu.keys()) if str(i)[0] == str(category) and menu[i][3] != 2 and menu[i][4] == burger_category]
            else:
                lst = [i for i in list(menu.keys()) if str(i)[0] == str(category) and menu[i][3] != 2]

        for i in lst:
            dis = 0
            if timezone == TIME_LAUNCH:     # 맥런치 시간에는 500원 할인
                dis = 500
            string += f"\n\t{i - (category * 100)}. {menu[i][0]}  세트 {menu[i][1] - dis}/ 단품 {menu[i][2] - dis}"

    else:       # 사이드, 음료 메뉴
        for i in [i for i in list(menu.keys()) if str(i)[0] == str(category)]:
            string += f"\n\t{i - (category * 100)}. {menu[i][0]}  {menu[i][1]}"

    return kiosk_print("메뉴를 선택해주세요" + burger_category_str + "\n\n\t0. 이전" + string)

def order_print(cart:dict, front_str:str):
    print("=" * 30)
    print(front_str + "\n  이름" + " " * 10 + "수량" + " " * 10 + "가격")
    total_price = 0

    for k, v in cart.items():
        print(f"  {k}. {menu.get(v["id"])[0]}           {v["quantity"]}           {int(v["price"]) * int(v["quantity"])}")
        total_price += int(v["price"]) * int(v["quantity"])

    print(f"\n합계: {total_price}")

def main():
    progress = START                    # 진행 레벨(0:시작/1:식사장소/2:카테고리/3:사이드/4:음료/5:버거/6:소분류/7:단,세트/8:s_사이즈/9:s_사이드/10:s_음료/11:선택내용/12:장바구니/13:결제)
    now_timezone = TIME_NORMAL          # 0:일반/1:맥런치/2:맥모닝
    user_in = ""                        # 사용자 입력
    items_cart = {}                     # { 1:{item1}, 2:{item2} }
    selected_item = {}                  # 현재 선택된 아이템. { ID, 수량, 사이드_ID, 음료_ID, 세트여부, 사이즈여부, 맥런치여부 }
    prev_progress = 0

    while True:
        # 시작
        if progress == START:
            # 초기화
            items_cart = {}

            if kiosk_print("맥도날드에 오신 것을 환영합니다\n\t1. 주문하기") == "1":
                progress = EAT_PLACE

        # 식사장소 선택
        elif progress == EAT_PLACE:
            user_in = kiosk_print("식사장소를 선택해주세요\n\t0. 이전\n\t1. 매장\n\t2. 포장")
            if user_in == "0":      # 이전으로
                progress = START
            else:
                progress = CATEGORY

        # 대분류(버거, 사이드, 음료) 선택
        elif progress == CATEGORY:
            # 선택 아이템 초기화
            selected_item = {"id": 0, "quantity": 1, "side_id": 0, "beverage_id": 0, "is_set": False, "large_size": False, "price": 0}

            if time(hour=4, minute=0) <= datetime.now().time() < time(hour=10, minute=30):      # 맥모닝 시간대일 때
                now_timezone = TIME_MORNING
                user_in = kiosk_print("카테고리를 선택해주세요\n\t0. 이전\n\t1. 맥모닝\n\t2. 사이드\n\t3. 음료\n\t4. 장바구니")
            elif time(hour=10, minute=30) <= datetime.now().time() < time(hour=14, minute=0):   # 맥런치 시간대일 때
                now_timezone = TIME_LAUNCH
                user_in = kiosk_print("카테고리를 선택해주세요\n\t0. 이전\n\t1. 맥런치\n\t2. 사이드\n\t3. 음료\n\t4. 장바구니")
            else:                                                                               # 그 외 시간대일 때
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
            print("="*30, "\n", "선택하신 메뉴 \n\n", "  이름", " "*10, "가격")
            price = 0

            # 버거 메뉴일 때
            if str(selected_item["id"])[0] == str(TYPE_BURGER):
                if selected_item["is_set"]:
                    price += menu.get(selected_item["id"])[1]       # 세트 가격
                    price += menu.get(selected_item["side_id"])[1] - menu.get(202)[1]   # 선택한 사이드 - 감튀
                    price += menu.get(selected_item["beverage_id"])[1] - menu.get(305)[1]   # 선택한 음료 - 콜라
                    price += -500 if now_timezone == TIME_LAUNCH and menu.get(selected_item["id"])[3] == 1 else 0     # 런치는 -500원
                    price += 700 if selected_item["large_size"] else 0      # 라지 사이즈는 +700원
                else:
                    price += menu.get(selected_item["id"])[2]       # 단품 가격
                    price += -500 if now_timezone == TIME_LAUNCH and menu.get(selected_item["id"])[3] == 1 else 0  # 런치는 -500원
            else:
                price = menu.get(selected_item["id"])[1]

            selected_item["price"] = price
            print(f"  - {menu.get(selected_item["id"])[0]}", " "*10, f"{price}")

            user_in = kiosk_print("\n\t0. 이전\n\t1. 장바구니에 담기", sep_line=False)

            if user_in == "0":
                progress = prev_progress
            elif user_in == "1":
                if selected_item is not None:
                    main_id = selected_item["id"]
                    side_id = selected_item["side_id"]
                    bvg_id = selected_item["beverage_id"]
                    flag = True

                    # 중복 체크
                    for i in items_cart:
                        if items_cart[i]["id"] == main_id and items_cart[i]["side_id"] == side_id and items_cart[i]["beverage_id"] == bvg_id:
                            items_cart[i]["quantity"] += 1
                            flag = False
                    # 동일한 음식이 없으면 새로 추가
                    if flag:
                        # 장바구니용 ID 생성
                        n_id = min([i for i in range(1, 99) if i not in list(items_cart.keys())])

                        if n_id is not None:
                            items_cart[n_id] = selected_item
                        else:
                            print("ID 오류")
                progress = CART

        # 장바구니
        elif progress == CART:
            order_print(items_cart, "장바구니\n")
            user_in = kiosk_print("\n\t0. 카테고리\n\t1. 수량 수정\n\t2. 결제", sep_line=False)

            # 카테고리로 이동
            if user_in == "0":
                progress = CATEGORY
            else:
                if len(items_cart) == 0:
                    print("장바구니가 비었습니다.\n")
                    continue    # => 이 continue가 있어야 무한루프에 안빠짐

                # 수량 설정
                if user_in == "1":
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
                        del items_cart[int(idx)]
                    else:       # 수량 수정
                        items_cart[int(idx)]["quantity"] = num
                elif user_in == "2":        # 결제
                    progress = PAYMENT

        # 결제하기
        elif progress == PAYMENT:
            # 카드, 현금
            user_in = kiosk_print("결제 방식을 선택해주세요\n\t0. 이전\n\t1. 카드\n\t2. 현금")
            if user_in == "0":      # 이전으로
                progress = CART
            else:
                order_print(items_cart, "결제가 완료되었습니다.\n")
                print(f"결제 방식: {("카드 1234 5678 0000 " + str(random.randrange(1000, 9999))) if user_in == "1" else "현금"}")
                print(f"주문 번호: {datetime.now()}")
                progress = START

# Start~
main()


# 키오스크를 구현하는 또 다른 방법은?