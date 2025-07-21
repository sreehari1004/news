import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob

# Sample news data
news_data = {
    "articles": [
        {
            "title": "Markets soar as investors cheer new tech breakthroughs",
            "description": "Technology stocks rallied today, led by gains in AI and cloud companies."
        },
        {
            "title": "Climate change protests escalate in Europe",
            "description": "Protests over climate policy intensified across several major cities."
        },
        {
            "title": "Global oil prices fall amid supply boost",
            "description": "Crude oil futures dropped sharply after new supply reports."
        },
        {
            "title": "Startup raises $50M to fight misinformation with AI",
            "description": "A new AI platform aims to detect and block fake news in real-time."
        },
        {
            "title": "Conflict in region X intensifies after peace talks stall",
            "description": "Diplomatic efforts failed again as tensions rose."
        }
    ]
}

# Convert to DataFrame
df = pd.DataFrame(news_data["articles"])

# Sentiment analysis
df["title_sentiment"] = df["title"].apply(lambda x: TextBlob(x).sentiment.polarity)
df["description_sentiment"] = df["description"].apply(lambda x: TextBlob(x).sentiment.polarity)

# Streamlit UI
st.title("📰 News Sentiment Dashboard")

st.subheader("📈 Title Sentiment Chart")
fig1 = px.bar(df, x="title", y="title_sentiment", title="Sentiment of News Titles")
st.plotly_chart(fig1)

st.subheader("🧾 Description Sentiment Chart")
fig2 = px.bar(df, x="title", y="description_sentiment", title="Sentiment of Descriptions")
st.plotly_chart(fig2)

st.subheader("📊 Raw Data")
st.dataframe(df)
