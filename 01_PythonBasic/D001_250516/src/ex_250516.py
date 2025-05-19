#
# # 하나만 출력합니다.
# print("# 하나만 출력합니다.")
# print("Hello Python Programming...!")
# print()
#
# # 여러 개를 출력합니다.
# print("# 여러 개를 출력합니다.")
# print(10, 20, 30, 40, 50)   # 프린트 함수 사용 => 여러 개를 출력하려면 쉼표로 구분한다.
# print("안녕하세요", "저의", "이름은", "윤인성입니다!")  # 쉼표로 구분 된 요소는 띄어쓰기로 출력한다.
# print()
#
# # 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
# print("# 아무것도 출력하지 않습니다.")
# print("---확인 출력선---")
# print()
# print()
# print("---확인 출력선---")
#
# print(type("안녕하세요"))
# print(type(12345))
# print(type(3.14))
# print(type(False))
#
# print(type("안녕하세요"))    # str 형태
# print(type(12345))          # int 형태
# print(type(3.14))           # float 형태
# print(type(False))          # bool 형태
#
# "안녕하세요"
# # "안녕하세요'  #오류
#
# print("안녕하세요'안녕하세요'")
#
# print("\"안녕하세요\"라고 말했습니다.")
#
# print("""123
# 45
# 6""")
#
# print("안녕" + "하세요")     # 문자열 + 문자열 연산은 가능
# print("안녕하세요" + "!")
# print("안녕하세요" + 1)      # 오류) 문자열 + 숫자(정수) 연산은 불가능
#
# print("안녕하세요"*10)
# print(10*"안녕하세요")
#
# print("안녕하세요"[0])
# print("안녕하세요"[-1])
#
# print("안녕하세요"[0:-1])    # 안녕하세
# print("안녕하세요"[-3:-1])   # 하세
# print("안녕하세요"[:])       # 안녕하세요
# print("안녕하세요"[:])       # 안녕하세요
# print("안녕하세요"[:3])       # 안녕하
# print("안녕하세요"[2:])      # 하세요
#
# print(len("fjdosfjidsjfklewfjlekwjfidsjfjdsifjs"))
#
# print(2 + 2 - 2 * 2 / 2 * 2)
#
# print(15/4 )

# 변수 선언과 할당
pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2 * pi * r)
print("원의 넓이 =", pi * r * r)
