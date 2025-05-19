#
#
# number = 100 # number 변수 생성, 100 값을 number 변수에 할당
# number += 10 # 복합 대입 연산자
# print(number)
#
# aa = 10
# print(aa)
# aa *= 10    # aa = aa * 10
# print(aa)
# aa = aa * 10
# print(aa)
#
#
#
# # 문자열의 더하기 연산은 => 문자열 + 문자열 형태로 가능
# string_a = '안녕하세요'
# string_a += "!!!"
# print(string_a)
#
#
#
# input()
#
# string = input("인사말을 입력하세요")
# print(string)
#
# string = input("입력하세요")
# print(type(string))     # string 변수에 저장된 값의 데이터 형태를 확인
from operator import itemgetter

# # 예제1
# # 입력을 받습니다.
# string = input("입력> ")
#
# # 출력합니다.
# print("자료: ", string)
# print("자료형: ", type(string))
#
# # 예제2
# # 입력을 받습니다.
# string = input("입력> ")
#
# # 출력합니다.
# print("입력 + 100: ", string + 100)   # 오류 발생
#
# string_a = input("입력A> ")
# int_a = int(string_a)
#
# string_b = input("입력> ")
# int_b = int(string_b)
#
# print("문자열 자료: ", string_a + string_b)
# print("숫자 자료: ", int_a + int_b)
#
# output_a = int("53")
# output_b = float("52.273")
#
# print(type(output_a), output_a)
# print(type(output_b), output_b)
#
# input_a = float(input("첫 번째 숫자> "))
# input_b = float(input("두 번째 숫자> "))
#
# print("덧셈결과:", input_a + input_b)
# print("뺄셈결과:", input_a - input_b)
# print("곱셈결과:", input_a * input_b)
# print("나눗셈결과:", input_a / input_b)
#
#
# # 숫자를 입력받습니다.
# raw_input = input("inch 단위의 숫자를 입력해주세요: ")
#
# # 입력 받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
# inch = int(raw_input)
# cm = inch * 2.54
#
# # 출력합니다.
# print(inch, "inch는 cm 단위로 ", cm, "cm입니다.")

# input 사용자 입력을 통해 사용자의 신장과 체중을 입력 받고 사용자의 BMI 지수를 출력하는 코드 작성
# BMI 계산 공식 : 체중(kg) / 신장(m)의 제곱
# input을 통해 신장 입력 시 cm 단위로 입력하고 계산은 m단위로 변환하여 수행
#
# height_cm = input("신장을 입력하세요(cm): ")
# weight_kg = input("체중을 입력하세요(kg): ")
#
# height_m = float(height_cm) / 100
#
# print(f"체중 {weight_kg} 신장 {height_cm} BMI는 {float(weight_kg) / height_m ** 2}입니다.")

# str_a = input("문자열 입력> ")
# str_b = input("문자열 입력> ")
#
# print(str_a, str_b)
#
# str_tmp = str_a
# str_a = str_b
# str_b = str_tmp
#
# print(str_a, str_b)
#
# str_input = input("원의 반지름 입력> ")
# num_input = int(str_input)
# print()
#
# print("반지름: ", num_input)
# print("둘레: ", 2 * 3.14 * num_input)
# print("넓이: ", 3.14 * num_input ** 2)

# # format() 함수로 숫자를 문자열로 변환하기
# format_a = "{}만 원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
# format_c = "{} {} {}".format(3000, 4000, 5000)
# format_d = "{} {} {}".format(1, "문자열", True)
#
# # 출력하기
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)
#
# contents = "1234qwer"
# ct = contents[contents.find("4"):]
#
# print(f"{contents=}, {ct=}")

# pi = 3.141592
# r = float(input("구의 반지름을 입력해주세요: "))
# print(f"구의 부피는 {4/3 * pi * (r ** 3)}")
# print(f"구의 겉넓이는 {4 * pi * (r ** 2)}")
#
# w = float(input("밑변의 길이를 입력해주세요: "))
# h = float(input("높이의 길이를 입력해주세요: "))
# print(f"빗변의 길이는 {((h ** 2) + (w ** 2)) ** (1/2)}")















