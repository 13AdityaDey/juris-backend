import pandas as pd
import os

def load_case_data(filename="cases.csv"):
    """
    Loads case data from the data folder.
    """
    filepath = os.path.join(os.path.dirname(__file__), "../data", filename)
    df = pd.read_csv(filepath)
    return df

def display_case(case):
    """
    Pretty prints a single case's data.
    """
    return (
        f"\n📂 Case ID: {case['case_id']}\n"
        f"🧾 Title: {case['title']}\n"
        f"📝 Summary: {case['summary']}\n"
        f"📜 Judgment: {case['judgment']}\n"
        f"📅 Date: {case.get('date', 'N/A')}\n"
        f"⚖️ Bench: {case.get('bench', 'N/A')}\n"
        f"🔗 Link: {case.get('link', 'N/A')}\n"
    )
