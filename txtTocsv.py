import pandas as pd

df = pd.read_csv("file.txt",delimiter="\n")

df.to_csv("test3.csv", encoding='utf-8', index=False)