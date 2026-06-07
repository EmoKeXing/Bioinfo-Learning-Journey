import pandas as pd
data={
    "gene":["TP53","EGFR","BRCA1","KRAS","MYC","PTEN"],
    "expression":[18.5,95.3,9.2,68.7,142.0,7.8],
    "p_value":[0.03,0.001,0.21,0.008,0.0005,0.44],
    "group":["tsg","oncogene","tsg","oncogene","oncogene","tsg"]
}
df = pd.DataFrame(data)
print("=== 原始数据 ===")
print(df)

candidates = df[(df["expression"] > 20)&(df["p_value"] < 0.05)]

print("\n=== 候选基因 ===")
print(candidates)

candidates.to_csv("candidates.csv", index=False)
print("\n 已保存 candidates.csv")