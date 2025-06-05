import sys
import subprocess
from urllib import request, parse
from bs4 import BeautifulSoup

try:
    import requests
except:
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'requests'])
    import requests

# try:
#     from bs4 import BeautifulSoup
# except:
#     subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
#     subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'beautifulsoup4'])
#     from bs4 import BeautifulSoup

def main():

    city = "대전"
    # 입력 검사 -> 유효할 때까지 재입력
    # 유효 도시명 검사

    try:
        city = parse.quote(city, encoding='utf-8')
        url = f"https://www.diningcode.com/list.dc?query={city}"
        target = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

        soup = BeautifulSoup(target.text, "html.parser")

        print(soup)


        # output = ""
        # for i in soup.select('h2'):
        #     print(i)

    except Exception as e:
        print("error", e)

if __name__ == "__main__":
    main()

