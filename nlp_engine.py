import re
import nltk
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from faq_data import faqs

# ─── Load NLP tools ───────────────────────────────────────────────────────────
nlp = spacy.load("en_core_web_sm")
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# ─── Text Preprocessing ───────────────────────────────────────────────────────
def preprocess(text):
    """
    Full NLP pipeline:
    1. Lowercase
    2. Remove special characters & digits
    3. Tokenize using NLTK
    4. Remove stopwords
    5. Lemmatize using WordNetLemmatizer
    6. Rejoin cleaned tokens
    """
    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove special characters and digits
    text = re.sub(r"[^a-z\s]", "", text)

    # Step 3: Tokenize
    tokens = nltk.word_tokenize(text)

    # Step 4: Remove stopwords
    tokens = [t for t in tokens if t not in stop_words]

    # Step 5: Lemmatize
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    # Step 6: Rejoin
    return " ".join(tokens)


# ─── Named Entity Recognition (bonus spaCy feature) ──────────────────────────
def extract_entities(text):
    """Extract named entities from user input using spaCy."""
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]


# ─── Build TF-IDF Matrix from FAQ questions ───────────────────────────────────
faq_questions = [faq["question"] for faq in faqs]
faq_answers   = [faq["answer"]   for faq in faqs]

# Preprocess all FAQ questions
processed_questions = [preprocess(q) for q in faq_questions]

# Fit TF-IDF vectorizer on the FAQ corpus
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_questions)


# ─── Match user query to best FAQ ─────────────────────────────────────────────
def get_best_match(user_query, threshold=0.15):
    """
    1. Preprocess user query
    2. Transform to TF-IDF vector
    3. Compute cosine similarity against all FAQ vectors
    4. Return best match if above threshold, else fallback message
    """
    processed_query = preprocess(user_query)

    if not processed_query.strip():
        return {
            "answer": "Please type a valid question so I can help you.",
            "matched_question": None,
            "confidence": 0.0,
            "entities": []
        }

    # Vectorize the user query
    query_vector = vectorizer.transform([processed_query])

    # Compute cosine similarity
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Find the best match index
    best_idx   = int(np.argmax(similarities))
    best_score = float(similarities[best_idx])

    # Extract entities from original query (spaCy)
    entities = extract_entities(user_query)

    if best_score >= threshold:
        return {
            "answer": faq_answers[best_idx],
            "matched_question": faq_questions[best_idx],
            "confidence": round(best_score * 100, 1),
            "entities": entities
        }
    else:
        return {
            "answer": (
                "I'm sorry, I don't have a specific answer for that. "
                "Please contact our support team at support@example.com "
                "or call 1-800-123-4567 for further assistance."
            ),
            "matched_question": None,
            "confidence": round(best_score * 100, 1),
            "entities": entities
        }