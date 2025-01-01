import json

# highgroup.txt에서 주소 읽기
with open('20250101/highgroup.txt', 'r', encoding='utf-8') as f:
    high_addresses = [line.split(',')[0].split(':')[1].strip() for line in f.readlines()]

# JSON 데이터 읽기
with open('20250101/a.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 분석할 지표들을 저장할 딕셔너리
metrics = {
    'price': [],
    'price_change_percent': [],
    'swaps': [],
    'volume': [],
    'liquidity': [],
    'market_cap': [],
    'holder_count': [],
    'buys': [],
    'sells': [],
    'swaps_24h': [],
    'initial_liquidity': [],
    'top_10_holder_rate': [],
    'bluechip_owner_percentage': [],
    'smart_degen_count': [],
    'renowned_count': []
}

# highgroup에 있는 주소들의 데이터 수집
for coin in data['data']['rank']:
    if coin['address'] in high_addresses:
        for metric in metrics:
            try:
                metrics[metric].append(float(coin[metric]))
            except (ValueError, KeyError, TypeError):
                continue

# 평균값 계산
averages = {}
for metric, values in metrics.items():
    if values:  # 값이 있는 경우에만 평균 계산
        avg = sum(values) / len(values)
        averages[metric] = avg

# 결과 출력 및 파일 저장
with open('metrics_analysis_low.txt', 'w', encoding='utf-8') as f:
    f.write("=== High Liquidity Group Metrics Analysis ===\n\n")
    
    for metric, avg in averages.items():
        output = f"{metric}:\n"
        output += f"  Average: {avg:,.2f}\n"
        output += f"  Min: {min(metrics[metric]):,.2f}\n"
        output += f"  Max: {max(metrics[metric]):,.2f}\n\n"
        
        print(output)
        f.write(output)

# high.txt 파일로 저장
with open('20250101/low.txt', 'w', encoding='utf-8') as f:
    for address in high_addresses:
        f.write(f"{address}\n")

print(f"Analysis complete. Results saved to metrics_analysis.txt")
print(f"High addresses saved to high.txt")
