import pandas as pd
import matplotlib.pylot as plt

data = {
"stock_A": [50000,52000, 51000, 53000, 55000, 54000],
"stock_B": [80000, 78000, 81000, 79000,83000]

df = pd.DataFrame(data)
returns = df.pct().dropna() *100
average = returns.mean()
volatility = returns.std()

correlation = returns["stock_A"].corr(returns["stock_B"])

print("===평균 수익률 ===")
print(average,round(2))

print("===표준편차 ===")
print(volatility.round(2))


plt.plot(returns["Stock_A"], marker="o", label="Stock A")
plt.plot(returns["Stock_B"], marker="s", label="Stock B")

plt.title("Daily Stock Returns")
plt.xlabel("Day Index")
plt.ylabel("Return (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
