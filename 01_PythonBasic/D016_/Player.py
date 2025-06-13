status = 0  # 현재 상태
item_status = []  # 가방(인벤토리) -> item_status


from Item import Item, res_dic

class Player:
   player_list = []
   tick_count = 0
   inst = []
   login = 0
   @classmethod
   # 캐릭터 생성 함수
   def create(cls, obj):
       Player.player_list.append(obj)
       return obj


   @classmethod
   # 0. 생성 1.이동 2.이동 불가 3.아이템 획득
   def tick(cls,event_code, data=dict):
       global inst
       global login


       Player.tick_count += 1


       if event_code == 0:  # 게임 시작 시점
           inst = Player.create(Player(data["name"], x=data["x"], y=data["y"], hp=3))
           login = 1
       elif event_code == 9:
           login = 0
           print("게임이 종료되었습니다.")

       if login == 1 and event_code == 1:
           cls.move(inst, data["input_key"])
       elif login == 1 and event_code == 2:
           pass
       elif login == 1 and event_code == 3:
           cls.plus_status(inst, data["item_temp"])
       elif login == 1 and event_code == 4:  # 몬스터 만난 상황 현재 미정
           pass
       return inst.get_status_dict() if login else {}

   def __init__(self, name, hp=30, x=0, y=0):
       self.name = name
       self.x = x
       self.y = y
       self.inventory = []
       self.sight = 10000
       self.key = 0
       self.warp = 0
       self.hp = hp
       self.protect = 0


       # 상태 입력값 합 => status


   def sum_status(self):
       global status
       status = self.sight + self.key + self.warp + self.hp + self.protect
       return status

   def get_status_dict(self):
       return {
           "name": self.name,
           "x": self.x,
           "y": self.y,
           "sight": self.sight,
           "key": self.key,
           "warp": self.warp,
           "hp": self.hp,
           "protect": self.protect,
           "status":status
       }




   def plus_status(self, item_data):
       # [{상수값 : [이름,효과,value]}] => [[상수값,value],]
       for h in item_data:
           for i, j in h.items():
               item_status.append([i, j[-1]])


       # 리스트에 가장 최근에 담긴 아이템 확인 (역순으로 확인)
       # 갑옷
       if item_status[-1][0] == 316:
           print(self.protect)
           self.protect = 3
           print(self.protect)


       elif item_status[-1][0] == 315:
           if str(status)[-1] == "0" or "1" or "2":
               self.protect = 2


       elif item_status[-1][0] == 314:
           if str(self)[-1] == "0" or "1":
               self.protect = 1


       # 회복
       elif item_status[-1][0] == 313:
           self.drink_potion()
           print(f"회복약을 먹었습니다.{self.hp}")


       # # 워프 / 미 구현
       # elif item_status[-1][0] == 317:
       #     self.use_warp()
       #     pass


       # -- 시야 --
       # 횃불
       elif item_status[-1][0] == 311:
           if str(status)[0] == "1" or "2":
               self.sight = 20000


       # 손전등
       elif item_status[-1][0] == 312:
           self.sight = 30000


       # 꽝
       elif item_status[-1][0] == 318:
           pass


       return self.sum_status()


   # 이동 함수
   def move(self, input_key):
       # 1. 이동
       if input_key == "w":
           self.y -= 1
       elif input_key == "s":
           self.y += 1
       elif input_key == "a":
           self.x -= 1
       elif input_key == "d":
           self.x += 1


       new_pos = (self.x, self.y)


       item_data = Item.give_item(new_pos)


       if item_data != None:
           self.plus_status(item_data)
       else:
           print(item_data)








   # 현재 위치 정보 반환
   def my_position(self):
       print(self.x, self.y)


   # 인벤토리 목록을 보여줌
   def inventory_check(self):
       return self.inventory


   # 인벤토리에 들어온 아이템을 추가 해줌
   def inventory_save(self, item):
       self.inventory.append(item)


   # 포션을 마심
   def drink_potion(self):
       print(self.hp)
       self.hp += 1


   # 캐릭터의 체력 반환
   def get_hp(self):
       return self.hp

