import pandas as pd
import re
import numpy as np

games = ["Dark Souls", "Dark Souls II", "Dark Souls III", "Demon’s Souls", "Bloodborne", "Sekiro", "Elden Ring", "Hollow Knight", "Celeste", "Cuphead", "Hades", "Resident Evil 0", "Resident Evil", "Resident Evil 2", "Resident Evil 3", "Resident Evil 4", "Resident Evil 7", "Resident Evil 8", "Resident Evil 3", "Resident Evil Survivor", "Resident Evil Village",
         "Zelda: Breath of the Wild", "Zelda: Tears of the Kingdom", "Crash Bandicoot", "Crash Bandicoot 2", "Crash Bandicoot 3", "Crash Bandicoot 4", "Dishonored: Death of the Outsider", "Dishonored", "Dishonored 2", "Tormented Souls", "Lies of P", "Skyrim", "Minecraft", "Batman: Arkham Asylum", "Batman: Arkham City", "Batman: Arkham Origins", "Batman: Arkham Knight", "The Binding of Isaac"]


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


def remove_wf(df):
    for index, row in df.iterrows():
        indices = []
        set_runs = set()
        if index == 911:
            runs_str = df['runs'][index]
            for game in games:
                if game in runs_str:
                    tmp_ind = list(find_all(runs_str, game))
                    indices.extend(tmp_ind)
            indices.sort()
            print(indices)
            result = []
            prev_index = 0
            for index in indices:
                result.append(runs_str[prev_index:index])
                prev_index = index
            result.append(runs_str[prev_index:])
            for r in result:
                print(r)
                if " (World’s First)" in r:
                    tmp_r = r.strip(" (World’s First)")
                    set_runs.add(tmp_r)
            print(set_runs)

    return df


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
