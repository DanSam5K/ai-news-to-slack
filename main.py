# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dansam <dansam@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/08/19 16:59:21 by dansam            #+#    #+#              #
#    Updated: 2025/08/19 17:14:24 by dansam           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import requests
import schedule
import time
from datetime import datetime

# 🔑 Environment variables (set these before running)
CRUNCHBASE_API_KEY = os.getenv("CRUNCHBASE_API_KEY")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def fetch_ai_news():
    """
    Fetch latest AI startup news from Crunchbase News API.
    (If no access, replace with NewsAPI or other news sources.)
    """
    url = "https://api.crunchbase.com/api/v4/news"
    params = {
        "query": "AI startup",
        "limit": 5,
        "order": "newest",
        "user_key": CRUNCHBASE_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    headlines = []
    for article in data.get("data", []):
        title = article.get("title", "Untitled")
        link = article.get("url", "#")
        headlines.append(f"• <{link}|{title}>")

    return headlines


def send_to_slack(headlines):
    """
    Send formatted news to Slack via incoming webhook
    """
    if not headlines:
        text = "No new AI startup news today."
    else:
        text = "*🤖 Latest AI Startup News (" + datetime.utcnow().strftime("%Y-%m-%d") + ")*\n" + "\n".join(headlines)

    payload = {"text": text}
    requests.post(SLACK_WEBHOOK_URL, json=payload)


def job():
    headlines = fetch_ai_news()
    send_to_slack(headlines)


# Schedule once a day at 09:00 UTC
schedule.every().day.at("09:00").do(job)

print("✅ AI news automation started...")

while True:
    schedule.run_pending()
    time.sleep(60)
