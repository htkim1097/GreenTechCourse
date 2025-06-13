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

