import json

# JSON 파일 읽기
with open('20250101/a.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# smart_degen_count가 1 이상인 코인들을 추출하고 추가 정보 포함
smart_degens = []
for pool in data['data']['rank']:
    if pool['smart_degen_count'] >= 1:
        # None 값을 0으로 처리
        initial_liq = float(pool['initial_liquidity'] or 0)
        current_liq = float(pool['liquidity'] or 0)
        
        # 유동성 상승률 계산 (현재 유동성 / 초기 유동성)
        liq_growth = current_liq / initial_liq if initial_liq > 0 else 0
        
        smart_degens.append({
            'address': pool['address'],
            'smart_degen_count': pool['smart_degen_count'],
            'renowned_count': pool.get('renowned_count', 0),
            'bluechip_count': pool.get('bluechip_count', 0),
            'market_cap': float(pool['market_cap'] or 0),
            'current_liq': current_liq,
            'init_liq': initial_liq,
            'liq_growth': liq_growth
        })

# smart_degen_count 기준으로 내림차순 정렬
smart_degens.sort(key=lambda x: x['smart_degen_count'], reverse=True)

# 결과를 CSV 파일로 저장
with open('20250101/smart_degens.csv', 'w', encoding='utf-8-sig') as f:  # utf-8-sig를 사용하여 Excel에서 한글이 깨지지 않도록 함
    f.write("Address,Smart Degen Count,Renowned Count,Bluechip Count,Market Cap,Current Liquidity,Initial Liquidity,Liquidity Growth\n")
    for coin in smart_degens:
        f.write(f"{coin['address']},{coin['smart_degen_count']},{coin['renowned_count']},{coin['bluechip_count']},"
                f"{coin['market_cap']:.2f},{coin['current_liq']:.2f},{coin['init_liq']:.2f},{coin['liq_growth']:.2f}\n")

print(f"총 {len(smart_degens)}개의 코인이 smart_degen_count >= 1 조건을 만족합니다.")
print(f"결과가 'smart_degens.csv' 파일로 저장되었습니다.")
