import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfs = pd.read_excel("iron_ores.xlsx", sheet_name=None, skiprows=[0,2,3,4,5,6], parse_dates=["指标名称"])
rizhao = dfs["Rizhao Port"]
print(rizhao.head())
input()