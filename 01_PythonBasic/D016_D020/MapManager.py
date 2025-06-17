import random
import MapObjectId as objId
import math

class R_Map:
    # 방 중앙에 배치할 오브젝트 목록
    CENTER_OBJECTS = [objId.WATER, objId.MOUNTAIN, objId.STONE, objId.SUN, objId.WALL]

    def __init__(self, width, height, room_min=4, room_max=10, room_count=15):
        self.width = width             # 맵 가로
        self.height = height           # 맵 세로
        self.room_min = room_min       # 방의 최소 크기
        self.room_max = room_max       # 방의 최대 크기
        self.room_count = room_count   # 방 개수
        self.player_pos = []
        self.goal_pos = []
        self.map_data = []
        self.rooms = []

    def place_rooms(self):
        # room_count만큼 방을 생성
        for i in range(self.room_count):
            # 방 배치를 위한 랜덤 시도 (최대 1000번)
            for j in range(1000):
                # 방의 가로, 세로 크기 랜덤 지정 (짝수)
                w = random.randrange(self.room_min, self.room_max+1, 2)
                h = random.randrange(self.room_min, self.room_max+1, 2)
                # 방의 시작 좌표 랜덤 지정 (짝수)
                x = random.randrange(1, self.width - w - 1, 2)
                y = random.randrange(1, self.height - h - 1, 2)
                new_room = (x, y, w, h)
                # 기존 방과 겹치지 않으면 진행
                if any(x < rx + rw and x + w > rx and y < ry + rh and y + h > ry for rx, ry, rw, rh in self.rooms):
                    continue
                # 방 내부를 ROAD로 채움 (2x2 단위)
                for i in range(y, y + h, 2):
                    for j in range(x, x + w, 2):
                        for v in range(2):
                            for k in range(2):
                                self.map_data[i + v][j + k] = objId.ROAD
                self.rooms.append(new_room)
                break  # 방 하나 배치 완료


    def coner_way(self, x1, y1, x2, y2):
        # 두 점(x1,y1), (x2,y2) 사이를 연결하는 길 생성
        # 경로는 먼저 x축, 그다음 y축으로 이동 (코너 방식)
        cx, cy = x1, y1
        # x축 이동
        while cx != x2:
            step = 2 if cx < x2 else -2
            for dy in range(2):
                for dx in range(2):
                    if 0 <= cy + dy < self.height and 0 <= cx + dx < self.width:
                        self.map_data[cy + dy][cx + dx] = objId.ROAD
            cx += step
        # y축 이동
        while cy != y2:
            step = 2 if cy < y2 else -2
            for dy in range(2):
                for dx in range(2):
                    if 0 <= cy+dy < self.height and 0 <= cx+dx < self.width:
                        self.map_data[cy + dy][cx + dx] = objId.ROAD
            cy += step


    def connect_rooms(self):
        # 각 방의 중심 좌표 계산
        centers = []
        for x, y, w, h in self.rooms:
            cx = x + (w // 2) // 2 * 2  # 방의 중심 x좌표 (짝수)
            cy = y + (h // 2) // 2 * 2  # 방의 중심 y좌표 (짝수)
            centers.append((cx, cy))
        # 각 방의 중심을 순서대로 연결
        for i in range(1, len(centers)):
            x1, y1 = centers[i - 1]
            x2, y2 = centers[i]
            self.coner_way(x1, y1, x2, y2)


    def place_center_objects(self):
        # 각 방의 중앙에 오브젝트 배치
        for x, y, w, h in self.rooms:
            room_area = w * h
            # 방의 중심 좌표 계산
            cx = x + (w // 2) // 2 * 2
            cy = y + (h // 2) // 2 * 2
            #todo 각 방의 코너에 오브젝트 배치?
            co_y = y + (h // 3) // 3*3

            #todo 하나더?
            # CENTER_OBJECTS 중 랜덤 선택
            obj1 = random.choice(self.CENTER_OBJECTS)

            #중심 2x2 영역에 오브젝트 배치 (시작/도착지가 아니면)
            for dy in range(1):
                for dx in range(1):
                    if cy + dy != self.player_pos[1] and cx + dx != self.player_pos[0] and cy + dy != self.goal_pos[1] and cx + dx != self.goal_pos[0]:
                        self.map_data[cy + dy][cx + dx] = obj1
                    if co_y + dy != self.player_pos[1] and cx + dx != self.player_pos[0] and co_y + dy != self.goal_pos[1] and cx + dx != self.goal_pos[0]:
                        self.map_data[co_y + dy][cx + dx] = obj1

            # 방이 크면(면적 36 이상) 추가 오브젝트 배치
            if room_area >= 36:
                tries = 0
                while tries < 30:
                    rx = random.randint(x, x + w - 2)
                    ry = random.randint(y, y + h - 2)
                    # 중심과 겹치지 않게
                    if not (abs(rx-cx) < 2 and abs(ry-cy) < 2):
                        obj2 = random.choice(self.CENTER_OBJECTS)
                        for dy in range(2):
                            for dx in range(2):
                                if ry + dy != self.player_pos[1] and rx + dx != self.player_pos[0]:
                                    self.map_data[ry + dy][rx + dx] = obj2
                        break
                    tries += 1


    def set_start_and_arrive(self):
        random.shuffle(self.rooms)

        for y in range(self.height):
            for x in range(self.width):
                if self.map_data[y][x] in [objId.PLAYER, objId.DOOR]:
                    self.map_data[y][x] = objId.ROAD

        sx = self.rooms[0][0] + (self.rooms[0][2] // 2) // 2 * 2
        sy = self.rooms[0][1] + (self.rooms[0][3] // 2) // 2 * 2
        ex = self.rooms[-1][0] + (self.rooms[-1][2] // 2) // 2 * 2
        ey = self.rooms[-1][1] + (self.rooms[-1][3] // 2) // 2 * 2

        self.map_data[sy][sx] = 101
        self.map_data[ey][ex] = objId.DOOR

        dist = math.sqrt((sx - ex) ** 2 + (sy - ey) ** 2)
        return dist, sy, sx, ey, ex

    def generate(self):
        self.map_data = [[objId.TREE for i in range(self.width)]for j in range(self.height)]
        self.rooms = []

        self.place_rooms()
        self.connect_rooms()

        max_tries = 10
        for tries in range(1, max_tries + 1):
            data = self.set_start_and_arrive()
            current_dist = data[0]
            if current_dist >= 20:
                self.player_pos = [data[2], data[1]]
                self.goal_pos = [data[4], data[3]]
                break

        self.place_center_objects()

    def get_map_data(self):
        return self.map_data