from selenium import webdriver
import os

currentPath= os.getcwd() # getcwd() : Get + Current + Woring Directory 현재 작업 경로를 얻다
os.chdir(currentPath)  # chdir() : 디렉토리 위치 변경

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

Google = "https://www.google.com/"

driver.get(Google)

#clone 테스트
