import pandas as pd

data = pd.read_csv("appearances.csv", sep=';')

players = data["Name"].unique()

plate_appearances = {}
at_bats = {}

count_towards_atbats = ["1b", "2b", "3b", "HR", "K", "ROE", "RFC", "GO", "FO"]

plate_appearances = data.groupby("Name").size()

# for player in players:
#     appeared = data.loc[data["Name"]==player,"Name"].count()
#     plate_appearances[player] = int(appeared)
#     turns_at_bat = data.loc[
#         ((data["Appearance"] == "1b") |
#         (data["Appearance"] == "2b") |
#         (data["Appearance"] == "3b") |
#         (data["Appearance"] == "HR") |
#         (data["Appearance"] == "K") |
#         (data["Appearance"] == "ROE") |
#         (data["Appearance"] == "RFC") |
#         (data["Appearance"] == "GO") |
#         (data["Appearance"] == "FO")) &
#         (data["Name"] == player) 
#         ,"Appearance"].count()
#     at_bats[player] = int(turns_at_bat)
