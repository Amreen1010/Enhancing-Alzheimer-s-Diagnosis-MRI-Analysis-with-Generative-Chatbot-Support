import html
import requests
import streamlit as st

KEYWORD = "alzheimer"
DEFAULT_IMAGE = "C:/Users/ASHWIN M/Alzheimers_Prediction_System-main/assets/images/default.webp"
NEWS_API_KEY = "c886b1766bdc4af69e19811aef4dc9e8"

def _get_news():
    response = requests.get(f'https://newsapi.org/v2/everything?q={KEYWORD}&apiKey={NEWS_API_KEY}&language=en&searchIn=title').json()
    return response.get('articles', [])

def news_page():
    news_articles = _get_news()
    if not news_articles:
        st.write("No news articles found.")
        return

    for random_news in news_articles:
        st.write(f"""<h2>{html.unescape(random_news['title'])}</h2><br>""", unsafe_allow_html=True)
        if random_news.get("urlToImage"):
            st.image(random_news["urlToImage"])
        else:
            st.image(DEFAULT_IMAGE)
        st.write(f"""
            <h5>{random_news['description']}</h5>
            Link : <a href="{random_news['url']}">{random_news['url'][:80]}...</a><br>
            Author : {random_news['author']}, &nbsp; <i>{random_news['publishedAt'][:10]}</i>
            <hr>
            """, unsafe_allow_html=True)

