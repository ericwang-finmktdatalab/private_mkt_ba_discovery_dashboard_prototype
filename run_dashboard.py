import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate weighted EBITDA growth
def weighted_ebitda(group):
    return (group["EBITDA_GROWTH"] * group["MARKET_VALUE"]).sum() / group["MARKET_VALUE"].sum()

# Function to add centered value labels
def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')  # Aligning text at center

# Load dataset
df = pd.read_csv("data/Company_Metrics.csv")

# Ensure numeric types
df["EBITDA_GROWTH"] = pd.to_numeric(df["EBITDA_GROWTH"], errors="coerce")
df["MARKET_VALUE"] = pd.to_numeric(df["MARKET_VALUE"], errors="coerce")

# Drop rows with missing critical values
df = df.dropna(subset=["EBITDA_GROWTH", "MARKET_VALUE"])

# -------------------------------------------------------------------
# 1) SECTOR level weighted EBITDA growth
sector_group = df.groupby("SECTOR").apply(weighted_ebitda).reset_index(name="SECTOR_EBITDA_GROWTH")

plt.figure(figsize=(8,6))
plt.bar(sector_group["SECTOR"], sector_group["SECTOR_EBITDA_GROWTH"], color="skyblue")
add_labels(sector_group["SECTOR"], sector_group["SECTOR_EBITDA_GROWTH"])
plt.title("Sector-level Weighted EBITDA Growth")
plt.ylabel("Weighted EBITDA Growth")
plt.xlabel("Sector")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/Sector-level Weighted EBITDA Growth.png")
plt.close()

# -------------------------------------------------------------------
# 2) PARENT_FUND level weighted EBITDA growth
fund_group = df.groupby("PARENT_FUND").apply(weighted_ebitda).reset_index(name="FUND_EBITDA_GROWTH")

plt.figure(figsize=(8,6))
plt.bar(fund_group["PARENT_FUND"], fund_group["FUND_EBITDA_GROWTH"], color="lightgreen")
add_labels(fund_group["PARENT_FUND"], fund_group["FUND_EBITDA_GROWTH"])
plt.title("Fund-level Weighted EBITDA Growth")
plt.ylabel("Weighted EBITDA Growth")
plt.xlabel("Parent Fund")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/Fund-level Weighted EBITDA Growth.png")
plt.close()