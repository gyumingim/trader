from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pyautogui
import pandas as pd
import pyperclip

# Selenium WebDriver 설정
service = Service(GeckoDriverManager().install())
options = Options()
options.add_argument("--disable-extensions")  # 확장 프로그램 비활성화
driver = webdriver.Firefox(service=service, options=options)
driver.maximize_window()
# CSV 파일 읽기
df = pd.read_csv('20250106/유명지갑보유코인_20250115_1740.csv')

image_path = 'marketcap.png'
search_region = (100, 238, 1400, 50)
# 결과를 저장할 리스트
results = []

cnt = 0

try:
    for index, row in df.iterrows():
        try:
            cnt += 1
            address = row['주소']
            old_marketcap = row['시가총액($)']
            
            # 웹페이지 접속
            url = f"https://pump.fun/coin/{address}"
            driver.get(url)
            print(address)
            sleep(1000)

            pyautogui.moveTo(958, 855)
            pyautogui.click()
            
            # 페이지 로딩을 위한 대기 시간 증가
            sleep(1.5)  # 5초에서 10초로 증가
            
            try:
                center = pyautogui.locateCenterOnScreen(
                    image_path, 
                    region=search_region, 
                    confidence=0.8,  # OpenCV 필요
                    grayscale=True   # 흑백 적용
                )
                pyautogui.moveTo(center)
                pyautogui.tripleClick()
                pyautogui.hotkey("ctrl", "c")
                copied_text = pyperclip.paste()

                market_cap = float(copied_text[13:].replace(",", ""))

                # 변화율 계산
                change_percent = ((market_cap - old_marketcap) / old_marketcap) * 100
                
                results.append({
                    '주소': address,
                    '이전_시가총액': old_marketcap,
                    '현재_시가총액': market_cap,
                    '변화율': change_percent
                })
                
                print(f"주소: {address}")
                print(f"이전 시가총액: ${old_marketcap:,.2f}")
                print(f"현재 시가총액: ${market_cap:,.2f}")
                print(f"변화율: {change_percent:.2f}%")
                print("-" * 50)

            except Exception as e:
                print(f"주소 {address}에서 오류 발생: {str(e)}")
                results.append({
                    '주소': address,
                    '이전_시가총액': old_marketcap,
                    '현재_시가총액': 'ERROR',
                    '변화율': 'ERROR'
                })
            if cnt >= 15:
                break
            
        except Exception as e:
            print(f"처리 중 오류 발생: {str(e)}")
            continue
except Exception as e:
    print(e)
finally:
    driver.quit()

# 결과를 DataFrame으로 변환하고 CSV로 저장
results_df = pd.DataFrame(results)
results_df.to_csv('시가총액_변화_결과.csv', index=False, encoding='utf-8-sig')
