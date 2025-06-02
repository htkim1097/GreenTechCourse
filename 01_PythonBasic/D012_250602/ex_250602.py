# # 354 하노이 탑
# # 1. 한 번에 한개의 원판만 옮길 수 있다.
# # 2. 큰 원판이 작은 원판 위에 있어서는 안된다.
# # 원판 n개일 때, 2^n - 1 회 움직이면 옮길 수 있다.
#
# count = 0
#
# def hanoi(n:int, src="A", dst="B", sp="C"):
#     global count
#
#     if n == 1:
#         print(f"{src} -> {dst}")
#         count += 1
#
#     if n >= 2:
#         hanoi(n - 1, src=src, dst=sp, sp=dst)
#         print(f"{src} -> {dst}")
#         count += 1
#         hanoi(n - 1, src=sp, dst=dst, sp=src)
#
# user_in = int(input("원판의 개수를 입력하세요: "))
# hanoi(user_in)
# print(f"이동 횟수는 {count}회입니다.")

