import json
import csv

# JSON 파일 읽기
with open('20250106/코인데이터.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 결과를 저장할 리스트
filtered_coins = []

# renowned_count가 10 이상인 코인 필터링 및 데이터 추출
for coin in data['data']['pumps']:
    try:
        if int(coin.get('renowned_count', 0)) >= 1:
            liquidity = float(coin.get('liquidity', 0))
            initial_liquidity = float(coin.get('initial_liquidity', 0))
            market_cap = float(coin.get('usd_market_cap', 0))
            
            # 초기 유동성이 0이 아닌 경우에만 성장률 계산
            growth_rate = liquidity / initial_liquidity if initial_liquidity > 0 else 0
            
            filtered_coins.append({
                'address': coin['address'],
                'liquidity': liquidity,
                'initial_liquidity': initial_liquidity,
                'growth_rate': growth_rate,
                'market_cap': market_cap,
                'renowned_count': int(coin.get('renowned_count', 0))
            })
    except (KeyError, ValueError, TypeError):
        continue

# 성장률 기준으로 정렬 (내림차순)
filtered_coins.sort(key=lambda x: x['growth_rate'], reverse=True)

# 결과를 CSV 파일로 저장
with open('20250106/유명지갑보유코인.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    # CSV 헤더 작성
    writer.writerow(['주소', '현재 유동성($)', '초기 유동성($)', '성장률(x)', '시가총액($)', '유명 지갑 수'])
    
    # 데이터 작성
    for coin in filtered_coins:
        writer.writerow([
            coin['address'],
            f"{coin['liquidity']:.2f}",
            f"{coin['initial_liquidity']:.2f}",
            f"{coin['growth_rate']:.2f}",
            f"{coin['market_cap']:.2f}",
            coin['renowned_count']
        ])
