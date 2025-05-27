# p230 범위 자료형과 while 반복문
# while 반복문
# pass, break, continue 키워드는 반복문의 실행문 부분에 배치 가능.

# # for의 반복 대상 : 리스트, 문자열, 딕셔너리, range
# for i in range(10):
#     print(i)
#
# for i in [1, 2, 3, 4]:
#     print(i)
#
# for i in {1:100, 2:200}:
#     print(i)
#
# for i in "abcde":
#     print(i)
#
# # for 문은 시작과 끝이 정해진 반복 가능 객체를 대상으로 한다. (몇 바퀴 돌지 알고 시작한다.)
#
# # while 반복문은 ~까지 반복한다. 어떤 조건이 될 때까지 반복한다.
# # reversed() : 리스트의 순서를 반대로
# for i in reversed(range(0, 10)):    # 9,8,7,6,5,4,3,2,1,0
#     print(i)
#
# output = "*"
#
# for i in range(1, 10):
#     for j in range(0, i):
#         output += "*"
#     output += "\n"
#
# print(output)

# output = input("어떤 문자?")
#
# a = int(input("총 몇행?"))
# b = int(input("어디서부터?수직"))
#
# for i in range(1, a):
#     if i <= b:
#
#         for j in range(0, i):
#             output += output
#         output += "\n"
#     else:
#         for m in range(0, b+1):
#             output += output
#         output += "\n"
# print(output)

# output = ""
#
# for i in range(1, 15):
#     for j in range(14, i, -1):
#         output += ' '
#     for k in range(0, 2*i-1):
#         output += '*'
#     output += '\n'
# print(output)

# output = ""
# max_line = 6
# for i in range(max_line):
#     for j in range(max_line - i):
#         output += ' '
#
#     max_cols = 2 * i + 1
#     for m in range(0, max_cols):
#         if m == 0 or m == max_cols - 1:
#             output += '#'
#         elif i % 2 == 0:
#             output += '2'
#         else:
#             output += '1'
#     output += '\n'
#
# print(output)

# # while 반복문
# print(type(range(10)))
# print(list(range(10)))
#
# dicta = {1:100, 2:200, 3:300}
# print(list(dicta.keys()))

# 리스트나 딕셔너리 내부의 요소를 순회하는 반복의 경우 for을 사용
# 그러나 랜덤으로 1~100 범위 내에서 랜덤으로 48을 뽑는다면 for문을 사용하기 힘듬
# 언제 그 숫자가 나올지 알 수 없기 때문이다.
# => for 보다 while이 적합한 경우

# while 조건식:
#    실행문

# i=0
# while i<10:
#     print(f"{i+1}번째 반복")
#     i+=1

# # p242
# # 변수를 선언합니다.
# list_test = [1, 2, 1, 2]
# value = 2
#
# # list_test 내부에 value가 있다면 반복
# while value in list_test:
#     list_test.remove(value)
#
# # 출력합니다.
# print(list_test)
#

# import time
#
# number = 0
#
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1
#
# print(f"5초 동안 {number}번 반복했습니다.")
#

# break 키워드
# break 키워드는 반복무에서 벗어날 때 사용하는 키워드

# continue 키워드
# continue 키워드는 반복문의 처음으로 돌아가서 반복

# p248
# # 2
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# charcter = {}
#
# for i in range(len(key_list)):
#     charcter[key_list[i]] = value_list[i]
#
# print(charcter)
#
# # 3
# limit = 1000
# i = 1
# sum_val = 0
#
# while sum_val <= 1000:
#     sum_val += i
#     i += 1
#
#
# print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_val))

# # 4
# max_val = 0
# a = 0
# b = 0
#
# for i in range(1, 100):
#     j = 100 - i
#
#     if max_val < i * j:
#         max_val = i * j
#
# print(max_val)

# dicta={1:100, 2:200, 3:300}
# print(dicta.keys())
# print(dicta.values())
# print(dicta.items())

# list_a = [1,2,3,4,5]
# list_reverse = reversed(list_a)
# print(list_reverse)
#
# print(list_a.__iter__())    # 리스트를 이터레이터로 반환되도록 함.
# # 이터러블 : 반복 가능한 속성
# # 이터레이터 : 반복 가능 객체 자체를 의미
#
# # p252
# # 리스트를 선언하고 뒤집습니다.
# list_a = [1,2,3,4,5]    # 리스트 오브젝트 / 이터러블 / 계속 사용 가능, 실제 메모리에 모든 값이 있음.
# list_reversed = reversed(list_a) # 이터레이터 오브젝트 / 이터러블 / 한 번만 사용 가능
#
# # 출력합니다.
# print("# reversed() 함수")
# print(f"{list_reversed=}")
# print(f"{list(list_reversed)}")
# print()
#
# # 반복문을 적용해 봅니다.
# print("# reversed() 함수와 반복문")
# print("for i in reversed([1,2,3,4,5])")
# for i in reversed(list_a):
#     print("-", i)
#
# # 이터레이터는 한 번 순회하면 더 이상 사용 할 수 없다.

# # enumerate() : 인덱스와 값을 동시에 출력 가능함
# ex_lst = ["A", "B", "C"]
#
# for i, v in enumerate(ex_lst):
#     print(f"{i} : {v}")

# # p255
# # 변수를 선언합니다.
# ex_lst = ["요소A", "요소B", "요소C"]
#
# # 그냥 출력합니다.
# print("# 단순 출력")
# print(ex_lst)
# print()
#
# # enumerate() 함수를 적용해 출력합니다.
# print("# enumerate() 함수 적용 출력")
# print(enumerate(ex_lst))
#
# # list() 함수로 강제 변환해 출력합니다.
# print("# list() 함수로 강제 변환 출력")
# print(list(enumerate(ex_lst)))
# print()
#
# # for 반복문과 enumerate() 함수 조합해서 사용하기
# print("# 반복문과 조합하기")
# for i, value in enumerate(ex_lst):
#     print("{}번째 요소는 {}입니다.".format(i, value))

# 딕셔너리에 items() 함수 사용하면 딕셔너리에서 enumerate()와 같이 사용 가능

# 리스트 내포
# arr = [i * i for i in range(0, 20, 2)]
# print(arr)

# 리스트를 선언합니다.
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)