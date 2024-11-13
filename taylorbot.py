import csv
import os
import argparse
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
import blueskyapi

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


def skeet_song(client, df, dry_run):
    line = df.sample().iloc[0]  # Sample a row and get it as a Series
    formatted_line = f"{line['performer']} - {line['song']} (Taylor's Version)"
    if dry_run:
        print(f"[DRY RUN] Would skeet: {formatted_line}")
    else:
        client.send_post(formatted_line)
        print(f"Skeeted: {formatted_line}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Post a random song to Bluesky.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be skeeted without posting.",
    )
    args = parser.parse_args()

    # Load songs
    df = loadSongs()

    # Set up Bluesky API client
    client = blueskyapi.Client()
    client.login(os.getenv("BLUESKY_USERNAME"), os.getenv("BLUESKY_PASSWORD"))

    # Skeet a song (or dry run)
    skeet_song(client, df, args.dry_run)
