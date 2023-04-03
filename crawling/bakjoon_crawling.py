from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
#BeautifulSoup 클래스는 웹문서를 파싱하여, 크롤링을 할 수 있게 문서 개체를 생성해준다

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://www.acmicpc.net/problemset/1')

html = driver.page_source
soup = BeautifulSoup(html,'html.parser') 

#대상 선택
answerrate = soup.select('tbody tr td:nth-child(6)')
sum = 0

for text in answerrate:
    print(text.text[0:-1]) #float형 정답률 데이터만 추출하기 위해 '%' cut
    sum += float(text.text[0:-1]) #합계

length = len(answerrate)
acp = round(sum/(len(answerrate)),3) #평균을 소수 셋째 자리까지 표시

print('Size='+str(length))
print('Average Correct Percentage='+str(acp)+'%')
    
