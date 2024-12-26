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

pyautogui.moveTo(958, 810)
pyautogui.click()

sleep(.1)

pyautogui.moveTo(183, 643)
pyautogui.click()

sleep(.1)


# 이건 마켓캡
pyautogui.moveTo(200, 860)
# 이건 최근 거래순
# pyautogui.moveTo(200, 740)
pyautogui.click()

sleep(0.1)

# 쿠키 허용
pyautogui.moveTo(804, 938)
pyautogui.click()

sleep(1)


# 'div' 태그 중 id가 'p'로 시작하는 요소 선택
texts = []
for _ in range(1, 20):
    for i in range(1, 50):
        # 각 div_elements에서 /div[1]/div[1]을 찾음
        target_element = driver.find_element(By.XPATH, f'/html/body/div[1]/main/div[1]/div[3]/div[1]/div[3]/div/div[{i}]')
        texts.append(target_element.get_attribute('id'))
    btn_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div[3]/div[2]/div/div/button[2]")
    btn_element.click()
    sleep(6)

with open("output.txt", "w") as file:
    for item in texts:
        file.write(item + "\n")



