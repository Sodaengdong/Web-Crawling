import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

#검색어 입력하기
search = input('검색어를 입력해주세요 : ')

sheet.append(["검색어명", "기사 제목", "기사 요약"])

#1~10페이지까지 수잡
for p in range(1, 10+1, 1):
    raw = requests.get("https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&q={s}&p={p}".format(s = search, p = p))
    html = BeautifulSoup(raw.text, 'html.parser')

    container = html.select("div.wrap_cont")

    for con in container:
        title = con.select_one("div.wrap_cont > a").text.strip()
        content = con.select_one("p.desc").text.strip()

        sheet.append([search, title, content])

wb.save("daum_news.xlsx")