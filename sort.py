import pandas as pd
import numpy as np


def remove_wf(df):
    for index, row in df.iterrows():
        if index == 911:
            runs_str = df['runs'][index]
            split = runs_str.split(",")
            print(type(split))
            print(split)
            for s in split:

    return df


games = ["Dark Souls", "Dark Souls II", "Dark Souls III", "Demon’s Souls", "Bloodborne", "Sekiro", "Elden Ring", "Hollow Knight", "Celeste", "Cuphead", "Hades", "Resident Evil 0", "Resident Evil", "Resident Evil 2", "Resident Evil 3", "Resident Evil 4", "Resident Evil 7", "Resident Evil 8", "Resident Evil 3", "Resident Evil Survivor", "Resident Evil Village",
         "Zelda: Breath of the Wild", "Zelda: Tears of the Kingdom", "Crash Bandicoot", "Crash Bandicoot 2", "Crash Bandicoot 3", "Crash Bandicoot 4", "Dishonored: Death of the Outsider", "Dishonored", "Dishonored 2", "Tormented Souls", "Lies of P", "Skyrim", "Minecraft", "Batman: Arkham Asylum", "Batman: Arkham City", "Batman: Arkham Origins", "Batman: Arkham Knight", "The Binding of Isaac"]
category = []
df = pd.read_csv("th_raw.csv", sep=',')
# df = df.iloc[: , 1:]
df['runner'] = df['runner'].str[:-15]
df['country'] = df['country'].str.replace(r'.*/', '', regex=True).str[:-4]
# df['runs']= df['runs'].str.replace(" (World’s First)","")
# df['runs']= df['runs'].str.replace(" (Worìd’s First)","")
df['runs'] = df['runs'].str.replace(" (Worìd’s First)", " (World’s First)")

df = remove_wf(df)

# df = df.drop_duplicates(subset=['runs'], keep='first')
df['game'] = ""
df['catgeory'] = ""
df['restriction'] = ""


print(df)
df.to_csv("a.csv", sep='|')
