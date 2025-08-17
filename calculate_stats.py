import pandas as pd

data = pd.read_csv("appearances.csv", sep=';')

players = data["Name"].unique()

plate_appearances = {}

for player in players:
    appeared = data.loc[data["Name"]==player,"Name"].count()
    # print(type(appeared))
    plate_appearances[player] = int(appeared)

print(plate_appearances)