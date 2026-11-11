
import pandas as pd

# 두 주식의 5일간 가상 수익률 (%)
data = {
    "Stock_A": [2, 3, -1, 4, 2],
    "Stock_B": [-2, -3, 1, -4, -2]
}

df = pd.DataFrame(data)

# 상관계수
correlation = df["Stock_A"].corr(df["Stock_B"])

# 공분산
covariance = df["Stock_A"].cov(df["Stock_B"])

print("상관계수:", round(correlation, 2))
print("공분산:", round(covariance, 2))


import matplotlib.pyplot as plt

plt.plot(df["Stock_A"], marker="o", label="Stock A")
plt.plot(df["Stock_B"], marker="s", label="Stock B")

plt.title("Stock Returns Comparison")
plt.xlabel("Day Index")
plt.ylabel("Return (%)")
plt.legend()
plt.grid(True)

plt.show()
