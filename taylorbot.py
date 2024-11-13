import csv
import os
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
from bluesky import BlueskyAPI

load_dotenv()

def loadSongs():
    pickleFrameFile = Path("./pickleFrameFile")
    if pickleFrameFile.is_file():
        df = pd.read_pickle(pickleFrameFile)
    else: 
        df = pd.read_csv("Hot 100.csv")
        df.drop_duplicates(subset=["performer", "song"], inplace=True)  # dedupe
        df = df[["performer", "song"]]  # drop all other columns
        df.to_pickle(pickleFrameFile)
    return df

def skeet_song(api, df):
    line = df.sample().iloc[0]  # Sample a row and get it as a Series
    formatted_line = f"{line['performer']} - {line['song']} (Taylor's Version)"
    api.skeet(formatted_line)
    print(f"Skeeted: {formatted_line}")

if __name__ == "__main__":
    df = loadSongs()

    # Set up Bluesky API
    api = BlueskyAPI(os.environ("TAYLORS_USER"), os.environ("TAYLORS_PW"))  # replace with your actual username and password

    # Skeet a song
    skeet_song(api, df)