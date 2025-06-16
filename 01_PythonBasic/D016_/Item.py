import random
import ItemIDs as ids

# 아이템 클래스
class Item:
    def __init__(self, id, name, desc):
        self.__id = id
        self.__name = name
        self.__desc = desc

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def desc(self):
        return self.__desc

torch = Item(ids.TORCH, "횃불", "시야 5x5로 상승")
flashlight = Item(ids.FLASHLIGHT, "손전등", "정면 시야 상승")
potion = Item(ids.POTION, "회복약", "즉시 체력 1회복")
cloth_armor = Item(ids.CLOTH_ARMOR, "천갑옷", "1회 방어 후 소멸")
leather_armor = Item(ids.LEATHER_ARMOR, "가죽갑옷", "2회 방어 후 소멸")
plate_armor = Item(ids.PLATE_ARMOR, "판금갑옷", "3회 방어 후 소멸")
warp = Item(ids.WARP, "워프", "특정 구역 랜덤 이동")
nothing = Item(ids.NOTHING, "꽝", "아무 것도 없음")

# 확률에 따른 랜덤 아이템 생성
def get_random_item() :
    r = random.randrange(1, 101)
    if r <= 10 : # 10%
        return torch
    elif r <= 20 : # 10%
        return flashlight
    elif r <= 40 : # 20%
        return potion
    elif r <= 55: # 15%
        return cloth_armor
    elif r <= 65: # 10%
        return leather_armor
    elif r <= 70: # 5%
        return plate_armor
    elif r <= 80: # 10%
        return warp
    else: # 20%
        return nothing

# 전체 맵 셔플 좌표 리턴
def get_random_places(map_data, num):
    res = []
    random.shuffle(map_data)
    for i in range(num):
        res.append(map_data[i])
    return res

"""
Main -> Item : num, able_place
Item -> Main : pos, item
"""
def tick(tick_count, data:dict):
    if tick_count == 0:
        item_num = data["num"]
        able_place = data["able_place"]

        itembox_pos = get_random_places(able_place, item_num)
        i_send_data = []

        for i in range(item_num):
            i_send_data.append(itembox_pos[i])

        return i_send_data
    else:
        return None

if __name__ == "__main__":
    pass