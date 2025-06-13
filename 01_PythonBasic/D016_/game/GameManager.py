import random
import MapObjectId as oid
import MapManager

class GameManager:
    def __init__(self):
        self.map_w = 0
        self.map_h = 0
        self.enemy_loc_lst = []
        self.message_list = []
        self.status_w = 70
        self.status_h = 5
        self.message_w = 70
        self.message_h = 8
        self.map_manager = MapManager.R_Map()
        self.map_manager.generate()
        self.map_data = self.map_manager.get_map_data()
        print(self.map_data)
        self.player_loc = self.map_manager.player_xy
        self.goal_loc = self.map_manager.goal_xy

    def move_obj(self, obj_id:int, dst:list) -> bool:
        if self.check_move(obj_id, dst):
            self.player_loc = dst
            return True

        return False
        
    def get_map(self):
        return self.map_data

    def set_map_size(self, map_width, map_height):
        self.map_w = map_width
        self.map_h = map_height

    def get_player_xy(self):
        return self.player_loc

    def add_itmes(self, item_xy_lst:list):
        for i in item_xy_lst:
            self.map_data[i[0]][i[1]] = oid.ITEM_BOX

    def generate_forest_map(self, is_last=False):
        # self.map_data = [
        #     [101, 101, 101, 101, 201],
        #     [201, 201, 101, 101, 201],
        #     [101, 201, 201, 101, 201],
        #     [101, 101, 101, 101, 201],
        #     [201, 101, 201, 101, 102]
        # ]

        width = self.map_w
        height = self.map_h

        room_min_size = 4  # 2x2 단위이므로 최소 4
        room_max_size = 12  # 2x2 단위이므로 짝수로
        room_count = 15

        map_data = [[oid.TREE for _ in range(width)] for _ in range(height)]

        rooms = []
        for _ in range(room_count):
            for _ in range(100):  # 최대 100번 시도
                w = random.randrange(room_min_size, room_max_size + 1, 2)
                h = random.randrange(room_min_size, room_max_size + 1, 2)
                x = random.randrange(1, width - w - 1, 2)
                y = random.randrange(1, height - h - 1, 2)
                new_room = (x, y, w, h)
                # 겹침 체크
                if any(x < rx + rw and x + w > rx and y < ry + rh and y + h > ry for rx, ry, rw, rh in rooms):
                    continue
                # 방 그리기 (2x2 단위)
                for i in range(y, y + h, 2):
                    for j in range(x, x + w, 2):
                        for dy in range(2):
                            for dx in range(2):
                                map_data[i + dy][j + dx] = oid.ROAD
                rooms.append(new_room)
                break

        # 방의 중심끼리 2x2 통로로 연결
        centers = []

        for x, y, w, h in rooms:
            cx = x + (w // 2) // 2 * 2  # 2의 배수로 맞춤
            cy = y + (h // 2) // 2 * 2
            centers.append((cx, cy))

        for i in range(1, len(centers)):
            x1, y1 = centers[i - 1]
            x2, y2 = centers[i]

            # 2x2 단위로 L자형 통로 생성
            cx, cy = x1, y1
            while cx != x2:
                step = 2 if cx < x2 else -2
                for dy in range(2):
                    for dx in range(2):
                        if 0 <= cy + dy < height and 0 <= cx + dx < width:
                            map_data[cy + dy][cx + dx] = oid.ROAD
                cx += step
            while cy != y2:
                step = 2 if cy < y2 else -2
                for dy in range(2):
                    for dx in range(2):
                        if 0 <= cy + dy < height and 0 <= cx + dx < width:
                            map_data[cy + dy][cx + dx] = oid.ROAD
                cy += step

        # 출발점, 도착점 표시 (첫 방, 마지막 방의 중심)
        # sx, sy = rooms[0][0] + (rooms[0][2] // 2) // 2 * 2, rooms[0][1] + (rooms[0][3] // 2) // 2 * 2
        # ex, ey = rooms[-1][0] + (rooms[-1][2] // 2) // 2 * 2, rooms[-1][1] + (rooms[-1][3] // 2) // 2 * 2
        #
        # map_data[sy][sx] = "🚶"
        # map_data[ey][ex] = "🏁"

        #rpg_map = mm.R_Map()
        self.player_loc = centers[0]
        #
        #
        self.map_data = map_data

        #self.map_data = rpg_map.generate()
        pass

    def check_move(self, obj_id:int, dst:list) -> bool:
        if obj_id == oid.PLAYER:
            # 맵 바깥으로 이동이면 무시
            if dst[1] < 0 or dst[0] < 0 or self.map_h <= dst[1] or self.map_w <= dst[0]:
                return False

            # 이동 가능 지역의 번호는 100번대이므로 첫 번째 숫자가 1이면 이동 가능.
            if str(self.map_data[dst[1]][dst[0]])[0] == "1":
                return True

        return False

    # TODO 연구소 맵 생성
    def generate_lab_map(self):
        lab_map = []

        for h in range(self.map_h):
            for w in range(self.map_w):
                pass

    def update_enemy(self, lst):
        self.enemy_loc_lst = lst

    def display_map(self):
        height = self.map_h + 2
        width = self.map_w + 2

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
                # else:
                #     sight_range = 5
                #
                #     for i in range(sight_range):
                #         for j in range(sight_range):
                #             pass
                #
                #
                #
                #     if self.player_loc[0] - sight_range + 3 <= w <= self.player_loc[0] + sight_range - 1 and \
                #             self.player_loc[1] - sight_range + 3 <= h <= self.player_loc[1] + sight_range - 1:
                #         self.render_map(self.map_data[h - 1][w - 1])
                #
                #         # 적 표시
                #         for zombies in self.enemy_loc_lst:
                #             for z in zombies:
                #                 if h - 1 == z[1] and w - 1 == z[0]:
                #                     print("\b\b🧟", end="")
                #     else:
                #         print("\033[32m  \033[0m", end='')
                #
                #     # 플레이어 표시
                #     if h - 1 == self.player_loc[1] and w - 1 == self.player_loc[0]:
                #         print("\b\b☹️", end="")

                else:
                    self.render_map(self.map_data[h - 1][w - 1])

                    # 플레이어 표시
                    if h - 1 == self.player_loc[1] and w - 1 == self.player_loc[0]:
                        print("\b\b☹️", end="")

                    # 적 표시
                    for zombies in self.enemy_loc_lst:
                        for z in zombies:
                            if h - 1 == z[1] and w - 1 == z[0]:
                                print("\b\b🧟", end="")


                    
                    # # 적 표시
                    # for zombies in self.enemy_loc_lst:
                    #     for z in zombies:
                    #         if h - 1 == z[1] and w - 1 == z[0]:
                    #             print("\b\b🧟", end="")

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

    def add_message(self, msg:str):
        if len(self.message_list) == self.message_h:
            self.message_list.remove(self.message_list[0])
            self.message_list.append(msg)
        else:
            self.message_list.append(msg)

    # TODO 메시지 디스플레이
    def display_message(self):
        print()

        sep_line = "━━" * self.message_w
        print(sep_line)
        for msg in self.message_list:
            print(msg)

    # TODO 플레이어 상태 디스플레이
    def display_status(self, name, hp, items, shield):
        print(f"{name}")
        print(f"HP: {hp}")
        print(f"Shield: {shield}")
        print("Items:")

        for i in items:
            print(f"{i}", end=" / ")