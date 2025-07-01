import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    # 1. Basic: nouns & proper nouns
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop:
            keywords.append(token.lemma_.lower())

    # 2. Named entities like laws, numbers, people
    for ent in doc.ents:
        if ent.label_ in ['LAW', 'ORDINAL', 'CARDINAL', 'PERSON']:
            keywords.append(ent.text.lower())

    # 3. Custom: Match things like "Section 302", "Article 14", etc.
    pattern = re.compile(r'\b(section|article)\s+\d+\w*\b', re.IGNORECASE)
    matches = pattern.findall(text)
    for match in re.finditer(pattern, text):
        keywords.append(match.group(0).lower())

    return list(set(keywords))
