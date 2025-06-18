import Item
import ItemIDs
import random

class Player:
    def __init__(self, name="", hp=3, pos=0):
        self.__name = name
        self.__pos = pos
        self.__sight = {"item":0, "remain":0}
        self.__max_hp = hp
        self.__hp = hp
        self.__armor = 0
        self.__messages = []
        self.is_pass = False

    @property
    def sight(self):
        return self.__sight

    @sight.setter
    def sight(self, val):
        self.__sight = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, val):
        self.__pos = val

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, val):
        self.__armor = val

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, val):
        self.__hp = val

    def get_player_info(self):
        data = {
            "name" : self.__name,
            "pos" : self.__pos,
            "sight" : self.__sight,
            "hp" : self.__hp,
            "armor" : self.__armor,
            "message" : self.__messages,
        }
        self.__messages = []
        return data

    # 이동 함수
    def move(self, input_key):
        try:
            if input_key == "w":
                self.__pos[1] -= 1
            elif input_key == "s":
                self.__pos[1] += 1
            elif input_key == "a":
                self.__pos[0] -= 1
            elif input_key == "d":
                self.__pos[0] += 1
        except: pass

    def use_item(self, random_place):
        item = Item.get_random_item()
        item_id = item.id

        if item_id == ItemIDs.PLATE_ARMOR:
            self.__armor = 3
            self.__messages.append("판금 갑옷을 획득했습니다.")

        elif item_id == ItemIDs.LEATHER_ARMOR:
            if self.__armor < 2:
                self.__armor = 2
                self.__messages.append("가죽 갑옷을 획득했습니다.")
            else:
                self.__messages.append("가죽 갑옷을 획득했지만, 기존 갑옷을 계속 착용합니다.")

        elif item_id == ItemIDs.CLOTH_ARMOR:
            if self.__armor < 1:
                self.__armor = 1
                self.__messages.append("천 갑옷을 획득했습니다.")
            else:
                self.__messages.append("천 갑옷을 획득했지만, 기존 갑옷을 계속 착용합니다.")

        elif item_id == ItemIDs.POTION:
            if self.__hp < self.__max_hp:
                self.__hp += 1
                self.__messages.append("회복약을 먹었습니다. 체력을 1 회복했습니다.")
            else:
                self.__messages.append("회복약을 먹었지만, 이미 체력이 최대입니다.")

        elif item_id == ItemIDs.TORCH:
            self.__sight["item"] = ItemIDs.TORCH
            self.__sight["remain"] = 15
            self.__messages.append("횃불을 획득했습니다.")

        elif item_id == ItemIDs.FLASHLIGHT:
            self.__sight["item"] = ItemIDs.FLASHLIGHT
            self.__sight["remain"] = 15
            self.__messages.append("손전등을 획득했습니다.")

        elif item_id == ItemIDs.WARP:
            self.__pos = random_place
            self.is_pass = True
            self.__messages.append("어딘가로 순간이동 됐습니다.")

        elif item_id == ItemIDs.NOTHING:
            self.__messages.append("빈 상자였습니다...")

player_inst = Player()

"""
Player -> Main : name:str, pos:list, sight:int, hp:int, armor:int, messages:list
Main -> Player : item:bool, damaged:int, name:str, init_pos:list, hp:int, input_key:str, pass:bool
"""
def tick(tick_cnt, data:dict):
    global player_inst

    if tick_cnt == 0:
        player_inst = Player(data["name"], data["hp"], data["init_pos"])

    # 시야 아이템 내구도 줄이기
    if player_inst.sight["remain"] == 1:
        player_inst.sight = {"item":0, "remain":0}
    elif player_inst.sight["remain"] > 0:
        player_inst.sight["remain"] -= 1

    data_keys = data.keys()

    # Pass
    # if player_inst.is_pass:
    #     player_inst.is_pass = False
    #     return player_inst.get_player_info()

    # 이동
    if "input_key" in data_keys:
        player_inst.move(data["input_key"])

    # 아이템 획득
    if "item" in data_keys and data["item"]:
        r = random.choice(data["able_place"])
        player_inst.use_item(r)

    # 피해
    if "damaged" in data_keys:
        value = data["damaged"]

        if player_inst.armor > 0:
            player_inst.armor -= value
        else:
            player_inst.hp -= value


    return player_inst.get_player_info()