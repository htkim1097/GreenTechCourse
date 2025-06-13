import math
import random
from copy import deepcopy

import MapObjectId as oid
import MapManager

class GameManager:
    def __init__(self):
        self.__map_w = 70
        self.__map_h = 30
        self.__enemy_loc_lst = []
        self.__message_list = []
        self.__max_message = 8
        self.__player_sight = 20
        self.__player_sight_shape = 1
        self.__map_manager = MapManager.R_Map(self.__map_w, self.__map_h)
        self.__map_data = []
        self.__items = []

        self.gen_map()

        self.__player_loc = self.__map_manager.player_xy
        self.__goal_loc = self.__map_manager.goal_xy

        print(self.__goal_loc)

    def move_obj(self, obj_id:int, dst:list) -> bool:
        if self.check_move(obj_id, dst):
            self.__player_loc = dst
            return True
        return False
        
    def get_map(self):
        return self.__map_data

    def get_player_xy(self):
        return self.__player_loc

    def get_goal_xy(self):
        return self.__goal_loc

    def add_itmes(self, item_xy_lst:list):
        self.__items = item_xy_lst
        for i in item_xy_lst:
            self.__map_data[i[0]][i[1]] = oid.ITEM_BOX

    def check_move(self, obj_id:int, dst:list) -> bool:
        if obj_id == oid.PLAYER:
            # 맵 바깥으로 이동이면 무시
            if dst[1] < 0 or dst[0] < 0 or self.__map_h <= dst[1] or self.__map_w <= dst[0]:
                return False

            # 이동 가능 지역의 번호는 100번대이므로 첫 번째 숫자가 1이면 이동 가능.
            if str(self.__map_data[dst[1]][dst[0]])[0] in ["1", "3"]:
                return True
        return False

    def update_enemy(self, lst):
        self.__enemy_loc_lst = lst

    def gen_map(self):
        self.__map_manager.generate()
        self.__map_data = self.__map_manager.get_map_data()

    def display_map(self):
        height = self.__map_h + 2
        width = self.__map_w + 2

        for h in range(height):
            for w in range(width):
                if h == 0 and w == 0:
                    print('┏', end='')
                elif h == 0 and w == width - 1:
                    print('┓')
                elif h == height - 1 and w == 0:
                    print('┗', end='')
                elif h == height - 1 and w == width - 1:
                    print('┛')
                elif h == 0 or h == height - 1:
                    print('━━', end='')
                elif w == 0:
                    print('┃', end='')
                elif w == width - 1:
                    print('┃')
                else:
                    dx = abs(self.__player_loc[0] - w + 1)
                    dy = abs(self.__player_loc[1] - h + 1)

                    if dx + dy <= self.__player_sight:
                        self.render_map(self.__map_data[h - 1][w - 1])

                        # 적 표시
                        for zombie in self.__enemy_loc_lst:
                            if h - 1 == zombie[1] and w - 1 == zombie[0]:
                                print("\b\b🧟", end="")
                    else:
                        print("  ", end='')
                        #print("\033[47m  \033[0m", end='')

                    # 플레이어 표시
                    if h - 1 == self.__player_loc[1] and w - 1 == self.__player_loc[0]:
                        print("\b\b☹️", end="")

    def render_map(self, obj_id):
        if obj_id == oid.ROAD:
            print("  ", end="")
        elif obj_id == oid.TREE:
            print("🌳", end="")
        elif obj_id == oid.ITEM_BOX:
            print("🎁", end="")
        elif obj_id == oid.WATER:
            print("🌊", end="")
        elif obj_id == oid.MOUNTAIN:
            print("⛰️", end="")
        elif obj_id == oid.STONE:
            print("🪨", end="")
        elif obj_id == oid.SUN:
            print("☀️", end="")
        elif obj_id == oid.WALL:
            print("🧱", end="")
        elif obj_id == oid.DOOR:
            print("🏁", end="")

    def create_mask(self, sight):
        tmp_lst = []
        tmp_pos = [sight, sight]

        for i in range(sight * 2 + 1):
            tmp_lst.append([])
            for j in range(sight * 2 + 1):
                tmp_lst[i].append(0)

        for x in range(tmp_pos[0] - sight, tmp_pos[0] + sight + 1):
            for y in range(tmp_pos[1] - sight, tmp_pos[1] + sight + 1):
                if self.get_dist(tmp_pos[0], tmp_pos[1], x, y) <= sight:
                    tmp_lst[x][y] = 1

    def get_dist(self, x, y, x2, y2):
        return math.sqrt((x - x2) ** 2 + (y - y2) ** 2)

    def get_items(self):
        return self.__items

    def add_message(self, msg:str):
        if len(self.__message_list) == self.__max_message:
            self.__message_list.remove(self.__message_list[0])
            self.__message_list.append(msg)
        else:
            self.__message_list.append(msg)

    def display_message(self):
        print()

        sep_line = "━━" * self.__map_w
        print(sep_line)
        for msg in self.__message_list:
            print(msg)

    def display_status(self, name, hp, shield, items):
        print(f"{name}")
        print(f"HP: {hp}")
        print(f"Shield: {shield}")
        print(f"Items:{items}")
