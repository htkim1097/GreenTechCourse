# # p196 ~
# # 문자열 : + * 연산 가능
# # 숫자 : + - / * // % ** 연산 가능
# # 리스트 : + * 연산 가능
#
# # p196 리스트 연산자
# # 리스트를 선언합니다.
# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
#
# # 출력합니다.
# print("# 리스트")
# print(f"{list_a = }")
# print(f"{list_b = }")
# print()
#
# # 기본 연산자
# print("# 리스트 기본 연산자")
# print(f"{list_a + list_b = }")
# print(f"{list_a * 3 = }")
# print()
#
# # 함수
# print("# 길이 구하기")
# print(f"{len(list_a) = }")
#
# # 문자열과 리스트의 공통 사용방법
# # len(), *, +, 인덱싱, 슬라이싱 가능
# # 두 자료형 모두 열 구조

# ----------------------------

# # p.196 리스트에 요소 추가하기
# # 문자열은 추가가 불가능, 할당 후 수정 불가.
# # 리스트는 추가, 수정이 가능.
#
# # 리스트.append()
# # 리스트 전용함수 append를 사용
# # 리스트.append(추가할 요소) : 마지막 자리에 추가하는 방법
# # 리스트.insert(위치, 추가할 요소) : 위치 지정하여 추가하는 방법
#
# # p.198 리스트에 요소 추가하기
# # 리스트를 선언합니다.
# lst_a = [1, 2, 3]
#
# # 리스트 뒤에 요소 추가하기
# print("# 리스트 뒤에 요소 추가하기")
# lst_a.append(4)
# lst_a.append(5)
# print(lst_a)
# print()
#
# # 리스트 중간에 요소 추가하기
# print("# 리스트 중간에 요소 추가하기")
# lst_a.insert(0, 10)
# print(lst_a)
#
# # 문자열은 불변 객체
# # 리스트는 가변 객체
#
# # extend() 함수는 + 와 동일한 동작을 함
# lst_a.extend([10, 20, 30])
# print(lst_a)
# print(lst_a + [40, 50, 60])

# # 리스트 내 요소 제거하기
# # 1. 값을 통한 제거
# # 2. 위치를 통한 제거 : del, pop()
#
# # pop() : 마지막 요소가 제거된다.
# # pop(인덱스) : 인덱스의 요소가 제거된다.

# # p.202 리스트 요소 하나 제거하기
# lst = [0, 1, 2, 3, 4, 5]
# print("# 리스트의 요소 하나 제거하기")
#
# # 제거 방법[1] - del 키워드
# del lst[1]
# print("del lst[1]:",lst)
#
# # 제거 방법[2] - pop()
# lst.pop(2)
# print("pop(2):",lst)

# # 슬라이싱을 이용한 여러개 삭제
# lst=[1,2,3,4,5]
# del lst[2:]
# print(lst)

# # 값으로 제거 : remove()
# lst = [1,2,3,4,5,6]
# lst.remove(4)
# print(lst)
#
# # 중복 값이 있을 때, 왼쪽 첫 번째만 제거
# lst_a = [100, 1, 100]
# lst_a.remove(100)
# print(lst_a)
#
# # 리스트 초기화 : clear()
# lst.clear()
# print(lst)

# # 리스트의 정렬 : sort()
# lst = [100, 200, 3, 2, 90]
# lst.sort() # 오름차순으로 정렬
# print(lst)
# lst.sort(reverse=True) # 내림차순으로 정렬
# print(lst)

# --------------------------

# array = [1,2,3]
# # 리스트의 요소 수 만큼 실행
# for i in array: # array 리스트에 있는 요소를 처음부터 하나씩 i에 넣음
#     print(i)
#

# lst = [
#     [1, 2, 3],
#     [4, 5, 6, 7],
#     [8, 9]
# ]
#
# for i in lst:
#     print(i)
#
# for i in lst:
#     for j in i:
#         print(j)

# a = [1, 2, 3, 4]
# b = [*a, *a]
# print(b)
#
# c = [*a, 5]
# print(c)

# -----------------------------
# 확인문제
# # 5
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in range(0, len(numbers) // 2):
#     j = i * 2 + 1
#     print(f"{i=}, {j=}")
#     numbers[j] = numbers[j] ** 2
#
# print(numbers)

# # 4
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output = [[], [], []]
#
# for number in numbers:
#     output[(number-1)%3].append(number)
#
# print(output)

# # 3
# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
#
# for i in numbers:
#     if i % 2 == 0:
#         print(f"{i}는 짝수입니다.")
#     else:
#         print(f"{i}는 홀수입니다.")
#
# for i in numbers:
#     print(f"{i}는 {len(str(i))} 자릿수입니다.")
#
# # 2
# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
#
# for number in numbers:
#     if number >= 100:
#         print("- 100 이상의 수: ", number)

# -------------------------------------

# # 중간 점검 문제
# a = 300
# b = "22"
# testlist = [a, b, "test", len(b), 60]
#
# sum = 0
# for i in testlist:
#     if type(i) == int:
#        sum += i
#
# if sum % 2 == 0:
#     print(f"합은 {sum}이며 짝수입니다.")
# else:
#     print(f"합은 {sum}이며 홀수입니다.")

# --------------------------------------

# 딕셔너리: 데이터 타입 중 하나, 여러 요소를 담는다.
# 키(key):값(value)

# 리스트는 인덱스 기반으로 값 저장
# 딕셔너리는 키를 기반으로 값 저장

# """
# {
#     키A:값A,
#     키B:값B,
#     키C:값C
# }
# """
#
# mw = {"등급":1, "높이":400, "너비":600, "가격":80000}
# print(mw["높이"])
#
# print(mw)
#
# # 타 언어의 배열은 메모리에 순차적으로 저장됨
# # 반면, 리스트는 메모리에 순서대로 저장되지 않는다.
#

# p219 딕셔너리의 요소에 접근하기
# 딕셔너리를 선언합니다.
# dictionary = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임",
#     "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin" : "필리핀"
# }
#
# # 출력합니다.
# print("name", dictionary["name"])
# print("type:", dictionary["type"])
# print("ingredient:", dictionary["ingredient"])
# print("origin:", dictionary["origin"])
# print()
#
# # 값을 변경합니다.
# dictionary["name"] = "8D 건조 망고"
# print("name:", dictionary["name"])

# # p222 딕셔너리에 요소 추가하기
# # 딕셔너리를 선언합니다.
# dictionary = {}
#
# # 요소 추가 전에 내용을 출력해 봅니다.
# print("요소 추가 이전: ", dictionary)
#
# # 딕셔너리에 요소를 추가합니다.
# dictionary["name"] = "새로운 이름"
# dictionary["head"] = "새로운 정신"
# dictionary["body"] = "새로운 몸"
#
# # 출력합니다.
# print("요소 추가 이후: ", dictionary)
#
# # p222 딕셔너리에 요소 제거하기
# # 딕셔너리를 선언합니다.
# dictionary = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임"
# }
#
# # 요소 제거 전에 내용을 출력해 봅니다.
# print("요소 제거 이전: ", dictionary)
#
# # 딕셔너리의 요소를 제거합니다.
# del dictionary["name"]
# del dictionary["type"]
#
# # 요소 제거 후에는 내용을 출력해 봅니다.
# print("요소 제거 이후: ", dictionary)
#

# # 딕셔너리 전용 함수
# dict_key={"name":"mango"}
# print(dict_key["name"]) # 조회 방법1
# print(dict_key.get("fds"))  # 조회 방법2 : get 함수를 통해 오류 방지, 존재하지 않는 키 값에 대해 None 반환
#
# # 딕셔너리는 for문 대상으로 사용 가능
# # 딕셔너리를 for에 배치하여 사용하면 key만 추출되더 나옴
# dictA = {"1":1000, "2":2000, "3":3000}
# for i in dictA:
#     print(f"{i=}:{dictA[i]=}")

# # 확인문제 2
# pets = [
#     {"name": "구름", "age": 5},
#     {"name": "초코", "age": 3},
#     {"name": "아지", "age": 1},
#     {"name": "호랑이", "age": 1},
# ]
#
# print("# 우리 동네 애완 동물들")
# for pet in pets:
#     print(f"{pet["name"]} {pet["age"]}살")

# # 3
# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}
#
# for number in numbers:
#     if counter.get(str(number)) is None:
#         counter[str(number)] = 0
#     counter[str(number)] += 1
#
# print(counter)
#
# # 4
# character = {
#     "name" : "기사",
#     "level" : 12,
#     "items" : {
#         "sword" : "불꽃의 검",
#         "armor" : "풀플레이트"
#     },
#     "skill" : ["베기", "세게 베기", "아주 세게 베기"]
# }
#
# for key in character:
#     if type(character[key]) is dict:
#         for i in character[key]:
#             print(f"{i} : {character[key][i]}")
#
#     elif type(character[key]) is list:
#         for i in character[key]:
#             print(f"{key} : {i}")
#
#     elif type(character[key]) is str or int:
#         print(f"{key} : {character[key]}")















