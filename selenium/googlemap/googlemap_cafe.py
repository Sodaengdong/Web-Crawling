from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#chrome창(웹드라이버) 열기
service = Service("../chromedriver")
driver = webdriver.Chrome(service=service)
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)


#실행할 웹페이지 불러도기(구글 지도)
driver.get("https://www.google.com/maps/")

#검색창에 "카페" 검색
search = driver.find_element(By.CSS_SELECTOR, "#searchboxinput").send_keys('카페')
searchbutton = driver.find_element(By.CSS_SELECTOR, "#searchbox-searchbutton").click()

#999페이지까지 반복하기
for i in range(999):
    #시간 지연
    time.sleep(5)
    #가게 데이터 수집
    stores = driver.find_element(By.CSS_SELECTOR, "a.hfpxzc")

    for s in stores:
        title = driver.find_element(By.CSS_SELECTOR, "div.bfdHYd Ppzolf OFBs3e ").text