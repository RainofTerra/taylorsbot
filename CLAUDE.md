# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

TaylorsBot is a Bluesky bot that posts random Billboard Hot 100 songs with "(Taylor's Version)" appended. It uses the AT Protocol to interact with Bluesky.

## Commands

Run the bot:
```bash
python taylorsbot.py
```

Dry run (preview without posting):
```bash
python taylorsbot.py --dry-run
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

- `taylorsbot.py` - Main application script
- `Hot 100.csv` - Billboard Hot 100 chart data
- `pickleFrameFile` - Cached pandas DataFrame for faster loading
- `.env` - Bluesky credentials (BLUESKY_USERNAME, BLUESKY_PASSWORD)

## Key Functions

- `loadSongs()` - Loads and deduplicates song data, uses pickle cache
- `skeet_song()` - Selects random song and posts to Bluesky

## Dependencies

- `atproto` - AT Protocol client for Bluesky
- `pandas` - Data processing
- `python-dotenv` - Environment variable loading
