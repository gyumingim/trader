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

with open('GMGN에서 API를 써서 추출한 데이터/base_output.txt', 'r') as file:
    COIN_ADDRESSES = [line.strip() for line in file]

print(COIN_ADDRESSES)

first = True

try:
    for COIN_ADDRESS in COIN_ADDRESSES:
        # 웹 페이지로 이동
        driver.get("https://pump.fun/coin/"+COIN_ADDRESS)

        # 버튼 클릭 대기 및 클릭
        driver.maximize_window()
        sleep(1)
        if first:
            sleep(1)
            pyautogui.moveTo(958, 810)
            pyautogui.click()
            first = False
        try:
            # 마켓캡
            market_cap = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[1]/div[1]/div/div[3]/span').text
            market_cap = market_cap[market_cap.index("$")+1:].replace(",", "")
            print(market_cap)
        except:
            market_cap = None
            


        try:
            with open('output2.txt', 'a') as f:
                f.write(f"https://pump.fun/coin/{COIN_ADDRESS}, COUNT : {counts[0]}, MAX_OWNER : {max_owner_amount}, MARKET_CAP : {market_cap}\n")
        except:
            with open('output2.txt', 'a') as f:
                f.write(f"https://pump.fun/coin/{COIN_ADDRESS}, COUNT : 0, MAX_OWNER : {max_owner_amount}, MARKET_CAP : {market_cap}\n")

        
        

finally:
    # WebDriver 종료
    driver.quit()
