import random

# 상수 처리
TORCH = 311
FLASHLIGHT = 312
POTION = 313
ARMOR1 = 314
ARMOR2 = 315
ARMOR3 = 316
WARP = 317
NOTHING = 318
VACCINE = 319

# 아이템 클래스
box_queue = [] # 🚩아이템 박스
tick_c = 0
res_dic = {}
status1 = [] # 획득 아이템 나열

class Item:
   def __init__(self,id,name,effect):
       self.id = id
       self.name = name
       self.effect = effect
       self.item_box = {}

   def type_change(self, value):
       self.item_box[self.id] = []
       self.item_box[self.id].append(self.name)
       self.item_box[self.id].append(self.effect)
       self.item_box[self.id].append(value)
       return self.item_box


   @classmethod
   def tick(cls,tick_count, event_code, map1, num): # map1 = 맵 내 가능한 위치
       global tick_c
       global res_dic
       # tick 스택
       tick_c += tick_count
       # event_code = 0 아이템 생성, 1 None
       if event_code == 0:
           res_dic = {}
           box_place = ran_map(map1, num)
           for i in range(num):
               res_dic[box_place[i]] = list(random_item().keys())
           return res_dic
       # 워프삭제
       # elif event_code == 1:
       #     return ran_map(map1,1)
       else:
           return None

   @classmethod
   def give_item(cls, xy):
       tmp =[]
       global status1
       # print(res_dic[xy])
       if res_dic.get(xy) is None:
           return None
       else:
           for i in box_queue:
               if list(i.keys()) == res_dic[xy]:
                   tmp.append(i)
       del res_dic[xy]
       return tmp # [{316:[이름,효과,값]}]

# 아이템 클래스 하위
torch = Item(311,"횃불","시야 5x5로 상승")
flashlight = Item(312,"손전등","정면 시야 상승")
potion = Item(313,"회복약","즉시 체력 1회복")
armor1 = Item(314,"천갑옷","1회 방어 후 소멸")
armor2 = Item(315,"가죽갑옷","2회 방어 후 소멸")
armor3 = Item(316,"판금갑옷","3회 방어 후 소멸")
warp = Item(317,"워프","특정 구역 랜덤 이동")
nothing = Item(318,"꽝","아무 것도 없음")
vaccine = Item(319,"백신","좀비 치료제")
box_queue.append(Item.type_change(vaccine,2000)) #0
box_queue.append(Item.type_change(torch,10000)) #1
box_queue.append(Item.type_change(flashlight,20000)) #2
box_queue.append(Item.type_change(warp,100)) #3
box_queue.append(Item.type_change(potion,10)) #4
box_queue.append(Item.type_change(armor3,3)) #5
box_queue.append(Item.type_change(armor2,2)) #6
box_queue.append(Item.type_change(armor1,1)) #7
box_queue.append(Item.type_change(nothing,0)) #8


# 확률에 따른 랜덤 아이템 생성
def random_item() :
   r = random.randrange(1, 101)
   if r <= 10 : # 10%
       return box_queue[1]
   elif 10 < r <= 20 : # 10%
       return box_queue[2]
   # 워프 삭제 / 리스트 상에는 존재
   elif 20 < r <= 35 : # 15%
       return box_queue[4]
   elif 35 < r <= 45: # 10%
       return box_queue[5]
   elif 45 < r <= 60: # 15%
       return box_queue[6]
   elif 60 < r <= 80: # 20%
       return box_queue[7]
   else: # 100%
       return box_queue[8]

# 전체 맵 셔플 좌표 리턴
def ran_map(map1, num): #num = 좌표 갯수
   res = []
   random.shuffle(map1)
   for i in range(num):
       res.append(map1[i])
   return res[:num] # 인덱스 숫자 변경 가능