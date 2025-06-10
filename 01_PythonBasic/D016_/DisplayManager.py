import random

# 게임 매니저
#  - 이동 체크
#  - 각 조의 속성, 메서드 호출만
#  - 플레이어와 적 사이에서 통보
#  - 메시지 출력

# 맵
#  - 맵 생성
#  - 맵 코드 관리

# 우선순위
# 캐릭터
# 몬스터
# 아이템

# TODO 맵 오브젝트 코드 정의

class DisplayManager:
    def __init__(self):
        self.map_w = 0
        self.map_h = 0
        self.map = [[]]

    def set_game(self, map_width, map_height):
        self.map_w = map_width
        self.map_h = map_height

    def generate_forest_map(self):
        self.map = [["🌲" for _ in range(self.map_w)] for _ in range(self.map_h)]

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
                else:
                    print(self.map[h-1][w-1], end='')

    def generate_maze_map(self, width=60, height=40):
        # 전부 숲으로 초기화
        grid = [["🌲" for _ in range(width)] for _ in range(height)]

        # 중앙 강 좌표
        river_start = 27
        river_end = 32
        bridge_y = height // 2  # 다리 위치 (y=15)

        # 강을 세로로 채우기
        for y in range(height):
            for x in range(river_start, river_end + 1):
                grid[y][x] = "🌊"

        # 다리 놓기 (강 중앙 가로 길)
        for x in range(river_start, river_end + 1):
            grid[bridge_y][x] = "  "  # 다리

        # 미로형 길 생성 (강 양쪽에)
        def carve_maze():
            for _ in range(300):  # 길 수 늘림
                # 강 왼쪽(x=0~26) 또는 오른쪽(x=33~59) 중에서 랜덤 시작점 선택
                x = random.choice(list(range(1, river_start - 1)) + list(range(river_end + 1, width - 1)))
                y = random.randint(1, height - 2)
                direction = random.choice([(0, 1), (1, 0), (-1, 0), (0, -1)])  # 상하좌우
                length = random.randint(3, 7)

                for _ in range(length):
                    if 0 < x < width - 1 and 0 < y < height - 1:
                        if not (river_start <= x <= river_end):  # 강 제외
                            grid[y][x] = "  "
                    x += direction[0]
                    y += direction[1]

        carve_maze()

        # 출력
        for row in grid:
            print("".join(row))

    # TODO 메시지 디스플레이
    # TODO 플레이어 상태 디스플레이
