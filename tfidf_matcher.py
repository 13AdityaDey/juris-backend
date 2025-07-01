from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def preprocess_text(text):
    return text.lower().strip()

def get_top_matches(user_query, df, top_n=5):
    if df.empty:
        return pd.DataFrame()

    # Combine title and summary (or any other relevant fields)
    documents = (df["title"].fillna("") + " " + df["summary"].fillna("")).apply(preprocess_text)
    
    # Vectorize text
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Vectorize user query
    query_tfidf = vectorizer.transform([preprocess_text(user_query)])

    # Compute cosine similarity
    similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

    # Get top N matches
    top_indices = similarities.argsort()[-top_n:][::-1]

    # Add similarity scores for frontend if needed
    top_matches = df.iloc[top_indices].copy()
    top_matches["score"] = similarities[top_indices]

    return top_matches
