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
        # 'div' 태그 중 id가 'p'로 시작하는 요소 선택
        div_elements = driver.find_elements(By.XPATH, "//*[starts-with(@id, 'p')]")

        texts = []
        for element in div_elements:
            # 각 div_elements에서 /div[1]/div[1]을 찾음
            target_element = element.find_element(By.XPATH, './div[1]/div[1]')
            if "M" in target_element.text:
                break
            texts.append(target_element.text)

        # 텍스트 빈도 계산
        text_counts = Counter(texts)
        # dict_items 객체를 리스트로 변환
        sorted_text_counts = list(text_counts.items())
        # 날짜와 빈도수 추출
        counts = [item[1] for item in sorted_text_counts]  # 빈도수

        # 최대 주주 수치
        try:
            max_owner_amount = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[1]/div').text
            max_owner_amount = float(max_owner_amount[:-1])
            # 일정 이상이면 스캠
            if (max_owner_amount > 50):
                continue
        except:
            max_owner_amount = None

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
