import pandas as pd

data = pd.read_csv("appearances.csv", sep=';')

players = data["Name"].unique()
