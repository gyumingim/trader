import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 데이터 준비
metrics = {
    'price': [0.15, 0.00],
    'price_change_percent': [260478388.08, 205.89],
    'swaps': [70727.42, 43627.95],
    'volume': [19674152.50, 3005235.05],
    'liquidity': [5979004.58, 17249.62],
    'market_cap': [1606680102.58, 20835.07],
    'holder_count': [61853.75, 964.10],
    'buys': [44529.25, 32260.55],
    'sells': [26198.17, 11367.40],
    'swaps_24h': [70727.42, 43627.95],
    'initial_liquidity': [4693.75, 30107.05],
    'top_10_holder_rate': [0.19, 0.18],
    'bluechip_owner_percentage': [0.01, 0.01],
    'smart_degen_count': [5.33, 0.45],
    'renowned_count': [28.08, 3.15]
}

# 그래프 스타일 설정
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))

# 데이터 준비
metrics_names = list(metrics.keys())
high_values = [metrics[metric][0] for metric in metrics_names]
low_values = [metrics[metric][1] for metric in metrics_names]

# 로그 스케일로 변환 (0이나 음수값 처리)
def safe_log(x):
    return np.log10(x) if x > 0 else 0

high_values_log = [safe_log(x) for x in high_values]
low_values_log = [safe_log(x) for x in low_values]

# 막대 그래프 생성
x = np.arange(len(metrics_names))
width = 0.35

fig, ax = plt.subplots(figsize=(15, 8))
rects1 = ax.bar(x - width/2, high_values_log, width, label='High Liquidity Group')
rects2 = ax.bar(x + width/2, low_values_log, width, label='Low Liquidity Group')

# 그래프 꾸미기
ax.set_ylabel('Log10 Scale')
ax.set_title('Comparison of Metrics between High and Low Liquidity Groups')
ax.set_xticks(x)
ax.set_xticklabels(metrics_names, rotation=45, ha='right')
ax.legend()

# 값 레이블 추가
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                   xy=(rect.get_x() + rect.get_width() / 2, height),
                   xytext=(0, 3),  # 3 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom', rotation=0)

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.savefig('20250101/metrics_comparison.png')
plt.close()

# 개별 지표 시각화
for metric in metrics_names:
    plt.figure(figsize=(8, 6))
    values = [metrics[metric][0], metrics[metric][1]]
    
    plt.bar(['High Liquidity', 'Low Liquidity'], values)
    plt.title(f'{metric} Comparison')
    plt.ylabel('Value')
    
    # 값이 매우 큰 경우 로그 스케일 사용
    if max(values) > 1000:
        plt.yscale('log')
    
    plt.savefig(f'20250101/metric_{metric}.png')
    plt.close()
