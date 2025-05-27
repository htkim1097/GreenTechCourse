# str = "하마"
# print(2 ** 32)
#
# x = 10
# under_20 = x < 20
# print(f"{under_20=}")
# print(f"{not under_20=}")
#

# # 1. 간단한 대화 프로그램
# import time
#
# while True:
#     in_str = input("입력: ")
#
#     if "안녕" in in_str:
#         print("> 안녕하세요.")
#     elif "몇시" in in_str.strip():
#         print(f"> 지금은 {time.strftime("%X").split(":")[0]}시입니다.")
#     else:
#         print(in_str)

# # 2. 나누어 떨어지는 숫자
# while True:
#     in_int = int(input("정수를 입력해주세요: "))
#
#     if in_int % 2 == 0:
#         print(f"{in_int}은 2로 나누어 떨어지는 숫자입니다.")
#     else:
#         print(f"{in_int}은 2로 나누어 떨어지는 숫자가 아닙니다.")
#
#     if in_int % 3 == 0:
#         print(f"{in_int}은 3로 나누어 떨어지는 숫자입니다.")
#     else:
#         print(f"{in_int}은 3로 나누어 떨어지는 숫자가 아닙니다.")
#
#     if in_int % 4 == 0:
#         print(f"{in_int}은 4로 나누어 떨어지는 숫자입니다.")
#     else:
#         print(f"{in_int}은 4로 나누어 떨어지는 숫자가 아닙니다.")
#
#     if in_int % 5 == 0:
#         print(f"{in_int}은 5로 나누어 떨어지는 숫자입니다.")
#     else:
#         print(f"{in_int}은 5로 나누어 떨어지는 숫자가 아닙니다.")
#
# in_num = int(input("숫자를 입력해주세요> "))

# isFirst = False
# isSecond = False
# cnt = 0
# 
# for i in range(-100, 100):
#     num = str(i / 2)
#     if num.split(".")[1] == "0":
#         isFirst = True
#     else:
#         isFirst = False
#
#     if i % 2 == 0:
#         isSecond = True
#     else:
#         isSecond = False
#
#     if isFirst == isSecond:
#         cnt += 1
#
# print(cnt)
#
#
# u_input = input("4개의 조건에 대한 값을 TF로 표현하세요.")
# userres = u_input.split(" ")
#
# con1 = userres[0]
# con2 = userres[1]
# con3 = userres[2]
# con4 = userres[3]
#
# if con1 == 't':
#     if con2 == 't':
#         if con3 == 't':
#             if con4 == 't':
#                 print("밥!")
#             else:
#                 print("잔액이 없어서 못먹습니다.")
#         else:
#             print("카드가 없어서")
#     else:
#         print("지갑을 놓고와서")
# else:
#     print("밥 생각 없음")
#
# complex_list = ["abc", [1, 2, [3]], 5, 4000, "원", ["100"]]
#
# print(complex_list[1][0], complex_list[1][1], complex_list[1][2][0], str(complex_list[3])[0], complex_list[2], complex_list[4], sep="")


