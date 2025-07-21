import json
import pandas as pd

# Simulated news data
news_data = {
    "articles": [
        {
            "source": {"name": "CNN"},
            "author": "John Doe",
            "title": "Markets soar as investors cheer new tech breakthroughs",
            "description": "Technology stocks rallied today, led by gains in AI and cloud companies.",
            "content": "In a day of strong trading, tech companies saw major gains...",
            "publishedAt": "2025-07-21T09:30:00Z"
        },
        {
            "source": {"name": "BBC"},
            "author": "Jane Smith",
            "title": "Climate change protests escalate in Europe",
            "description": "Protests over climate policy intensified across several major cities...",
            "content": "Thousands of protesters gathered in London and Paris today...",
            "publishedAt": "2025-07-20T14:10:00Z"
        },
        {
            "source": {"name": "Reuters"},
            "author": "Mike Lee",
            "title": "Global oil prices fall amid supply boost",
            "description": "Crude oil futures dropped sharply after new supply reports...",
            "content": "Energy markets responded to increased output from key suppliers...",
            "publishedAt": "2025-07-19T17:45:00Z"
        },
        {
            "source": {"name": "TechCrunch"},
            "author": "Sara Kim",
            "title": "Startup raises $50M to fight misinformation with AI",
            "description": "A new AI platform aims to detect and block fake news in real-time...",
            "content": "The round was led by Sequoia Capital and signals rising interest in responsible AI...",
            "publishedAt": "2025-07-18T12:00:00Z"
        },
        {
            "source": {"name": "Al Jazeera"},
            "author": "Amir Hassan",
            "title": "Conflict in region X intensifies after peace talks stall",
            "description": "Diplomatic efforts failed again as tensions rose...",
            "content": "The UN expressed concern over the rising violence...",
            "publishedAt": "2025-07-17T21:00:00Z"
        }
    ]
}

# Save to a JSON file (optional for upload simulation)
with open("dummy_news_data.json", "w") as f:
    json.dump(news_data, f, indent=4)

# Convert to DataFrame for processing
df = pd.json_normalize(news_data["articles"])
df["publishedAt"] = pd.to_datetime(df["publishedAt"])
df.head()
