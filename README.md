# TaylorsBot

A Bluesky bot that posts random songs from the Billboard Hot 100 chart with "(Taylor's Version)" appended.

## Features

- Randomly selects songs from the Billboard Hot 100 historical dataset
- Posts formatted messages to Bluesky via the AT Protocol
- Dry-run mode for testing without posting
- Caches processed data for faster subsequent runs
- Docker support for containerized deployment

## Prerequisites

- Python 3.13+
- A Bluesky account

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd taylorsbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Bluesky credentials:
   ```
   BLUESKY_USERNAME=your-username.bsky.social
   BLUESKY_PASSWORD=your-app-password
   ```

## Usage

Run the bot:
```bash
python taylorsbot.py
```

Preview posts without actually posting (dry run):
```bash
python taylorsbot.py --dry-run
```

## Docker

Build the image:
```bash
docker build -t taylorsbot .
```

Run the container:
```bash
docker run --env-file .env taylorsbot
```

## Data

The bot uses Billboard Hot 100 chart data (`Hot 100.csv`) containing historical chart entries. Songs are deduplicated by performer and title before random selection.

## License

MIT
