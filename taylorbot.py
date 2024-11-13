import csv
import pandas as pd
from pathlib import Path

progress_file=Path("~/.taylorsbot")
if progress_file.is_file():
    with open(progress_file,"r+") as progressfd:
        progress=progressfd.readline()
        print ("Progress: "+ str(progress))

df = pd.read_csv("Hot 100.csv")
count1 = len(df.index)
#print(count1)
df.drop_duplicates(subset=["song","performer"], inplace=True) #dedupe
df = df[["performer", "song"]] # drop all other columns
#count2 = len(df.index)
line = df.sample() + "(Taylor's Version)"
#print(count2)
#print(line)
