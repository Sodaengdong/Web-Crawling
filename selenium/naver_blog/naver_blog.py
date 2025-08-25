
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
import time


url = "https://naver.com/"
id = "아이디"
pw = "비밀번호!"

#자동으로 크롬 버전을 확인하는 코드
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)
    
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
driver.implicitly_wait(5)

#execute_script 함수 사용하여 자바스크트로 id, pw 넘겨주기
driver.execute_script("document.getElementsByName('id')[0].value='" + id + "'")
driver.execute_script("document.getElementsByName('pw')[0].value='" + pw + "'")

#로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, '#log\.login').click()
time.sleep(1)

#로그인 정보 저장안함 클릭
driver.find_element(By.ID, 'new.dontsave').click()
time.sleep(1)

#네이버블로그 이동
baseurl = "https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0"
driver.get(baseurl)

#글쓰기 
driver.find_element(By.XPATH, '//*[@id="container"]/div/aside/div/div[1]/nav/a[2]').click()
time.sleep(10)

# 여기부터 안됨
title_bar = driver.find_element(By.ID, 'SE-7d8135bc-9aa3-4966-9cc1-8d9ef68d6eca')
title_bar.send_keys('테스트')

driver.find_element(By.XPATH, '//*[@id="SE-e01acf5c-b17a-41ba-ac08-f6fc264c573d"]/span[2]').send_keys('테스트 자동화로 글쓰기')
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div/div[3]/div[2]/button').click()
time.sleep(5)