from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_top_matches(user_input, df, top_n=5):
    corpus = df['summary'].astype(str).tolist() + [user_input]

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Compute similarity of last entry (user input) with all summaries
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # Get top N indices
    top_indices = similarities.argsort()[-top_n:][::-1]

    # Get corresponding DataFrame rows
    matched_df = df.iloc[top_indices].copy()
    matched_df['similarity_score'] = similarities[top_indices]
    return matched_df.reset_index(drop=True)
