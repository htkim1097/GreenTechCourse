import math
import MapObjectId as ObjId
import MapManager
import MyUtils as util

class GameManager:
    def __init__(self):
        self.__map_w = 70
        self.__map_h = 30
        self.__enemy_pos_lst = []
        self.__message_list = []
        self.__max_message = 8
        self.__player_sight = 20
        self.__player_sight_shape = 1
        self.__map_manager = MapManager.R_Map(self.__map_w, self.__map_h)
        self.__map_data = []

        self.gen_map()

        self.__player_pos = self.__map_manager.player_pos
        self.__goal_pos = self.__map_manager.goal_pos

    def clear_messages(self):
        self.__message_list.clear()

    def move_obj(self, obj_id:int, dst:list):
        self.__player_pos = dst
        
    def get_map(self):
        return self.__map_data

    def get_init_player_xy(self):
        return self.__player_pos

    def get_goal_xy(self):
        return self.__goal_pos

    def add_itmes(self, item_xy_lst):
        for i in item_xy_lst:
            self.__map_data[i[1]][i[0]] = ObjId.ITEM_BOX

    def get_able_place(self):
        tmp_lst = []

        for y in range(len(self.__map_data)):
            for x in range(len(self.__map_data[0])):
                dx = abs(self.__player_pos[0] - x + 1)
                dy = abs(self.__player_pos[1] - y + 1)

                if self.__map_data[y][x] == ObjId.ROAD and dx + dy <= self.__player_sight + 3:
                    tmp_lst.append((x, y))

        return tmp_lst

    def check_move(self, obj_id:int, dst:list) -> bool:
        if obj_id == ObjId.PLAYER:
            # 맵 바깥으로 이동이면 무시
            if dst[1] < 0 or dst[0] < 0 or self.__map_h <= dst[1] or self.__map_w <= dst[0]:
                return False

            # 이동 가능 지역의 번호는 100번대이므로 첫 번째 숫자가 1이면 이동 가능.
            if str(self.__map_data[dst[1]][dst[0]])[0] in ["1", "3"]:
                return True
        return False

    def update_enemy(self, enemy_lst):
        self.__enemy_pos_lst = enemy_lst

    def gen_map(self):
        self.__map_manager.generate()
        self.__player_pos = self.__map_manager.player_pos

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
                    dx = abs(self.__player_pos[0] - w + 1)
                    dy = abs(self.__player_pos[1] - h + 1)

                    if dx + dy <= self.__player_sight:
                        self.render_map(self.__map_data[h - 1][w - 1])

                        # 적 표시
                        for zombie in self.__enemy_pos_lst:
                            pos = zombie.pos
                            if h - 1 == pos[1] and w - 1 == pos[0]:
                                print("\b\b🧟", end="")
                    else:
                        print("  ", end='')
                        #print("\033[47m  \033[0m", end='')

                    # 플레이어 표시
                    if h - 1 == self.__player_pos[1] and w - 1 == self.__player_pos[0]:
                        print("\b\b☹️", end="")

    def render_map(self, obj_id):
        if obj_id == ObjId.ROAD:
            print("  ", end="")
        elif obj_id == ObjId.TREE:
            print("🌳", end="")
        elif obj_id == ObjId.ITEM_BOX:
            print("🎁", end="")
        elif obj_id == ObjId.WATER:
            print("🌊", end="")
        elif obj_id == ObjId.MOUNTAIN:
            print("⛰️", end="")
        elif obj_id == ObjId.STONE:
            print("🪨", end="")
        elif obj_id == ObjId.SUN:
            print("☀️", end="")
        elif obj_id == ObjId.WALL:
            print("🧱", end="")
        elif obj_id == ObjId.DOOR:
            print("🏁", end="")

    def del_item(self, pos:list):
        self.__map_data[pos[1]][pos[0]] = ObjId.ROAD

    def get_place_type(self, pos:list):
        return self.__map_data[pos[1]][pos[0]]

    def create_mask(self, sight):
        tmp_lst = []
        tmp_pos = [sight, sight]

        for i in range(sight * 2 + 1):
            tmp_lst.append([])
            for j in range(sight * 2 + 1):
                tmp_lst[i].append(0)

        for x in range(tmp_pos[0] - sight, tmp_pos[0] + sight + 1):
            for y in range(tmp_pos[1] - sight, tmp_pos[1] + sight + 1):
                if util.calc_dist(tmp_pos[0], tmp_pos[1], x, y) <= sight:
                    tmp_lst[x][y] = 1

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
            print(msg[0])

    def display_status(self, p_data:dict):
        try:
            print(f"{p_data["name"]}")
            print(f"HP: {p_data["hp"]}")
            print(f"armor: {p_data["armor"]}")
        except:
            pass
