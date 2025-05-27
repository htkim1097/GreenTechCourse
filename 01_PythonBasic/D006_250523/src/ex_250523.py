# p266
# # 2
# output = [i for i in range(1, 101) if str(bin(i)).count("0") == 2]
#
# for i in output:
#     print("{} : {}".format(i, "{:b}".format(i)))
# print("합계:", sum(output))

# p268
# # 1
# lst = [1,2,3,4,5,6,2,3,4,1,2,4,6,3,2,6,3,1,3]
# d = {}
#
# for i in lst:
#     if d.get(str(i)) is None:
#         d[str(i)] = 1
#     else:
#         d[str(i)] += 1
#
# print(f"사용된 숫자의 종류는 {len(d)}개입니다.")

# 2
# str = "ctagcagtgctagcagtcgatgcagaggatatgcgcatagtactagcagcatgtataagtca"
# d = {}
#
# for i in str:
#     if d.get(i) is None:
#         d[i] = 1
#     else:
#         d[i] += 1
#
# for i, v in d.items():
#     print(f"{i}의 개수: {v}")

# 3
# str = "ctagttagctatagctaggctataagctgctagcggcgcgctagcacgagcgcgcttcctagcgacgacgatgcatgcgat"
# i = 0
# d = {}
#
# while i <= len(str):
#     codon = ""
#     if i+3 <= len(str):
#         codon = str[i:i+3]
#     else:
#         break
#
#     if d.get(codon) is None:
#         d[codon] = 1
#     else:
#         d[codon] += 1
#     i+=3
#
# for j, v in d.items():
#     print(f"{j} : {v}")

# 4
# lst = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
# f_lst = []
#
# for i in lst:
#     if type(i) == list:
#         for j in i:
#             f_lst.append(j)
#     else:
#         f_lst.append(i)
#
# print(f_lst)


# def flatten_list(lst: list) -> list:
#     n_lst = []
#     for i in lst:
#         if type(i) == list:
#             n_lst = n_lst + flatten_list(i)
#         else:
#             n_lst.append(i)
#
#     return n_lst
#
# lst = [1, 2, [3, [4, [5]]], [6, 7], [8, 9]]
# f_lst = flatten_list(lst)
#
# print(f_lst)

# p291
# # 2
# def mul(*values):
#     multiply = 1
#     for i in values:
#         multiply *= i
#     return multiply
#
# print(mul(5,7,9,10))

plates=["12가3456",
  "88다7788",
  "30라3003",
  "9사9999",
  "1233가4567",
  "200가1000",
  "174마2234",
   "59저4554",
   "88x1221"]

def is_palindrom_str(string:str) -> bool:
    """
    회문 문자열인지 확인
    """
    for i in range(len(string)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

# 데이터를 모두 받아오는 함수
def is_valid_plate(plate_lst: list) -> list:
    lst = []
    # 데이터의 하나씩 검사
    for plate in plate_lst:
        index = 0
        cnt = 0

        # plate 문자열 중에 한글을 찾는다.
        for i, c in enumerate(plate):
            if '\uAC00' <= c <= '\uD7A3':   # 한글일 때
                index = i    # 한글의 인덱스를 저장
                cnt += 1    # 한글이 나온 횟수를 저장

        if cnt >= 2:  # 한글이 2회 이상 나왔다면
            continue

        splited_plate = plate.split(plate[index])   # 방금 찾은 한글을 중심으로 문자열 분리

        # 앞 번호들의 개수 확인
        if len(splited_plate[0]) != 2 and len(splited_plate[0]) != 3:
            continue

        # 앞 번호들이 숫자인지 확인
        for c in splited_plate[0]:
            if  c < '0' or'9' < c:
                continue

        # 뒷 번호들의 개수 확인
        if len(splited_plate[1]) != 4:
            continue

        # 뒷 번호들이 숫자인지 확인
        for c in splited_plate[1]:
            if c < '0' or '9' < c:
                continue

        # 뒤 번호는 회문형태인지 확인
        if is_palindrom_str(splited_plate[1]):
            lst.append(plate)

    return lst

print(is_valid_plate(plates))