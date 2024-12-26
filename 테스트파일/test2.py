from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pyautogui
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Selenium WebDriver 설정
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


# 웹 페이지로 이동
driver.get("https://pump.fun/board")

# 버튼 클릭 대기 및 클릭
driver.maximize_window()

sleep(.1)

# 쿠키 허용
pyautogui.moveTo(804, 938)
pyautogui.click()
sleep(0.2)
pyautogui.click()

sleep(1)


# 'div' 태그 중 id가 'p'로 시작하는 요소 선택
texts = []
for _ in range(1, 300):
    btn_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[3]/div[2]/div/div/button[2]")
    btn_element.click()
    sleep(0.1)

with open("output.txt", "w") as file:
    for item in texts:
        file.write(item + "\n")



