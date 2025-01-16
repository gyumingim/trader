import json
import csv
from datetime import datetime

# JSON 파일 읽기
with open('20250106/코인데이터2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 결과를 저장할 리스트
filtered_coins = []

# 현재 날짜 가져오기
current_date = datetime.now().date()

cnt = 0;

# renowned_count가 1 이상인 코인 필터링 및 데이터 추출
print("print(len(data['data']['completeds']))")
print(len(data['data']['completeds']))

for coin in data['data']['completeds']:
    try:
        base_token_info = coin
        renowned_count = int(base_token_info.get('renowned_count', 0))
        
        if renowned_count >= 1:
            created_date = datetime.fromtimestamp(int(coin.get('open_timestamp', 0))).date() if coin.get('open_timestamp') else None
            created_date_str = created_date.strftime('%Y-%m-%d') if created_date else 'Unknown'
            
            liquidity = float(base_token_info.get('volume', 0)) if base_token_info.get('volume') else 0
            initial_liquidity = float(coin.get('initial_liquidity', 0)) if coin.get('initial_liquidity') else 0
            market_cap = float(base_token_info.get('market_cap', 0)) if base_token_info.get('market_cap') else 0
            
            growth_rate = (liquidity / initial_liquidity) if initial_liquidity > 0 else 0

            filtered_coins.append({
                'address': base_token_info['address'],
                'symbol': base_token_info.get('symbol', ''),
                'liquidity': liquidity,
                'initial_liquidity': initial_liquidity,
                'growth_rate': growth_rate,
                'market_cap': market_cap,
                'renowned_count': renowned_count,
                'created_at': created_date_str
            })
        cnt += 1
    except Exception as e:
        print(f"Error processing coin: {e}")
        continue

print(cnt)
# 유명 지갑 수(renowned_count) 기준으로 정렬 (내림차순)
filtered_coins.sort(key=lambda x: x['renowned_count'], reverse=True)

# 현재 시간을 YYYYMMDD_HHMM 형식으로 가져오기
current_time = datetime.now().strftime('%Y%m%d_%H%M')

# CSV 파일 저장
with open(f'20250106/유명지갑보유코인_{current_time}.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['주소', '심볼', '24시간 거래량($)', '초기 유동성($)', '성장률(x)', '시가총액($)', '유명 지갑 수', '생성일'])
    
    for coin in filtered_coins:
        writer.writerow([
            coin['address'],
            coin['symbol'],
            f"{coin['liquidity']:.2f}",
            f"{coin['initial_liquidity']:.2f}",
            f"{coin['growth_rate']:.2f}",
            f"{coin['market_cap']:.2f}",
            coin['renowned_count'],
            coin['created_at']
        ])

print("CSV 파일 저장 완료")
