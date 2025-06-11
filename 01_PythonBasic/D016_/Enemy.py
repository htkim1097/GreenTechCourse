import MapObjectIDs as ids
import random
import heapq

g_map=[]
# 전체 맵 (0=좀비, 1=길, 2=숲(장애물), 9=플레이어)
game_map = [
    g_map
]

# 상, 하, 좌, 우, 제자리 이동 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
road = ids.ROAD
player = ids.PLAYER
n_zombie=ids.NORMAL_ZOMBIE
forest = ids.FOREST
water = ids.WATER
wall = ids.WALL

#휴리스틱함수 , 맨해튼거리 측정용
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#전체 크기를 정의하기위한 바운드함수
def in_bounds(position, map_height, map_width):
    row, col = position
    return 0 <= row < map_height and 0 <= col < map_width

#좀비의 제한된 시야를 위한 함수
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

            if abs(rel_row) + abs(rel_col) <= vision_radius:
                map_row = start_row + d_row
                map_col = start_col + d_col

                if 0 <= map_row < map_height and 0 <= map_col < map_width:
                    vision_map[d_row][d_col] = game_map[map_row][map_col]

                    if (map_row, map_col) == zombie_position:
                        zombie_rel_pos = (d_row, d_col)
                    if game_map[map_row][map_col] == player:
                        player_rel_pos = (d_row, d_col)

    return vision_map, zombie_rel_pos, player_rel_pos

#A star 함수 -> 시야범위안에 들어왔을때 최적경로계산을위한함수, 움직일때마다 장애물,위치가 갱신되므로 경로도갱신된다.
def a_star_partial(start, goal, vision_map):
    map_height = len(vision_map)
    map_width = len(vision_map[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for d_row, d_col in directions[:-1]:
            neighbor = (current[0] + d_row, current[1] + d_col)
            if 0 <= neighbor[0] < map_height and 0 <= neighbor[1] < map_width:
                if vision_map[neighbor[0]][neighbor[1]] == (forest or wall or water):
                    continue
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

#좀비의 움직임처리. 시야내에들어오면 a star함수처리. 시야밖에서 랜덤이동처리
def zombie_tick(zombie_position, player_position, game_map, vision_radius):
    vision_map, zombie_rel_pos, player_rel_pos = get_vision_map(game_map, zombie_position, vision_radius)

    if zombie_rel_pos is None:
        return zombie_position

    moved = False
    new_position = zombie_position

    if player_rel_pos is not None:
        path = a_star_partial(zombie_rel_pos, player_rel_pos, vision_map)
        if path and len(path) > 0:
            next_rel = path[0]
            new_position = (
                zombie_position[0] - vision_radius + next_rel[0],
                zombie_position[1] - vision_radius + next_rel[1]
            )
            moved = True

    if not moved:
        candidates = []
        for d_row, d_col in directions:
            next_row = zombie_position[0] + d_row
            next_col = zombie_position[1] + d_col
            if in_bounds((next_row, next_col), len(game_map), len(game_map[0])) and game_map[next_row][next_col] != (forest or wall or water):
                candidates.append((next_row, next_col))
        if candidates:
            new_position = random.choice(candidates)

    if new_position != zombie_position:
        old_row, old_col = zombie_position
        if game_map[old_row][old_col] == n_zombie:
            game_map[old_row][old_col] = road
        new_row, new_col = new_position
        if game_map[new_row][new_col] != player:
            game_map[new_row][new_col] = n_zombie

    return new_position

def find_position(game_map, target):
    for row in range(len(game_map)):
        for col in range(len(game_map[0])):
            if game_map[row][col] == target:
                return (row, col)
    return None
    #vision radius는 웬만하면 고정, (맵,좀비위치,플레이어위치,시야범위,사용자입력)
def get_final_zombie_position(initial_game_map, initial_zombie_pos=None, initial_player_pos=None, vision_radius=2, num_ticks=1):
    lst = []

   #게임맵 버그방지
    game_map = [row[:] for row in initial_game_map]

    zombie_position = initial_zombie_pos
    if zombie_position is None:
        zombie_position = find_position(game_map, n_zombie)

    player_position = initial_player_pos
    if player_position is None:
        player_position = find_position(game_map, player)

    if zombie_position is None:
        print("오류: 맵에서 좀비를 찾을 수 없습니다.")
        return None

    return [zombie_tick(zombie_position, player_position, game_map, vision_radius)]

