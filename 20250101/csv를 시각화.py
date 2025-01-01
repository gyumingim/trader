import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# CSV 파일 읽기
df = pd.read_csv('20250101/smart_degens.csv')

# 한글 폰트 설정 (필요한 경우)
plt.rcParams['font.family'] = 'Malgun Gothic'

# 1. 상관관계 히트맵
plt.figure(figsize=(10, 8))
numeric_columns = ['Smart Degen Count', 'Renowned Count', 'Bluechip Count', 
                  'Market Cap', 'Current Liquidity', 'Initial Liquidity', 'Liquidity Growth']
correlation = df[numeric_columns].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('변수간 상관관계 히트맵')
plt.tight_layout()
plt.savefig('20250101/correlation_heatmap.png')
plt.close()

# 2. 산점도 매트릭스 (주요 변수만)
main_columns = ['Smart Degen Count', 'Renowned Count', 'Market Cap', 'Current Liquidity']
sns.pairplot(df[main_columns], diag_kind='kde')
plt.savefig('20250101/scatter_matrix.png')
plt.close()

# 3. Smart Degen Count vs Renowned Count 관계
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Smart Degen Count', y='Renowned Count')
plt.title('Smart Degen Count와 Renowned Count의 관계')
plt.savefig('20250101/smart_vs_renowned.png')
plt.close()

# 4. Market Cap과 Liquidity의 관계 (로그 스케일)
plt.figure(figsize=(10, 6))
plt.scatter(np.log1p(df['Market Cap']), np.log1p(df['Current Liquidity']))
plt.xlabel('Log Market Cap')
plt.ylabel('Log Current Liquidity')
plt.title('Market Cap과 Current Liquidity의 관계 (로그 스케일)')
plt.savefig('20250101/marketcap_vs_liquidity.png')
plt.close()

# 5. Top 10 코인의 Smart Degen vs Renowned Count
top_10 = df.nlargest(10, 'Smart Degen Count')
plt.figure(figsize=(12, 6))
x = range(len(top_10))
plt.bar(x, top_10['Smart Degen Count'], width=0.4, align='edge', label='Smart Degen')
plt.bar(x, top_10['Renowned Count'], width=-0.4, align='edge', label='Renowned')
plt.xticks(x, top_10['Address'].str[:10] + '...', rotation=45)
plt.legend()
plt.title('Top 10 코인의 Smart Degen vs Renowned Count')
plt.tight_layout()
plt.savefig('20250101/top10_comparison.png')
plt.close()

# 기본 통계 출력
print("\n기본 통계:")
print(df[numeric_columns].describe())

# 상관계수 출력
print("\n주요 상관계수:")
print(correlation['Smart Degen Count'].sort_values(ascending=False))
