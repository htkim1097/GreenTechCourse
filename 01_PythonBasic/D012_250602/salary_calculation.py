# https://docs.google.com/forms/d/e/1FAIpQLScAPNmPQuHG-crpcuOwGHF3m3le5JDC6efL8MrnxM2CxWJMMw/viewform

# 결측치가 있는 부양자 가족수에 따른 간이세액 데이터를 불러와 전처리 후 입력된 연봉에 맞게 연봉을 계산하기

# 콘솔에서 네이버 연봉계산기 처럼 연봉을 입력하면 각 세액 계산 결과와 세후 금액이 나타나도록
# try except 구문, 함수, 반복/분기문, 파일객체 활용, 결측/이상.

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

# 급여 구간, 가족수에 따른 금액만 담은 리스트
total_list = []

# 파일 불러오기
try:
    with open("2025근로소득간이세액표_오류.txt", "r", encoding='UTF8') as file:
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
    print("파일 열기 에러", e)

# 이상치가 있는 데이터 범위만 추출(금액, 400만 이상)
target_list = []
for row in total_list:
    if row[0] >= 4000:  # 400만원 이상일 때
        target_list.append(row[2:]) # 금액만 넣기

# TODO 이상치 찾기(1+4개, 400만원 이상부터 존재)
outlier_lst = []
# max_int = max(target_list)[0]
# std_list = copy.deepcopy(target_list)
#
# for row in std_list:
#     for i, v in enumerate(row):
#         row[i] = v / max_int
#
# outlier_idx = []
# for j, row in enumerate(std_list):
#     #print(f"---------{row}------------")
#     for i, v in enumerate(row):
#         if i < len(row) - 1:
#             # 차이가 너무 크거나 너무 작은 경우를 이상치로 선택(기준 값은 5개 결과가 나오도록 하드코딩한 것)
#             if row[i] - row[i + 1] > 0.149 or row[i] - row[i + 1] < 0.003:
#                 outlier_idx.append([j, i])
# print(outlier_idx)

# 위 아래 값의 차이
row_diffs_lst = []
for i in range(len(target_list))[:-1]:
    row_diffs_lst.append([])
    for j in range(len(target_list[i])):
        row_diffs_lst[i].append(target_list[i+1][j] - target_list[i][j])
    #print(total_list[len(total_list) - len(target_list) + i][0], row_diffs_lst[i])

# 좌우 값의 차이
col_diffs_lst = []
for i in range(len(target_list)):
    col_diffs_lst.append([])
    for j in range(len(target_list[i]))[:-1]:
        col_diffs_lst[i].append(target_list[i][j] - target_list[i][j + 1])
        if target_list[i][j] - target_list[i][j + 1] < 0:
            #print(target_list[i][j] - target_list[i][j + 1])
            outlier_lst.append([len(total_list) - len(target_list) + i, j])
    #print(f"{total_list[len(total_list) - len(target_list) + i][0]} ~ {total_list[len(total_list) - len(target_list) + i][1]}", col_diffs_lst[i])

print(outlier_lst)

# TODO 주위 값과 평균, 규칙성, 커널(3x3)의 관계 등으로 대체값 넣기
for i in range(len(outlier_lst)):
    row = outlier_lst[i][0]
    col = outlier_lst[i][1]

    print(total_list[row][col])





# # 입력 받기
# annual_income = 0
# num_dependents = 0
#
# while True:
#     user_in = input("연봉을 입력하세요(만원)> ")
#     if not user_in.isdigit():
#         print("잘못된 값을 입력하셨습니다.")
#     annual_income = int(user_in)
#     break
#
# while True:
#     user_in = input("부양가족수를 입력하세요(명)> ")
#     if not user_in.isdigit():
#         print("잘못된 값을 입력하셨습니다.")
#     num_dependents = int(user_in)
#     break
#
# # 간이세액 찾기
# simplified_tax = 0
#
# for i in range(len(total_list)):
#     if (total_list[i][0] / 10) <= annual_income/12 < (total_list[i][1] / 10):
#         simplified_tax = total_list[i][num_dependents + 1]
#         #print(total_list[i][num_dependents + 1])
#
# # 연봉 계산
# monthly_income = annual_income * 10000 / 12
# a = int(round(monthly_income * 4.5 / 100, -1))  # 국민연금
# b = int(round(monthly_income * 3.545 / 100, -1))  # 건강보험
# c = int(round(b * 12.95 / 100, -1))  # 요양보험
# d = int(round(monthly_income * 0.9 / 100, -1))  # 고용보험
# e = int(round(simplified_tax, -1))  # 근로소득세(간이세액)
# f = int(round((e / 10) - ((e / 10) % 10), -1))  # 지방소득세
#
# monthly_actual = monthly_income - a - b - c - d - e - f
# annual_actual = monthly_actual * 12
#
# # 계산 결과 출력
# print(f"\n국민연금(4.5%): {a}원")
# print(f"건강보험(3.545%): {b}원")
# print(f"└ 요양보험(12.95%): {c}원")
# print(f"고용보험(0.9%): {d}원")
# print(f"근로 소득세(간이세액): {e}원")
# print(f"└ 지방소득세(10%): {f}원")
# print(f"년 예상 실수령액: {int(round(annual_actual, -2))}원")
# print(f"└ 월 환산금액: {int(round(monthly_actual, -2))}원")



