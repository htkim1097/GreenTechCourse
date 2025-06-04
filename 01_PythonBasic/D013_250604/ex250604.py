from urllib import request
#
# # urlopen(): URL 웹페이지를 열어주는 함수
# target = request.urlopen("https://news.naver.com")
# output = target.read()
#
# print(output)

# 420
import os

# output = os.listdir("..")
# print(output)
# print()
#
# for path in output:
#     if os.path.isdir(path):
#         print("폴더:", path)
#     else:
#         print("파일:", path)


# def read_folder(path):
#     # 폴더의 요소 읽어 들이기
#     output = os.listdir(path)
#
#     # 폴더의 요소 구분하기
#     for item in output:
#         if os.path.isdir(item):
#             # 폴더라면 계속 읽어 들이기
#             read_folder(path + "/" + item)
#         else:
#             # 파일이라면 출력하기
#             print("파일: ", item)
#
# read_folder("..")

# # 인코딩 : 암호화 예: str -> b`
# # 디코딩 : b` -> str 로 변환, 복호화
#
# tg=request.urlopen("https://news.naver.com/")
# dec_out = tg.read().decode('utf-8')
# print(dec_out)
#
# link_list = []
# s_in = dec_out.find("https")
# link_list.append(dec_out[s_in:s_in + dec_out[s_in:].index('"')])
# print(link_list)

# 426
# from urllib import request
# from bs4 import BeautifulSoup
#
# target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
#
# # html 구조를 가져온다.
# soup = BeautifulSoup(target, "html.parser")
#
# # location 태그를 찾아 location 덩어리를 가져온다.
# for location in soup.select("location"):
#     # location 태그 내부에 city, wf, tmn, tmx 태그를 찾아 출력한다.
#     print("도시:", location.select_one("city").string)
#     print("날씨:", location.select_one("wf").string)
#     print("최저기온:", location.select_one("tmn").string)
#     print("최고기온:", location.select_one("tmx").string)
#     print()

# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "<h1>Hello World</h1>"
#
# if __name__ == '__main__':
#     app.run()
