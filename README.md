# ai-news-to-slack

Automate sending the latest AI startup news to a Slack channel every morning.

## Features

- Fetches top AI startup news from Crunchbase News API
- Posts formatted headlines to Slack via webhook
- Runs daily at 09:00 UTC

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/ai-news-to-slack.git
cd ai-news-to-slack
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

**Required packages:**  
- `requests`
- `schedule`

You can also install them manually:

```sh
pip install requests schedule
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with the following content:

```
CRUNCHBASE_API_KEY=your_crunchbase_api_key
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/webhook/url
```

Or set them in your shell before running:

```sh
export CRUNCHBASE_API_KEY=your_crunchbase_api_key
export SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/webhook/url
```

#### Environment Variables

| Variable              | Description                      |
|-----------------------|----------------------------------|
| `CRUNCHBASE_API_KEY`  | Your Crunchbase News API key     |
| `SLACK_WEBHOOK_URL`   | Slack Incoming Webhook URL       |

### 4. Run the Application

```sh
python main.py
```

You should see:

```
✅ AI news automation started...
```

The app will fetch news and post to Slack every day at 09:00 UTC.

## Customization

- To change the news source, modify `fetch_ai_news` in `main.py`.
- To adjust the schedule, edit the line with `schedule.every().day.at("09:00").do(job)` in `main.py`.

## Author

👤 Daniel Samuel  
GitHub: [DanSam5k](https://github.com/DanSam5k)  
Twitter: [\_dan\_sam](https://twitter.com/_dan_sam)  
LinkedIn: [dansamuel](https://linkedin.com/in/dansamuel)

## License
MIT