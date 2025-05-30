# # 314 확인문제
# # 1
# min_person = 2
# max_person = 10
# total = 100
# memo = {}
#
# def m(remain_person, sitted_person):
#     key = str([remain_person, sitted_person])
#
#     # 종료 조건
#     if key in memo:
#         return memo[key]
#
#     if remain_person < 0:
#         return 0
#
#     if remain_person == 0:
#         return 1
#
#     # 재귀 처리
#     count = 0
#     for i in range(sitted_person, max_person + 1):
#         count += m(remain_person - i, i)
#
#     # 메모화
#     memo[key] = count
#
#     # 종료
#     return count
#
# print(m(total, min_person))

# # 함수 고급
# # def 기본 정의 방법
# # 튜플
# # 콜백함수
# # 람다함수
# # with
#
# # 람다 함수: 간단하게 함수 선언하는 방법
# # 튜플은 어떤 함수에서 리턴 오는 값의 형태로 튜플이 많이 사용된다.
# # enumerate([1,2,3,4])를 for의 대상으로 사용하는 경우 => 튜플 반환
# # 다음과 같을 떄 튜플
# dicta={1:100, 2:200}
# print(type(dicta.keys()))
# print(type(dicta.items()))
# for i in dicta.items():
#     print(i)
#
# t=(100,200)
# print(t[0]) # 조회 가능
# # t[0] = 100 # 오류; 수정불가
# # 리스트와 달리 요소를 하나만 사용해서 정의할 때 차이점
# a = [273]
# # b = (273) # 오류
# b = (273, )
# list(b)[0] = 500 # 형변환 가능
# tuple(a)
# 리스트, 튜플, keys 객체, values 객체는 서로 형변환이 가능하다.

# for i, j in 튜플:
# for i in 튜플:
#
# # for 의 변수가 하나 상태로 튜플을 반복하면 튜플형태 그대로 받음
# # 변수가 두개로 튜플을 반복하면 요소를 분리해서 얻음
# for i in enumerate([1,2,3,4]):
#     print(i)
#
# for i, j in enumerate([1,2,3,4]):
#     print(i)
#
#
# # 람다 함수
# # 기존 함수의 선언과 사용
# def test(aa):
#     for _ in range(10):
#         aa()
#
# test([1,2,3])
# test(100)
# test({1:100})
#
# def print_hello():
#     print("안녕하세요")

# 일반적인 함수 호출과 다르게 함수의 식별자만 넣는다.
# 매개변수 aa에 함수를 전달하는 방식. 이러한 함수를 콜백함수라고 한다.
# test(print_hello)

# 함수로 매개변수로 사용하는 대표적인 함수
# 내장함수
# filter, map 함수

# # 323
# # map함수와 filter 함수
# def power(item):
#     return item * item
#
# def under_3(item):
#     return item < 3
#
# list_input_a = [1, 2, 3, 4, 5]
#
# output_a = map(power, list_input_a)
# print("# map() 함수의 실행 결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()
#
# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행 결과")
# print("filter(under_3, list_input_a):", output_b)
# print("filter(under_3, list_input_aO:", list(output_b))
#

# # 람다함수
# power = lambda x: x*x
# under_3 = lambda x: x < 3
#
# list_input_a = [1,2,3,4,5]
#
# output_a = map(power, list_input_a)
# print("# map() 함수의 실행 결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()
#
# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행 결과")
# print("filter(under_3, list_input_a):", output_b)
# print("filter(under_3, list_input_aO:", list(output_b))

# 인라인 람다 함수 : 함수 정의를 식별자에 할당하지 않고 바로 사용하는 것.
# 재사용하지 않을 것 같은 함수에 사용

# 키오스크 실습의 부족한 점
# 정보저장 : 백업 / 로그 저장 / 저장방법: 외부파일(로컬 .ini 파일), 데이터베이스
# GUI : tkinter GUI
# 결제 가짜 : API, 하드웨어
# (구현x)터치 : 터치패널, 하드웨어
# 통신 : TCP socket

# 텍스트 파일
# 파일 열기
# open(문자열:파일경로, 문자열:모드)
# 모드: w(새 문서, 기존 파일을 덮어씀)/a(내용추가, 뒤에 이어서 입력 됨 )/r(읽기)
# 상대 경로 : 현재 실행되는 프로세스를 기준으로 한 위치
# 절대 경로 : 모든 경로

# 파일 닫기 : 파일객체.close()

# 파일에 입력 : write() 함수 사용
# 327
# file = open("basic.txt", "w")
# file.write("Hello Python Programming")
# file.close()

# 파일 객체 주의 사항 : 파일객체를 오픈해서 작업을 마치면 무조건 닫아야함.

# # with 문으로 파일의 close를 보장. close 작성 x.
# with open("test.txt", "w") as f:
#     f.write("123456")
#
# # 파일 읽기
# with open("test.txt", "r") as f:
#     print(f.read())
#
# # 내용 추가
# with open("test.txt", "a") as f:
#     f.write("3333333333")

# 데이터를 구조적으로 표현하는 방법: csv, xml, json
# csv : 콤마 분리 엑셀
# xml : 확장 마크업 랭귀지
# json : 자바스크립트 오브젝트 데이터, 웹 통신에서의 표준 데이터 규격


# 메타데이터 : 파일 내용이 아닌 파일에 대한 정보 데이터.(수정된 날짜, 위치, 등)

import random

hanguls = list("가나다라마바사아자차카파타하")

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))








