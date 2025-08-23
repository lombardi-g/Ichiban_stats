import pandas as pd

data = pd.read_csv("appearances.csv", sep=';')

players = data["Name"].unique()

count_towards_atbats = ["1b", "2b", "3b", "HR", "K", "ROE", "RFC", "GO", "FO"]
count_as_hits = ["1b", "2b", "3b", "HR"]
on_base = ["1b", "2b", "3b", "HR", "BB", "HBP"]

plate_appearances = data.groupby("Name").size()
atbats = data[data["Appearance"].isin(count_towards_atbats)].groupby("Name").size()
hits = data[data["Appearance"].isin(count_as_hits)].groupby("Name").size()
