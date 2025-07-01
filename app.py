from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from tfidf_matcher import get_top_matches
from utils import load_case_data  # if you're using it

app = Flask(__name__)
CORS(app)

# Load data once at startup (replace if needed)
df = pd.read_csv("data\cases.csv")

@app.route("/")
def home():
    return "✅ Flask backend is running. Use POST /search to get case results."

@app.route("/search", methods=["GET", "POST"])
def search_cases():
    if request.method == "GET":
        return "👋 This endpoint only supports POST requests for legal search."

    try:
        data = request.get_json()
        query = data.get("query", "").strip()

        if not query:
            return jsonify({"error": "No query provided"}), 400

        matches = get_top_matches(query, df)

        results = []
        for _, row in matches.iterrows():
            results.append({
                "id": row.get("case_id", ""),  # was "Case ID"
                "title": row.get("title", ""),
                "summary": row.get("summary", ""),
                "judgment": row.get("judgment", ""),
                "decidedDate": row.get("date", ""),
                "bench": row.get("bench", ""),
                "link": row.get("link", "")
            })

        return jsonify({"results": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)
