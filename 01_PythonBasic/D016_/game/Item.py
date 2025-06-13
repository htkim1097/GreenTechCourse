import random
import MapObjectId as oid
import ItemIDs


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
MY_KRY = 320

# 아이템 클래스
box_queue = [] # 🚩아이템 박스
tick_c = 0

class Item:
   def __init__(self,id,name,effect):
       self.id = id
       self.name = name
       self.effect = effect
       self.item_box = {}


   def type_change(self, value=0):
       self.item_box[self.id] = []
       self.item_box[self.id].append(self.name)
       self.item_box[self.id].append(self.effect)
       if value != 0:
           self.item_box[self.id].append(value)
       return self.item_box

   @classmethod
   def tick(cls, tick_count, event_code, map1, num, place, last_map):
       global tick_c
       # event_code =0 아이템 생성, event_code =1 워프
       tick_c += tick_count
       if event_code == 0:
           box_place = ran_map(map1, num)
           res_dic = {}
           if last_map:
               if place == "숲":
                   res_dic[box_place[0]] = list(box_queue[0].keys())
               else:
                   res_dic[box_place[0]] = list(box_queue[9].keys())
               for i in range(num - 1):
                   res_dic[box_place[i + 1]] = list(random_item().keys())
           else:
               for i in range(num):
                   res_dic[box_place[i]] = list(random_item().keys())
           return res_dic
       elif event_code == 1:
           return ran_map(map1, num)[0]
       else:
           return None

# 아이템 클래스 하위
# TODO 모든 코드를 이 클래스 안에 넣기
torch = Item(311,"횃불","시야 5x5로 상승")
flashlight = Item(312,"손전등","정면 시야 상승")
potion = Item(313,"회복약","즉시 체력 1회복")
armor1 = Item(314,"천갑옷","1회 방어 후 소멸")
armor2 = Item(315,"가죽갑옷","2회 방어 후 소멸")
armor3 = Item(316,"판금갑옷","3회 방어 후 소멸")
warp = Item(317,"워프","특정 구역 랜덤 이동")
nothing = Item(318,"꽝","아무 것도 없음")
vaccine = Item(319,"치료제","좀비 치료제")
my_key = Item(320,"연구소 열쇠","연구소 출입 가능")
box_queue.append(Item.type_change(my_key)) #1
box_queue.append(Item.type_change(torch)) #2
box_queue.append(Item.type_change(flashlight)) #3
box_queue.append(Item.type_change(warp)) #4
box_queue.append(Item.type_change(potion)) #5
box_queue.append(Item.type_change(armor3,value=3)) #6
box_queue.append(Item.type_change(armor2,value=2)) #7
box_queue.append(Item.type_change(armor1,value=1)) #8
box_queue.append(Item.type_change(nothing)) #9
box_queue.append(Item.type_change(vaccine)) #10




# 확률에 따른 랜덤 아이템 생성
def random_item() :
   r = random.randrange(1, 101)
   if r <= 5 : # 5%
       return box_queue[1]
   elif 5 < r <= 10 : # 5%
       return box_queue[2]
   elif 10 < r <= 20 : # 10%
       return box_queue[3]
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


# 맵 내 랜덤 좌표 생성 / 워프 좌표
def ran_map(map1,num): #num = 좌표 갯수
   res = []
   for i in range(len(map1)):
       for j in range(len(map1[0])):
           if map1[i][j] == oid.ROAD:
               res.append((i,j))
               random.shuffle(res)
   return res[:num] # 인덱스 숫자 변경 가능