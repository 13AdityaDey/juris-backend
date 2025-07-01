from utils import load_case_data
from tfidf_matcher import get_top_matches

def main():
    print("📚 Welcome to the Law Search Engine!")
    print("Type a brief description of your legal issue (or 'exit' to quit):\n")

    df = load_case_data()

    while True:
        user_input = input("🔍 Describe your case: ").strip()
        if user_input.lower() == 'exit':
            print("👋 Exiting Law Search Engine. Goodbye!")
            break

        matches = get_top_matches(user_input, df)

        if not matches.empty:
            print("\n✅ Top 5 related case(s):\n")
            for _, row in matches.iterrows():
                print(f"📂 Case ID: {row['case_id']}")
                print(f"🧾 Title: {row['title']}")
                print(f"📝 Summary: {row['summary']}")
                print(f"📜 Judgment: {row['judgment']}")
                print(f"📅 Date: {row['date']}")
                print(f"⚖️ Bench: {row['bench']}")
                print(f"🔗 Link: {row['link']}\n")
        else:
            print("❌ No similar cases found.\n")

if __name__ == "__main__":
    main()
