from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("../chromedriver")
driver = webdriver.Chrome(service=service)

driver.get('https://www.naver.com')
driver.implicitly_wait(10) #로딩이 끝날때까지 10초 기다리기

driver.find_element(By.CSS_SELECTOR, "a.nav.shop").click()
time.sleep(2)

search = driver.find_element(By.CSS_SELECTOR, "input._searchInput_search_input_QXUFf")
search.click()
