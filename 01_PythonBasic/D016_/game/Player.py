class Player:
    player_list = []
    tick_count=0
    ch = ""

    @classmethod
    # 캐릭터 생성 함수
    def create(cls,obj):
        Player.player_list.append(obj)

    @classmethod
    def tick(cls,count, event_code, data:dict):
        global ch
        if event_code == 0: #게임 시작 시점
            ch = Player.create(Player("a",x=0,y=0,hp=3))
        elif event_code == 1: # 이동 불가
            pass
        elif event_code == 2: # 이동 가능
            cls.move(ch, data["input_key"])


            Player.tick_count+=1

    # { tick: , 행동: , 상태: , ... }
    # 모든 동작은 각 모듈
    # 반환 받은 값으로 표시
    # 각 모듈과 주고 받을 인터페이스 정의
    #

    is_forest = True

    # 캐릭터가 가지고있는 속성값들
    def __init__(self,name,x=0,y=0,hp=3):
        self.x = x
        self.y = y
        self.hp = hp
        self.shield = 0
        self.vision = 0
        self.armor = None
        self.vision_item = None
        self.inventory = []

    # 이동 함수
    def move(self, input_key):
            if input_key == "W":
                self.y -= 1
            elif input_key == "S":
                self.y += 1
            elif input_key == "A":
                self.x -= 1
            elif input_key == "D":
                self.x += 1

    # 현재 위치 정보 반환
    def my_position(self):
            return self.x,self.y

    # 시야 아이템 착용 함수 None : 기본 311: 횟불 312:손전등
    def use_vision_item(self,item):
        if item == None:
            self.vision_item = None
        elif item == 311:
            self.vision_item = 311
        elif item == 312:
            self.vision_item = 312

    # 현재 시야 정보 확인
    def get_vision(self):
        # None: 아무것도 착용중이 아닐때는 나의 시야는 3x3(0)이 된다.
        if self.vision_item == None:
            self.vision = 0
        # 311: 횟불 착용중 일시 나의 시야는 5x5(1)이 된다.
        elif  self.vision_item == 311:
            self.vision = 1
        # 312: 손전등 착용중 일시 나의 시야는 원뿔형(2)이 된다.
        elif  self.vision_item == 312:
            self.vision = 2

        return self.vision

    # 갑옷 아이템 착용 함수 None: 기본 314: 천갑옷, 315: 가죽갑옷, 316:판금갑옷
    def use_armor(self,item):
        if item == None:
            self.armor = None
        elif item == 314:
            self.armor = 314
        elif item == 315:
            self.armor = 315
        elif item == 316:
            self.armor = 316

    # 현재 갑옷 정보에 따라서 쉴드(?)를 부여 하는 함수
    def set_use_item(self):
        if self.armor == None:
            self.shield = 0
        elif self.armor == 314:
            self.shield = 1
        elif self.armor == 315:
            self.shield = 2
        elif self.armor == 316:
            self.shield = 3





    # 틱 쪽에서 좀비로 공격을 받고 Hp나 쉴드를 감소시키고 쉴드,hp 상태를 넘겨줌.
    def take_damage(self,damage):
            self.armor_check()
            # 방어구 착용중 일시
            if self.armor:
                    self.shield -= damage
            # 방어구 미 착용시
            else:
                    self.hp -= damage
            return self.shield, self.hp

    # 현재 나의 쉴드를 넘겨줌.
    def get_shield(self):
        return self.shield

    # 피해를 받앗을때 현재 나의 쉴드에 따라 갑옷 착용 여부를 반환 해줌 0이되면 갑옷을 벗도록
    def armor_check(self):
            if self.shield == 0:
                   self.armor = None

    # 인벤토리 목록을 보여줌
    def inventory_check(self):
        return self.inventory

    # 인벤토리에 들어온 아이템을 추가 해줌
    def inventory_save(self,item):
        self.inventory.append(item)


# 4조: 1번 아이템 사용 -> 2조: 사용한 1번 아이템을 인벤토리에서 꺼냄(방출) -> 아이템이 어떤 아이템인지를 확인후 내 상태를 변화시킨다.
    def use_item(self,number):
        use_item_number = self.inventory.remove(number)
        # 만약 사용한 아이템이 시야 관련 아이템 311번 혹은 312번이라면 시야 아이템 착용 함수에 아이템 정보를 넘겨 착용한다.
        if use_item_number == 311 and use_item_number == 312:
            self.use_vision_item(use_item_number)
        # 만약 사용한 아이템이 갑옷 관련 아이템 314번부터 316번이라면 갑옷 아이템 착용 함수에 아이템 정보를 넘겨 착용한다.
        elif use_item_number == 314 and use_item_number == 315 and use_item_number == 316:
            self.use_armor(use_item_number)
        # 317







    # 포션을 마심
    def drink_potion(self):
        self.hp += 1

    # 캐릭터의 체력 반환
    def get_hp(self):
        return self.hp



# self.x = x
#         self.y = y
#         self.hp = hp
#         self.shield = 0
#         self.vision = 0
#         self.armor = None
#         self.vision_item = None
#         self.inventory = []





