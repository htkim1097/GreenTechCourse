#123123

import MapObjectId as ids
import random
import heapq

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
road = ids.ROAD
player = ids.PLAYER
n_zombie = ids.NORMAL_ZOMBIE
forest = ids.TREE
water = ids.WATER
wall = ids.WALL

ZOMBIE_TYPE = [
    {"type": "NormalZombie", "name": "일반 좀비", "rate": 50},
    {"type": "BombZombie", "name": "폭발 좀비", "rate": 5},
    {"type": "MistZombie", "name": "안개 좀비️‍️", "rate": 10},
    {"type": "ScreamZombie", "name": "괴성 좀비", "rate": 10},
    {"type": "MagicZombie", "name": "마법사 좀비‍", "rate": 5},
    {"type": "ReverseZombie", "name": "리버스 좀비", "rate": 15},
    {"type": "WeaponZombie", "name": "무기 좀비", "rate": 1}
]


# 휴리스틱 함수 (맨해튼 거리)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 유효 위치 확인
def in_bounds(position, map_height, map_width):
    row, col = position
    return 0 <= row < map_height and 0 <= col < map_width

# 시야 내 맵 추출
def get_vision_map(game_map, zombie_position, vision_radius):
    map_height = len(game_map)
    map_width = len(game_map[0])
    vision_size = 2 * vision_radius + 1

    vision_map = [[forest] * vision_size for _ in range(vision_size)]
    zombie_rel_pos = None
    player_rel_pos = None

    start_row = zombie_position[0] - vision_radius
    start_col = zombie_position[1] - vision_radius

    for d_row in range(vision_size):
        for d_col in range(vision_size):
            rel_row = d_row - vision_radius
            rel_col = d_col - vision_radius
            map_row = start_row + d_row
            map_col = start_col + d_col

            if abs(rel_row) + abs(rel_col) <= vision_radius and in_bounds((map_row, map_col), map_height, map_width):
                vision_map[d_row][d_col] = game_map[map_row][map_col]
                if (map_row, map_col) == zombie_position:
                    zombie_rel_pos = (d_row, d_col)
                if game_map[map_row][map_col] == player:
                    player_rel_pos = (d_row, d_col)

    return vision_map, zombie_rel_pos, player_rel_pos

# A* 알고리즘
def a_star_partial(start, goal, vision_map):
    map_height = len(vision_map)
    map_width = len(vision_map[0])
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    void_obj = [forest, wall, water, ids.ITEM_BOX]
    while open_list:
        current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for d_row, d_col in directions:
            neighbor = (current[0] + d_row, current[1] + d_col)
            if 0 <= neighbor[0] < map_height and 0 <= neighbor[1] < map_width:
                if vision_map[neighbor[0]][neighbor[1]] in void_obj:
                    continue
                h_score = g_score[current] + 1
                if neighbor not in g_score or h_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = h_score
                    f_score[neighbor] = h_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return []

# 좀비 한 마리 이동 처리
def zombie_tick(zombie_position, player_position, game_map, vision_radius=2):
    vision_map, zombie_rel, player_rel = get_vision_map(game_map, zombie_position, vision_radius)
    void_obj = [forest, wall, water, ids.ITEM_BOX]
    if zombie_rel is None:
        return zombie_position

    if player_rel:
        path = a_star_partial(zombie_rel, player_rel, vision_map)
        if path:
            rel_move = path[0]
            return (zombie_position[0] - vision_radius + rel_move[0],
                    zombie_position[1] - vision_radius + rel_move[1])

        # 랜덤 이동
    candidates = []
    for d_row, d_col in directions:
        next_row = zombie_position[0] + d_row
        next_col = zombie_position[1] + d_col
        if in_bounds((next_row, next_col), len(game_map), len(game_map[0])) and \
                game_map[next_row][next_col] not in void_obj:
            candidates.append((next_row, next_col))

    return random.choice(candidates) if candidates else zombie_position

def get_random_road_position(game_map):
    road_positions = [(r, c) for r in range(len(game_map)) for c in range(len(game_map[0])) if game_map[r][c] == road]
    return random.choice(road_positions) if road_positions else None

class ZombieManager:
    id_counter = 1

    def __init__(self, start_turn=0):
        self.zombies=[]
        self.max_zombies=12
        self.spawn_interval=7
        self.last_spawn_turn=start_turn
    def spawn_zombie(self,current_turn,game_map):
        if len(self.zombies) > self.max_zombies:
            return
        type_list =[]
        rate_list =[]
        for i in ZOMBIE_TYPE:
            type_list.append(i["type"])
            rate_list.append(i["rate"])

        selected = random.choices(range(len(type_list)),weights=rate_list)[0]
        selected_type = type_list[selected]
        selected_name = ZOMBIE_TYPE[selected]["name"]

        pos = get_random_road_position(game_map)
        if pos:
            new_zombie={
                "type": selected_type,
                "name": selected_name,
                "spawn_turn" : current_turn,
                "position": list(pos),
                "met_player": False
            }
            self.zombies.append(new_zombie)
    def remove_zombie(self,current_turn):
        list_zombies = []
        before = len(self.zombies)
        for zombie in self.zombies:
            if zombie["met_player"] == False:
                time_alive = current_turn - zombie["spawn_turn"]
                if time_alive < 20:
                    list_zombies.append(zombie)

            self.zombies = list_zombies  # 살아남은 좀비들로 리스트 교체

            after = len(self.zombies)

            if before != after:
                print(str(before - after) + "마리 좀비가 소멸되었습니다.")

    def my_tick(self, current_turn, game_map, player_position):
        move_list = []

        for z in self.zombies:
            prev = z["position"]
            new_pos = zombie_tick(prev, player_position, game_map)

            old_r = prev[0]
            old_c = prev[1]
            new_r = new_pos[0]
            new_c = new_pos[1]

            if game_map[old_r][old_c] == n_zombie:
                game_map[old_r][old_c] = road

            if game_map[new_r][new_c] != player:
                game_map[new_r][new_c] = n_zombie

            z["position"] = new_pos

            if new_pos == player_position:
                z["met_player"] = True

            info = {
                "name": z["name"],
                "pos": new_pos
            }
            move_list.append(info)

        if current_turn - self.last_spawn_turn >= self.spawn_interval:
            self.spawn_zombie(current_turn, game_map)
            self.last_spawn_turn = current_turn

        self.remove_zombie(current_turn)

        zombie_count = len(self.zombies)

        return [move_list, zombie_count]

    @classmethod
    def tick(cls, game_map, player_position, start_turn=0, start_count=5):
        manager = cls(start_turn)

        count = 0
        while count < start_count:
            manager.spawn_zombie(start_turn, game_map)
            count += 1

        return manager.my_tick(start_turn, game_map, player_position)
    #ZombieManager.tick(game_map, player_position)

