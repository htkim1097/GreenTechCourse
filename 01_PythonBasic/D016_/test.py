# import random
#
# arr = []
# for i in range(5):      # 행
#     arr.append([])
#     for _ in range(5): # 열
#         arr[i].append(random.randint(0, 4))
#
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if arr[i][j] == 0:
#             print("♟️", end="")
#         elif arr[i][j] == 1:
#             print("❤️", end="")
#         elif arr[i][j] == 2:
#             print("😍", end="")
#         elif arr[i][j] == 3:
#             print("🀄", end="")
#         elif arr[i][j] == 4:
#             print("🧱", end="")
#     print()
import math

# 하얀색
# \033[47m  \033[0m
#
# """
# 0: 플레이어
# 1: 길
# 2: 숲
# 9: 골인
# """
# # 맵 코드
# m_map = [
#     [0, 1, 1, 1, 2],
#     [2, 2, 1, 1, 2],
#     [1, 2, 2, 1, 2],
#     [1, 1, 1, 1, 2],
#     [2, 1, 2, 1, 9]
# ]
#
# for i in range(len(m_map)):
#     for j in range(len(m_map[0])):
#         if m_map[i][j] == 0:
#             print("♟️", end="")
#         elif m_map[i][j] == 1:
#             print("", end="")
#         elif m_map[i][j] == 2:
#             print("🌳", end="")
#         elif m_map[i][j] == 9:
#             print("🏁", end="")
#     print()

m_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

pos = [5, 5]
pos2 = [3, 4]

def get_dist(x, y, x2, y2):
    return math.sqrt((x - x2) ** 2 + (y - y2) ** 2)

sight = 4

# 쇄기형
dirc = [1, 0, 0, 0]
for x in range(pos[0] - (sight * dirc[0]), pos[0] + (sight * dirc[1]) + 1):
    if dirc[0] == 1 or dirc[1] == 1:
        count = abs(x - pos[0])
    for y in range(pos[1] - (sight * dirc[2]), pos[1] + (sight * dirc[3]) + 1):
        if dirc[2] == 1 or dirc[3] == 1:
            count = abs(y - pos[0])

        for i in range(count):
            if dirc[0] == 1 or dirc[1] == 1:
                m_map[y + i][x] = 0
                m_map[y - i][x] = 0
            else:
                m_map[y][x + i] = 0
                m_map[y][x - i] = 0

# 원형
# for x in range(pos[0] - sight, pos[0] + sight + 1):
#     for y in range(pos[1] - sight, pos[1] + sight + 1):
#         if get_dist(pos[0], pos[1], x, y) <= sight:
#             print(x, y)
#             m_map[x][y] = 0
#             count += 1



for i in range(len(m_map)):
    for j in range(len(m_map[0])):
        print(m_map[i][j], end='')
    print()




