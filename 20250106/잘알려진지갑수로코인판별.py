import json
import csv
from datetime import datetime

# JSON 파일 읽기
with open('20250106/코인데이터.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 결과를 저장할 리스트
filtered_coins = []

# 현재 날짜 가져오기
current_date = datetime.now().date()

# renowned_count가 1 이상인 코인 필터링 및 데이터 추출
for coin in data['data']['rank']:
    try:
        if int(coin.get('renowned_count', 0)) >= 1:
            # 생성일 처리
            created_date = datetime.fromtimestamp(int(coin.get('open_timestamp', 0))).date() if coin.get('open_timestamp') else None
            
            # 날짜 차이가 1일 이하인 경우만 처리
            if created_date and (current_date - created_date).days <= 1:
                liquidity = float(coin.get('liquidity', 0))
                initial_liquidity = float(coin.get('initial_liquidity', 0))
                market_cap = float(coin.get('market_cap', 0))
                
                growth_rate = liquidity / initial_liquidity if initial_liquidity > 0 else 0
                
                filtered_coins.append({
                    'address': coin['address'],
                    'liquidity': liquidity,
                    'initial_liquidity': initial_liquidity,
                    'growth_rate': growth_rate,
                    'market_cap': market_cap,
                    'renowned_count': int(coin.get('renowned_count', 0)),
                    'created_at': created_date.strftime('%Y-%m-%d')
                })
    except (KeyError, ValueError, TypeError):
        continue

# 유명 지갑 수(renowned_count) 기준으로 정렬 (내림차순)
filtered_coins.sort(key=lambda x: x['renowned_count'], reverse=True)

# 현재 시간을 YYYYMMDD_HHMM 형식으로 가져오기
current_time = datetime.now().strftime('%Y%m%d_%H%M')
print(current_time)

# 결과를 CSV 파일로 저장
with open(f'20250106/유명지갑보유코인_{current_time}.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    # CSV 헤더 작성
    writer.writerow(['주소', '현재 유동성($)', '초기 유동성($)', '성장률(x)', '시가총액($)', '유명 지갑 수', '생성일'])
    
    # 데이터 작성
    for coin in filtered_coins:
        writer.writerow([
            coin['address'],
            f"{coin['liquidity']:.2f}",
            f"{coin['initial_liquidity']:.2f}",
            f"{coin['growth_rate']:.2f}",
            f"{coin['market_cap']:.2f}",
            coin['renowned_count'],
            coin['created_at']
        ])
