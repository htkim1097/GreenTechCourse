# https://docs.google.com/forms/d/e/1FAIpQLScAPNmPQuHG-crpcuOwGHF3m3le5JDC6efL8MrnxM2CxWJMMw/viewform

# 정답
# 1) 428 ~ 430, 11 : 32650 -> 32000
# 2) 406 ~ 408, 2 : 175910 -> 173910
# 3) 498 ~ 500, 1 : 332660 -> 0
# 4) 690 ~ 692, 1 : 710020 -> -
# 5) 998 ~ 1000, 11 : 958650 -> 958000

"""
2025근로소득간이세액표 파일에는
결측치(1개)와 이상치(4개)가 존재한다.

결측치와 이상치는 400만원 이상 구간에만 존재한다.

파이참 콘솔에서 네이버 연봉계산기와 같이
세전 연봉 금액을 사용자 입력을 통해 입력받고,

1.국민연금 (4.5%)
2.건강보험 (3.545%)
2.1---요양보험 (12.95%)
3고용보험 (0.9%)
4근로소득세 (간이세액)
4.1---지방소득세(10%)
5.연간 예상 수령액
6.월 환산금액(세후)

를 출력한다.
"""

import copy
import os

def cutting_number(num:int, num_digit=2) -> int:
    """
    정수(num)와 자릿수(num_digit)를 받아 자릿수 이하의 수를 0으로 대체한다.
    """
    return num - (num % (10 * (num_digit - 1)))

# 파일 경로 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, '2025근로소득간이세액표_오류.txt')

# 급여 구간, 가족수에 따른 금액만 담은 리스트
total_list = []

# 파일 불러오기
try:
    with open(file_path, "r", encoding='UTF8') as file:
        # 데이터를 2차원 리스트로 만들기
        for i, line in enumerate(list(file)):
            lst = []

            if i <= 3:
                continue

            splitted_line = line.split("\t")

            # 결측치 제거
            for j in splitted_line:
                j = j.strip()

                if ',' in j:
                    j = j.replace(',', '')

                if j == '-' or (not j.isdigit()):
                    j = 0
                else:
                    j = int(j)
                lst.append(j)

            total_list.append(lst)
except Exception as e:
    print("파일 열기 에러: ", e)

# 이상치가 있는 데이터 범위만 추출(금액, 400만 이상)
target_list = []
for row in total_list:
    if row[0] >= 4000:  # 400만원 이상일 때
        target_list.append(row[2:]) # 금액만 넣기

# TODO 이상치 찾기(1+4개, 400만원 이상부터 존재)
outlier_lst = []

# 좌우 값의 차이 계산
col_diffs_lst = []
for i in range(len(target_list)):
    col_diffs_lst.append([])
    for j in range(len(target_list[i]))[:-1]:
        col_diffs_lst[i].append(target_list[i][j] - target_list[i][j + 1])
        if target_list[i][j] - target_list[i][j + 1] < 0:
            outlier_lst.append([i, j])

# 이상치 출력
# print(outlier_lst)

# 대체값 넣기
for i in range(len(outlier_lst)):
    row = outlier_lst[i][0]
    col = outlier_lst[i][1]
    sum = 0
    cnt = 0
    pred_val = 0

    # 위, 아래 값이 모두 있다면 두 값의 평균으로 대체값 예측.
    if row - 1 >= 0 and row + 1 < len(target_list):
        pred_val = round(int((target_list[row - 1][col] + target_list[row + 1][col]) / 2), -1)

    # 커널의 평균으로 대체값 예측.
    else:
        # 현재 데이터 주변 8개 데이터를 담은 2중 리스트 만들기
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                r = row + i - 1
                c = col + j - 1

                try:
                    if r < 0 or c < 0:
                        raise IndexError
                    sum += target_list[r][c]
                except:
                    pass
                else:
                    cnt += 1
        pred_val = round(int(sum / cnt), -1)

    
    # 원래 데이터에 대체값 추가
    origin_row = len(total_list) - len(target_list) + row
    origin_col = col + 2
    print(f"{total_list[origin_row][0]} ~ {total_list[origin_row][1]}, {origin_col - 1}인: ", end="")
    print(total_list[origin_row][origin_col], end="")
    total_list[len(total_list) - len(target_list) + row][col + 2] = pred_val
    print(" ->", pred_val)

annual_salary = 0   # 연봉
num_dependents = 0  # 부양가족수

while True:
    user_in = input("연봉을 입력하세요(만원)> ")
    if not user_in.isdigit():
        print("잘못된 값을 입력하셨습니다.")
    annual_salary = int(user_in)
    break

while True:
    user_in = input("부양가족수를 입력하세요(명)> ")
    if not user_in.isdigit():
        print("잘못된 값을 입력하셨습니다.")
    num_dependents = int(user_in)
    break

simplified_tax = 0  # 간이세액
salary = annual_salary * 10000 / 12     # 월급

# 간이세액 찾기
for i in range(len(total_list)):
    if (total_list[i][0] / 10) <= salary / 10000 < (total_list[i][1] / 10):
        simplified_tax = total_list[i][num_dependents + 1]

# 국민연금 기준소득월액 상/하한액
pension_upper_limit = 6170000
pension_lower_limit = 390000

# 국민연금 금액 계산
a = 0
if salary > pension_upper_limit:
    a = int(pension_upper_limit * 0.045)
elif pension_lower_limit < salary:
    a = int(pension_lower_limit * 0.045)
else:
    a = int(salary * 0.045)

a = cutting_number(a)

# 건강보험 금액 계산
b = cutting_number(int(salary * 0.03545))

# 요양보험 금액 계산
c = cutting_number(int(b * 0.1295))

# 고용보험 금액 계산
d = cutting_number(int(salary * 0.009))

# 근로소득세(간이세액) 금액 계산
e = cutting_number(int(simplified_tax))

# 지방소득세 금액 계산
f = cutting_number(int(e * 0.1))

actual_salary = salary - a - b - c - d - e - f
actual_annual_salary = actual_salary * 12

# 계산 결과 출력
print(f"\n국민연금(4.5%): {a}원")
print(f"건강보험(3.545%): {b}원")
print(f"└ 요양보험(12.95%): {c}원")
print(f"고용보험(0.9%): {d}원")
print(f"근로 소득세(간이세액): {e}원")
print(f"└ 지방소득세(10%): {f}원")
print(f"년 예상 실수령액: {int(actual_annual_salary)}원")
print(f"└ 월 환산금액: {int(actual_salary)}원")