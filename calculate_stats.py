import pandas as pd

data = pd.read_csv("appearances.csv", sep=';')

players = data["Name"].unique()

count_towards_atbats = ["1b", "2b", "3b", "HR", "K", "ROE", "RFC", "GO", "FO"]
count_as_hits = ["1b", "2b", "3b", "HR"]
on_base = ["1b", "2b", "3b", "HR", "BB", "HBP"]

plate_appearances = data.groupby("Name").size()
atbats = data[data["Appearance"].isin(count_towards_atbats)].groupby("Name").size()
hits = data[data["Appearance"].isin(count_as_hits)].groupby("Name").size()
got_on_base = data[data["Appearance"].isin(on_base)].groupby("Name").size()

strikeouts = data[data["Appearance"]=="K"].groupby("Name").size()
stolen_bases = data.groupby("Name")["SB"].sum()
stolen_base_attempts = data.groupby("Name")["SBA"].sum()

average = (hits/atbats).round(3)
on_base_percentage = (got_on_base/plate_appearances).round(3)

singles = data[data["Appearance"] == "1b"].groupby("Name").size().reindex(atbats.index, fill_value=0)
doubles = data[data["Appearance"] == "2b"].groupby("Name").size().reindex(atbats.index, fill_value=0)
triples = data[data["Appearance"] == "3b"].groupby("Name").size().reindex(atbats.index, fill_value=0)
homeruns = data[data["Appearance"] == "HR"].groupby("Name").size().reindex(atbats.index, fill_value=0)

total_bases = singles*1 + doubles*2 + triples*3 + homeruns*4
slugging = (total_bases / atbats).round(3)

on_base_plus_slugging = on_base_percentage + slugging

# RISP stats
data_RISPonly = data[data["RISP"] == True]
RISP_strikeouts = data_RISPonly[data_RISPonly["Appearance"]=="K"].groupby("Name").size()
RISP_atbats = data_RISPonly[data_RISPonly["Appearance"].isin(count_towards_atbats)].groupby("Name").size()
RISP_hits = data_RISPonly[data_RISPonly["Appearance"].isin(count_as_hits)].groupby("Name").size()
RISP_gotonbase = data_RISPonly[data_RISPonly["Appearance"].isin(on_base)].groupby("Name").size()
RISP_stolenbases = data_RISPonly.groupby("Name")["SB"].sum()