import pandas as pd
import matplotlib.pyplot as plt

expr = pd.DataFrame({
    "sample_1": [15.2, 25.1, 8.5, 12.3, 30.5],
    "sample_2": [18.5, 30.2, 9.2, 11.8, 28.9],
    "sample_3": [2.1, 100.5, 1.8, 50.6, 150.2], 
    "sample_4": [20.3, 28.3, 10.1, 13.5, 32.1],
}, index=["TP53","EGFR","BRCA1","KRAS","MYC"])

expr["mean"] = expr.mean(axis=1)
expr["var"] = expr.var(axis=1)

print("=== 表达统计 ===")
print(expr[["mean","var"]])

plt.figure(figsize=(8,4))
plt.boxplot([expr["sample_1"], expr["sample_2"], expr["sample_3"], expr["sample_4"]],
            labels=expr.columns[:-2])
plt.title("Samples expression distribution")
plt.ylabel("expression")
plt.tight_layout()
plt.savefig("tcga_mini_boxplot.png")
print("✅ 图已存 tcga_mini_boxplot.png")
plt.show()