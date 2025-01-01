from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import json

# JSON 파일 읽기 (UTF-8 인코딩 지정)
with open('20250101/a.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 결과를 저장할 리스트
liquidity_changes = []

# 각 코인에 대해 유동성 변화율 계산
for coin in data['data']['rank']:
    try:
        initial_liquidity = float(coin['initial_liquidity'])
        current_liquidity = float(coin['liquidity'])
        
        if initial_liquidity > 0:  # 0으로 나누기 방지
            multiplier = current_liquidity / initial_liquidity
            
            # 결과 저장
            liquidity_changes.append({
                'address': coin['address'],
                'multiplier': multiplier
            })
    except (KeyError, ValueError, TypeError):
        continue

# 변화율 기준으로 정렬 (내림차순)
liquidity_changes.sort(key=lambda x: x['multiplier'], reverse=True)

# 결과를 파일에 저장 (UTF-8 인코딩 지정)
with open('output3.txt', 'w', encoding='utf-8') as f:
    for change in liquidity_changes:
        f.write(f"Address: {change['address']}, Liquidity Multiplier: {change['multiplier']:.2f}x\n")
