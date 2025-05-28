# [계룡건설 빅데이터 기반 Green Tech SW개발자 10기]
# OT
- KDT 학습 ~~ 이메일로 받으면 2주 내 제출.
- 2차 특강(8월 말) 빠지지 않기.
- 수업 후 야간자습은 금욜 제외 21시까지.
- 수업 개요  
    1. 파이썬 문법
    2. 자바 문법
    3. GUI 소프트웨어(파)
    4. 통신(파)
    5. 웹서버; 백엔드(자)
    6. 웹표면; 프론트엔드(자스)
    7. 데이터 분석(수집/정제/추출)(파,자)
    8. 데이터 딥러닝, 머신러닝
    9. 포트폴리오 2개(중간, 최종)
- 수업 교제(총 8권)
    - 환경 관련(2권)
    - 개발 관련(6권)  
        1. 파이썬
        2. 자바
        3. 머신러닝/딥러닝
        4. SQL
        5. Spring Boot
        6. 데이터분석

<br></br>

# 파이썬
## Ch 1 파이썬 시작하기
### 개발 환경 설정  
- Python 3.13.3  
- Pycharm

### Sec 3 이 책에서 자주 나오는 용어들
- 문장: 실행 가능한 코드 최소 단위  
- 프로그램: 문장들이 모여 프로그램을 구성  
- 표현식: 어떠한 값을 만들어 내는 간단한 코드  
- 연산자: + - 등 사칙연산 외 연산자  
- 키워드: 파이썬에서 고정적인 기능을 담당하고 있는 단어  

- 식별자: 이름을 붙일 때 사용하는 단어, 주로 변수나 함수명
- 식별자 생성 규칙: 
    1) 키워드 사용금지
    2) 특수문자는 언더바만 허용
    3) 숫자로 시작 불가
    4) 공백 포함 불가
    5) 한글 금지
- 식별자 작성 스타일: 캐멀/스네이크 케이스
    식별자가 2단어 이상으로 되어 있을 때
    - 스네이크 케이스: 단어 사이에 언더바로 구분해서 작성
    - 캐멀 케이스: 각 단어의 첫 글자만 대문자로 작성

- 주석: #을 가장 앞에 넣고 작성한 문장은 파이썬 인터프리터가 무시한다
- 자료: 리터럴(literal)이라고 표현, 값 자체

- print()는 파이썬의 가장 기본적인 출력 방법
- 함수: 하난의 단위 기능 묶음
- 함수는 ()괄호가 있다
- 함수의 () 안에 들어가는 것: 함수 실행의 대상물
- print()는 줄바꿈의 효과가 있다
- 문자데이터 " "에 묶인 데이터는 문자열로 취급

```python
# 하나만 출력합니다.
print("# 하나만 출력합니다.")
print("Hello Python Programming...!")
print()

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)   # 프린트 함수 사용 => 여러 개를 출력하려면 쉼표로 구분한다.
print("안녕하세요", "저의", "이름은", "윤인성입니다!")  # 쉼표로 구분 된 요소는 띄어쓰기로 출력한다.
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("---확인 출력선---")
print()
print()
print("---확인 출력선---")

print(type("안녕하세요"))
print(type(12345))
print(type(3.14))
print(type(False))
```

- 결과 창에 [ 종료 코드 0 ]의 의미: 문제가 없이 실행 됨

<br></br>

## Ch 2 자료형
### Sec 1 자료형과 문자열
#### 자료형
- 자료형: 데이터의 타입
- 파이썬의 기본 자료형
    1. 문자열(string): "안녕", "Hello World" ...
    2. 숫자(number): 1, 2, 3, -100, 5000000, 3.141592 ...
        1) 정수 int : 100
        2) 실수 float : 3.14
    3. 불(boolean): True, False

```python
print(type("안녕하세요"))    # str 형태
print(type(12345))          # int 형태
print(type(3.14))           # float 형태
print(type(False))          # bool 형태

# 함수의 중첩 구조에서는 가장 안쪽 (완전한)구조부터 찾아서 해석하기
```
<br></br>

#### 문자열
- 문자열 데이터 형태: 따옴표로 감싸 생성
- 따옴표: 작은 따옴표, 큰 따옴표 다 가능하다, 짝을 맞춰야 한다
```python
"안녕하세요"
# "안녕하세요'  #오류
```

- 문자열 내 문자열 형태의 (인용) 따옴표 출력 하려면
- 문자열 데이터 타입임을 나타내는 따옴표와 다른 따옴표를 사용해야 한다.
```python
print("안녕하세요'안녕하세요'")
```

- 이스케이프 문자(코드)
- 이스케이프 문자는 역슬래시(백슬래시)기호와 조합하여 사용하는 특수문자를 의미
    - \"는 큰 따옴표
    - \'는 작은 따옴표
    - \t는 탭 기능(띄어쓰기 4칸)
    - \n는 줄 바꿈 기능
```python
print("\"안녕하세요\"라고 말했습니다.")
```

- 따옴표 3쌍: 자유 포멧 문자열 가능
```python
print("""123
45
6""")
```
<br></br>

#### 문자열의 더하기 + 연산
- 문자열의 더하기 연산은 문자열과 문자열을 더하는 기능: 문자열의 연결 효과
```python
print("안녕" + "하세요")     # 문자열 + 문자열 연산은 가능
print("안녕하세요" + "!")    
print("안녕하세요" + 1)      # 오류) 문자열 + 숫자(정수) 연산은 불가능
```
- 신텍스 에러: 문법오류, 파이참에서 빨간 줄로 안내 해준다.
- 타입 에러: 형태오류, 빨간줄이 뜨지 않는다.
<br></br>

#### 문자열의 * 곱 연산자
- 문자열을 숫자와 * 연산자로 곱하면 문자열을 반복하는 효과
```python
print("안녕하세요"*10)
print(10*"안녕하세요")
```
<br></br>

#### 인덱싱 []
- 문자 선택 연산자
- 문자열에서 일부 문자만 선택하는 방법
- 프로그래밍 언어의 인덱스 유형 
  1. 제로 인덱스(0부터 카운트)
  2. 원 인덱스(1부터 카운트)
- 파이썬은 제로 인덱스 방식으로, 시작 숫자가 0이다
```python
print("안녕하세요"[0])
print("안녕하세요"[5]) # 오류; 문자열 인덱싱에서 범위 밖 인덱스 번호를 추출하면 indexerror 발생
print("안녕하세요"[-1])  # -부호는 뒤에서 부터를 의미
```
<br></br>

#### 슬라이싱 [:]
- 슬라이싱 사용법 [어디서부터 : 어디까지]
```python
print("안녕하세요"[0:2])     # 0부터 2까지 슬라이싱
```
- 어디까지를 의미하는 ':' 뒤 숫자는 미만
- 어디부터를 의미하는 ':' 앞 숫자는 이상
- [a:b]는 a <= x < b
```python
print("안녕하세요"[0:-1])    # 안녕하세
print("안녕하세요"[-3:-1])   # 하세
print("안녕하세요"[:])       # 안녕하세요
print("안녕하세요"[:])       # 안녕하세요
print("안녕하세요"[:3])      # 안녕하
print("안녕하세요"[2:])      # 하세요
```
<br></br>

#### 문자열 길이
- len() 함수 사용
- len() 함수를 통해 문자열 길이를 얻고, 얻은 길이 값을 기반으로 인덱싱이나 슬라이싱을 하면 indexerror를 피할 수 있다.

```python
print(len("fjdosfjidsjfklewfjlekwjfidsjfjdsifjs"))
```
<br></br>

### Sec 2 숫자
#### 숫자 연산자
- 더하기 +
- 빼기 -
- 곱하기 *
- 나누기 /
```python
print(100 + 100)
print(100 - 100)
print(100 * 100)
print(100 / 100)    # 나누기는 실수형태로 나온다
```

- 정수 나누기(몫) 연산자
```python
print(100 // 100)     # 1
print(100 // 3)       # 99
# 정수 형태의 나누기 결과 값을 얻음
# 몫을 구하는 연산자이기도 함, 소수점 버린 결과
```

- 나머지 연산자
```python
print(100 % 3)      # 1
```

- 제곱 연산자
```python
print(100 ** 2)     # 10000
```
<br></br>

#### 연산자의 우선순위
- +, - 보다 *, / 가 우선
- () 괄호로 묶이면 우선
- 동일한 우선순위 끼리는 앞에를 먼저 처리
-  \+ 연산은 같은 데이터 형태끼리 가능
<br></br>

### Sec 3 변수와 입력
#### 변수
- 변수 선언 : 변수 생성
- 변수 할당 : 값 대입
- 변수 참조 : 값 조회
```python
pi = 3.14159265     # pi라는 식별자를 가진 변수를 생성하고 3.14159265라는 실수를 할당(대입)
print(pi * 100)     # 변수명을 통한 값의 참조(조회)
```
```python
# 변수 선언과 할당
pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2 * pi * r)
print("원의 넓이 =", pi * r * r)
```

#### 복합 대입 연산자
- 복합 대입 연산자는 원래 데이터 형태에서 사용 가능한 연산자에 대입을 하나로 합쳐 놓은 것
- 숫자 연산 후 대입
- +=, -=, *=, /=, %=, **= 
```python
number = 100 # number 변수 생성, 100 값을 number 변수에 할당
number += 10 # 복합 대입 연산자
# number = number + 10과 동일
print(number)

aa = 10
aa *= 10    # aa = aa * 10
print(aa)
```
<br></br>
- 문자열 대상 복합 대입 연산
- +=, *=
- *=는 문자열 *= 숫자 로만 사용
```python
# 문자열의 더하기 연산은 => 문자열 + 문자열 형태로 가능
string_a = '안녕하세요'
string_a += "!!!"
print(string_a)
```
<br></br>

-----
#### 사용자 입력: input()
- input() : 사용자의 입력을 받는다.
- 사용자로부터 데이터를 입력 받을 때, input()을 통해 프롬프트를 입력 받는다.
- prompt : 컴퓨터에서 다이얼로그(대화상자) 시스템이나 셸(터미널)을 통해 입력하는 메세지 형태.
```python
input("인풋")     # 사용자의 입력을 대기; 대기한다는 것은 프로세스가 죽지 않은 상태
```
- 종료 코드 0: 정상 종료, 더 이상 읽을 라인이 없을 때, 프로세스 완료
- 종료 코드 1: 비정상 종료, error 분석 필요
<br></br>

- 입력 시 출력 문자를 설정할 수 있다. 
```python
string = input("인사말을 입력하세요")
```
<br></br>
- input() 함수의 입력 자료형
```python
string = input("입력하세요")
print(type(string))     # string 변수에 저장된 값의 데이터 형태를 확인
```
- input 함수에 프롬프트를 통해 입력된 값은 문자열 형태로 저장된다.
```python
# 예제1
# 입력을 받습니다.
string = input("입력> ")

# 출력합니다.
print("자료: ", string)
print("자료형: ", type(string))

# 예제2
# 입력을 받습니다.
string = input("입력> ")

# 출력합니다.
print("입력 + 100: ", string + 100)   # 오류 발생
```
<br></br>

-----
#### 문자열을 숫자로 바꾸기
- 캐스트(cast) : 형 변환, 자료형의 변환
- input()으로 입력 받은 데이터는 문자열로 저장되기에 상황에 따라 숫자로 변환 할 필요가 있다.
- int(), float(), str()
```python

string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력> ")
int_b = int(string_b)

print("문자열 자료: ", string_a + string_b)
print("숫자 자료: ", int_a + int_b)
```
```python
output_a = int("53")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)
```
```python
input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))

print("덧셈결과:", input_a + input_b)
print("뺄셈결과:", input_a - input_b)
print("곱셈결과:", input_a * input_b)
print("나눗셈결과:", input_a / input_b)
```
- 문자를 숫자로 변환 : int(), float()
- 숫자를 문자로 변환 : str()
```python
# 숫자를 입력받습니다.
raw_input = input("inch 단위의 숫자를 입력해주세요: ")

# 입력 받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
inch = int(raw_input)
cm = inch * 2.54

# 출력합니다.
print(inch, "inch는 cm 단위로 ", cm, "cm입니다.")
```
- 지금까지 내용 종합 예제
```python
# input 사용자 입력을 통해 사용자의 신장과 체중을 입력 받고 사용자의 BMI 지수를 출력하는 코드 작성
# BMI 계산 공식 : 체중(kg) / 신장(m)의 제곱
# input을 통해 신장 입력 시 cm 단위로 입력하고 계산은 m단위로 변환하여 수행

height_cm = input("신장을 입력하세요(cm): ")
weight_kg = input("체중을 입력하세요(kg): ")

height_m = float(height_cm) / 100

print(f"체중 {weight_kg} 신장 {height_cm} BMI는 {float(weight_kg) / height_m ** 2}입니다.")
```

- 확인문제
```python
str_a = input("문자열 입력> ")
str_b = input("문자열 입력> ")

print(str_a, str_b)

str_tmp = str_a
str_a = str_b
str_b = str_tmp

print(str_a, str_b)
```

```python
str_input = input("원의 반지름 입력> ")
num_input = int(str_input)
print()

print("반지름: ", num_input)
print("둘레: ", 2 * 3.14 * num_input)
print("넓이: ", 3.14 * num_input ** 2)
```
<br></br>

-----
### Sec 4 숫자와 문자열의 다양한 기능
#### 문자열의 format() 함수
- format() 함수는 문자열 전용 함수
- 데이터.함수() 형태의 함수들은 앞에 놓인 데이터 타입에 적용할 수 있는 함수
```python
"{}".format(100)    # {} 중괄호 안에 100을 넣겠다는 의미
print("{}.format(100)")
```
```python
# format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

# 출력하기
print(format_a)
print(format_b)
print(format_c)
print(format_d)
```
- {:[+,-][0]n.m[d,f]} : n은 소수점 앞 자릿수, m은 소수점 뒤 자릿수, 0은 소수점 앞 빈 칸을 0으로 채울지, d와 f는 정수와 실수 표현
- 소수점 뒤 자릿수를 지정하면 자동 반올림 처리 됨.
- {:g}는 의미 없는 0을 제거.
<br></br>

#### 문자열 함수들
- 비파괴적 함수 : 원본 데이터를 변형시키지 않는다. 
```python
a = "Hello World"

# 대소문자로 변환
a.upper()
a.lower()

# 공백 제거
a.strip()
a.lstrip()  # 좌측 공백 제거
a.rstrip()  # 우측 공백 제거

# find/rfind()
# find() 왼쪽부터 찾아서 처음 등장하는 위치를 찾는다.
# rfind() 오른쪽부터 찾아서 처음 등장하는 위치를 찾는다.
aa = "안녕하세요".find("녕")

contents = "1234qwer"
ct = contents[contents.find("4"):]

print(f"{contents=}, {ct=}")

# in 연산자
print("안녕" in "안녕하세요")

# split()
aaa = "10 20 30 40 50".split(" ")
print(aaa)
```

- 확인 문제(p152 ~ 153)
```python
pi = 3.141592
r = float(input("구의 반지름을 입력해주세요: "))
print(f"구의 부피는 {4/3 * pi * (r ** 3)}")
print(f"구의 겉넓이는 {4 * pi * (r ** 2)}")
```
```python
w = float(input("밑변의 길이를 입력해주세요: "))
h = float(input("높이의 길이를 입력해주세요: "))
print(f"빗변의 길이는 {((h ** 2) + (w ** 2)) ** (1/2)}")
```

## Ch 3 조건문
### Sec 1 불 자료형과 if 조건문
#### Bool 자료형
```python
print(True)
print(False)
```
<br></br>

#### 비교 연산자
- == : 같다
- != : 다르다
- <, > : 크다, 작다
- <=, >= : 크거나 같다, 작거나 같다
```python
print(10 == 10)     # True
print(10 < 10)      # False
print(10 <= 10)     # True
print(10 != 10)     # False
```
- 영어는 아스키 코드로 표현
- 한글은 유니코드로 표현
- 인코딩 : 번역, 해석 방식
<br></br>
- 범위 비교
```python
x = 12
print(10 < x < 20)
```

#### 논리 연산자
- and
- or
- not
```python
# not
print(not True)
print(not False)
```
```python
x = 10
under_20 = x < 20
print(f"{under_20=}")
print(f"{not under_20=}")
```

```python
# and
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# or 
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False
```
<br></br>

#### if 조건문
- 조건 분기
- 조건이 참일 경우와 거짓일 경우로 나뉨
- if 조건식:  
    실행할 문장
- 들여쓰기 된 문장만 포함
```python
if 10 < 20:
    print("10이 작다.")
print("111")
```

```python
# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 양수 조건
if number > 0:
    print("양수입니다.")

if number < 0:
    print("음수입니다.")

if number == 0:
    print("0입니다.")
```

- if 문에 0과 ""(빈 문자열)은 False를 의미
```python
print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다.")
else:
    print("0은 False로 변환됩니다.")
    print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다.")
else:
    print("빈 문자열은 False로 변환됩니다.")
```

## Ch 4 반복문
### Sec 1
- 리스트
- 딕셔너리
- for
- while

-----
- 이터레이터 객체의 특징 : 반복 순회 1번만 가능하다.
```python
numbers = [1,2,3,4,5]
r_num = reversed(numbers)
print(r_num)
```
- next() : 이터레이터에서 값을 하나씩 뽑는다. 
- 범위를 넘어 값을 뽑을 시 에러 발생.
```python
numbers = [1,2,3,4,5]
r_num = reversed(numbers)

print(next(r_num))      # 5
print(next(r_num))      # 4
print(next(r_num))      # 3
print(next(r_num))      # 2
print(next(r_num))      # 1
print(next(r_num))      # stopIteration Error 발생. 
```

## Ch 5 함수
### Sec 1 함수 만들기
#### 함수의 선언 방법
- 함수 정의 키워드 def와 매개변수를 정의하는 ()소괄호
- 들여쓰기로 함수 내 실행문 구분
```
# 함수의 선언부(정의부)
def 식별자 ():
    실행문

# 함수의 사용(호출)
식별자()
```
- 사용자 정의 함수, 내장(built-in) 함수

```python
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()
```
#### 매개변수가 있는 함수 만들기
- 함수 정의부 소괄호 안에 매개변수를 정의한다.
- 매개변수가 선언되어 있는 함수를 호출시 꼭 인자 필요

```python
# 매개변수가 있는 함수 1개의 사용 위치
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("HI", 100)
print_n_times()     # 에러 발생
```

- 전역변수, 지역변수
```python
name = "kim"    # 전역변수

def myFunction(name):   # 매개변수는 지역적. 위에 name과 다름.
    print(name)
# 오류는 나오지 않지만 이름을 중복으로 정하지 말아야 한다.
```

- 리턴 여부 확인
```python
lst = [1,2,3]
res = type(lst)         # 리턴 유무 : 있음 / 행위 유무 : O
print(res)
res = lst.append(4)     # 리턴 유무 : 없음 / 행위 유무 : O
print(res)
```

- print()는 함수 내 작성 x. 반드시 지켜야 할 필요는 없지만 결과만 반환하고 따로 print하는 것이 더 좋음.
- return : 함수의 결과 반환. 함수를 호출한 자리에 반환 값이 할당.
```python
def plus(a,b):
    print(a+b)
# 보다
def plus2(a,b):
    return a+b
```

```python
def 
```
- sum함수 대상으로 딕셔너리를 넣으면 키값들의 합계를 구해준다.
- 사용자 정의함수를 생성합니다.
- 사용자 정의함수의 이름은 mySum 이다.
- mySum함수는 딕셔너리를 매개변수로 전달받아야 한다.
- mySum 함수는 해당 딕셔너리에 있는 값(value)들의 합을 구해서 return 해주는 함수입니다.
```python
def mySum(dic_a: dict):
    sum = 0
    for _, v in dic_a.items():
        sum += v
    return sum

print(mySum({1:100, 2:200}))

def mySum2(d):
    return sum(d.values())

print(mySum2({1:100, 2:200}))
```
- 대부분의 기능이 내장 함수로 있지만, 특수한 기능 등은 따로 구현하여 필요시 사용한다.

#### 가변 매개변수
- 기본적인 함수에서는 함수 선언시 매개변수 호출시 정의한 개수대로 들어가야 한다.
- 가변 매개변수 뒤에는 일반 매개변수가 올 수 없고, 가변 매개변수는 함수의 정의에 단 1개만 사용 가능하다.
- `*` + `변수명`으로 표기되는 매개변수. 

```python
def print_n_times(n, *values):  # values는 tuple이다.

    for i in range(n):
        for value in values:
            print(value)

        print()

# 함수를 호출합니다.
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
```

#### 기본 매개변수
- 일반 매개변수(n), 가변 매개변수(*n), 기본 매개변수(n=10) 순으로 배치.
- 기본 매개변수에 값을 넣지 않으면 기본값이 자동으로 들어간다.

```python
def m_func(n=10):
    print(n)
```

#### 키워드 매개변수
- 기본 매개변수와 가변 매개변수를 같이 사용할 때, 의도치 않은 결과가 생길 수 있다.
- 매개변수의 이름을 직접 지정하는 것이 키워드 매개변수.
- 키워드 매개변수로 작성 시 순서는 상관없다.
```
def test(x, *y, z=100):
    print(x)
    print(y)
    print(z)

print(100, 200, 300, 400, 500, z=600)       # z는 키워드 매개변수
```

#### return
- 함수의 결과를 반환할 때 사용한다.
- return하면 함수를 탈출하기 때문에 더이상 함수에 문장을 실행 할 수 없다.
- return은 탈출용으로도 사용할 수 있다.
```python
# 어떤 값을 받았을 때 정해진 자료형만 받고자 할 경우
def m_func(lst):
    for i in lst:
        if type(i) is int:
            pass
        else:
            return  # 예외, 오류를 피하기 위해 쓰는 경우(단순 탈출)
    return sum(lst)

print(m_func([1,2,3,4,5]))
print(m_func([1,2,3,4,5,"6"]))
```

- 매개변수가 있거나 없거나
- 리턴이 있거나 없거나
- 공요함수 / 전용함수
- 파괴 / 비파괴

#### 기본적인 함수의 활용

```python
# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print(f"{sum_all(0, 100)=}")
print(f"{sum_all(0, 1000)=}")
print(f"{sum_all(50, 100)=}")
print(f"{sum_all(500, 1000)=}")
```

```python
# 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

print(f"{sum_all(0, 100, 10)=}")
print(f"{sum_all(end=100)=}")
print(f"{sum_all(end=100, step=2)=}")
```

## 소프트웨어 개발 문서
### 플로우차트
프로그래밍의 기초. 설계도와 같은 느낌.
플로우차트의 흐름은 코딩(논리의 흐름)의 순서와 같다.
- draw.io

### 와이어 프레임
화면 레이아웃의 이동 흐름도.
- figma(layout, 와이어프레임)

### 클래스 다이어그램
객체 간의 관계도.

### ERD
데이터 베이스의 Entity 간의 관계도.

### 요구사항명세서
기능별로 요구사항을 명세한 것. 
소프트웨어 개발 첫 번째에 작성.
- 기능
- 어디서 사용
- 

### 아키텍처 설계도
CI/CD Workflow. 
Spring,docker,tomcat 등 프로젝트에 사용되는 기술들의 구조.




