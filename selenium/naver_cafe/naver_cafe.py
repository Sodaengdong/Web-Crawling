import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
from bs4 import BeautifulSoup as bs
import csv

#카페 게시글 제목, 링크를 저장하는 리스트 생성
total_list = ['제목', '링크']

#데이터를 저장하는 csv파일 생성
f = open('craw.csv', 'w', encoding="euc-kr", newline='')
wr = csv.writer(f)
wr.writerow([total_list[0], total_list[1]])
f.close()

url = "https://nid.naver.com/nidlogin.login"
id = "아이디"
pw = "비밀번호"

#자동으로 크롬 버전을 확인하는 코드
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

#webdriver.Chrome() 함수의 'executable_path' 매개변수가 더 이상 권장되지 않음, 'Service' 객체를 전달하도록 변경
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

driver.implicitly_wait(2)
time
#execute_script 함수 사용하여 자바스크트로 id, pw 넘겨주기
driver.execute_script("document.getElementsByName('id')[0].value='" + id + "'")
driver.execute_script("document.getElementsByName('pw')[0].value='" + pw + "'")

#로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
time.sleep(1)

#로그인 정보 저장안함 클릭
driver.find_element(By.ID, 'new.dontsave').click()
time.sleep(1)

baseurl = "https://cafe.naver.com/swtester"
driver.get(baseurl)
