import MapObjectId as ids
import random

# 방향 및 맵 상수 설정
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
road = ids.ROAD
player = ids.PLAYER
n_zombie = ids.NORMAL_ZOMBIE
forest = ids.TREE
water = ids.WATER
wall = ids.WALL
item = ids.ITEM_BOX

game_map=[[101,101,101,101,201],
          [101,101,101,101,201],
          [101,101,101,101,201],
          [101,101,101,101,201],
          [101,101,101,101,201]]




class Zombie:
    zombies = []
    max_zombies = 12
    spawn_interval = 7

    def __init__(self,position=None, start_turn=0):
        self.position = position
        self.start_turn = start_turn
        self.met_player = False

    @classmethod
    def init_zombie(self,game_map):
        road_positions = []
        for r in range(len(game_map)):
            for c in range(len(game_map[0])):
                if game_map[r][c] == road:
                    road_positions.append((r, c))

        if road_positions:
            return random.choice(road_positions)
        else:
            return None
    @classmethod
    def spawn_zombie(cls,game_map):
        if len(cls.zombies) >= cls.max_zombies:
            return None

        pos=cls.init_zombie(game_map)

        if pos:
            new_zombie = cls(pos)
            cls.zombies.append(new_zombie)
            return pos
        else:
            return None

    @classmethod
    def get_zombie_positions(cls):
        positions = []
        for z in cls.zombies:
            r = z.position[0]
            c = z.position[1]
            positions.append([r, c])
        return positions

    @classmethod
    def return_positions(cls, game_map, count=1):
        for _ in range(count):
            cls.spawn_zombie(game_map)
        return cls.get_zombie_positions()






















# def get_random_road_position(game_map):
#     road_positions = []
#
#     for r in range(len(game_map)):  # 첫 번째 for문: 행 순회
#         for c in range(len(game_map[0])):  # 두 번째 for문: 열 순회
#             if game_map[r][c] == road:  # 도로인 위치 찾기
#                 road_positions.append((r, c))  # 도로 위치 추가
#
#     if road_positions:  # 도로 위치가 존재한다면
#         return random.choice(road_positions)  # 랜덤으로 하나 선택해서 반환
#     else:
#         return None
