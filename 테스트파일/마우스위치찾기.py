import pyautogui
import time

try:
    while True:
        # 현재 마우스 포인터 위치 가져오기
        print(pyautogui.position())  # 같은 줄에 출력
        time.sleep(0.1)  # 0.1초 대기 (조정 가능)
except KeyboardInterrupt:
    print("\nTracking stopped.")
