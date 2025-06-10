import random

# TODO 맵 클래스화 하기
"""
속성
   - 맵 너비
   - 맵 높이
함수
   - 숲 맵 만들기
   - 연구소 맵 만들기
"""

class Map:

    def __init__(self):
        pass

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