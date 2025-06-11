import random

class R_Map:
    START = 1001
    ROAD  = 101  # "  "
    WATER = 202  # "🌊"
    TREE  = 201  # "🌲"
    STONE  = 203  # "🪨"


    CODE_TO_SYMBOL = {
        ROAD: "  ",
        WATER: "🌊",
        TREE: "🌲",
        STONE: "🪨",
    }

    SYMBOL_CLUSTERS = [
        (WATER, 6),
        (TREE, 8),
        (STONE, 4),
    ]

    def __init__(self, width=60, height=30, room_min=4, room_max=12, room_count=8):
        self.width = width
        self.height = height
        self.room_min = room_min
        self.room_max = room_max
        self.room_count = room_count
        self.map_data = [[self.TREE for _ in range(self.width)] for _ in range(self.height)]
        self.rooms = []

    def place_rooms(self):
        for _ in range(self.room_count):
            for _ in range(1000):
                w = random.randrange(self.room_min, self.room_max+1, 2)
                h = random.randrange(self.room_min, self.room_max+1, 2)
                x = random.randrange(1, self.width - w - 1, 2)
                y = random.randrange(1, self.height - h - 1, 2)
                new_room = (x, y, w, h)
                if any(x < rx + rw and x + w > rx and y < ry + rh and y + h > ry for rx, ry, rw, rh in self.rooms):
                    continue
                for i in range(y, y + h, 2):
                    for j in range(x, x + w, 2):
                        for v in range(2):
                            for k in range(2):
                                self.map_data[i + v][j + k] = self.ROAD
                self.rooms.append(new_room)
                break

    def coner_way(self, x1, y1, x2, y2):
        cx, cy = x1, y1
        while cx != x2:
            step = 2 if cx < x2 else -2
            for dy in range(2):
                for dx in range(2):
                    if 0 <= cy + dy < self.height and 0 <= cx + dx < self.width:
                        self.map_data[cy + dy][cx + dx] = self.ROAD
            cx += step
        while cy != y2:
            step = 2 if cy < y2 else -2
            for dy in range(2):
                for dx in range(2):
                    if 0 <= cy+dy < self.height and 0 <= cx+dx < self.width:
                        self.map_data[cy + dy][cx + dx] = self.ROAD
            cy += step

    def connect_rooms(self):
        centers = []
        for x, y, w, h in self.rooms:
            cx = x + (w // 2) // 2 * 2
            cy = y + (h // 2) // 2 * 2
            centers.append((cx, cy))
        for i in range(1, len(centers)):
            x1, y1 = centers[i - 1]
            x2, y2 = centers[i]
            self.coner_way(x1, y1, x2, y2)

    def place_symbol_clusters(self):
        for code, count in self.SYMBOL_CLUSTERS:
            for _ in range(count):
                size_x = random.randint(2, 5)
                size_y = random.randint(2, 5)
                tries = 0
                while tries < 100:
                    x = random.randint(0, self.width - size_x)
                    y = random.randint(0, self.height - size_y)
                    # 출발/도착/길은 덮어쓰지 않음
                    overlap = False
                    for dy in range(size_y):
                        for dx in range(size_x):
                            if self.map_data[y+dy][x+dx] in (self.START, self.ARRIIVE, self.ROAD):
                                overlap = True
                    if not overlap:
                        for dy in range(size_y):
                            for dx in range(size_x):
                                self.map_data[y+dy][x+dx] = code
                        break
                    tries += 1

    def set_start_and_arrive(self):
        sx, sy = self.rooms[0][0] + (self.rooms[0][2] // 2) // 2 * 2, self.rooms[0][1] + (self.rooms[0][3] // 2) // 2 * 2
        ex, ey = self.rooms[-1][0] + (self.rooms[-1][2] // 2) // 2 * 2, self.rooms[-1][1] + (self.rooms[-1][3] // 2) // 2 * 2
        self.map_data[sy][sx] = self.START
        self.map_data[ey][ex] = self.ARRIIVE

    def generate(self):
        self.place_rooms()
        self.connect_rooms()
        self.set_start_and_arrive()
        self.place_symbol_clusters()
        return self.map_data

if __name__ == "__main__":
    rpg_map = R_Map()
    rpg_map.generate()