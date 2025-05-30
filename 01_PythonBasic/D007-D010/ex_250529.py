# # 재귀 함수
# def factorial(n):
#     output = 1
#     for i in range(1, n + 1):
#         output *= i
#
#     return output
#
# print(f"1!:", factorial(1))
# print(f"1!:", factorial(2))
# print(f"1!:", factorial(3))
# print(f"1!:", factorial(4))

# # 메모 변수를 만듭니다.
# dictionary = {
#     1: 1,
#     2: 1
# }
#
# def fibonacci(n):
#     if n in dictionary:
#         # 메모가 되어 있으면 메모된 값을 리턴
#         return dictionary[n]
#     else:
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output
#
# print(f"{fibonacci(10)=}")
# print(f"{fibonacci(20)=}")
# print(f"{fibonacci(30)=}")
# print(f"{fibonacci(40)=}")
# print(f"{fibonacci(50)=}")

