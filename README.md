# 🤖 FAQ Chatbot — NLP-Powered Question Answering

> An intelligent FAQ assistant built with **Python**, **Flask**, **NLTK**, **spaCy**, and **scikit-learn**.  
> Matches user questions to the best answer using **TF-IDF vectorization** and **cosine similarity**.

---

## 📸 Preview

> Run the app and open `http://127.0.0.1:5000` to see the chatbot in action.

---

## ✨ Features

- 🧠 Full NLP pipeline — lowercase, clean, tokenize, remove stopwords, lemmatize
- 📐 TF-IDF vectorization + cosine similarity for intelligent question matching
- 🏷️ Named Entity Recognition (NER) via spaCy
- 📊 Confidence score badge with every response (High / Medium / Low)
- 📋 Sidebar with clickable FAQ list for quick access
- ⌨️ Typing indicator and timestamped messages
- 🗑️ Clear chat button
- 📱 Fully responsive — works on mobile too
- ➕ Easy to extend — just add entries to `faq_data.py`

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Flask | Web framework & REST API |
| NLTK | Tokenization, stopword removal, lemmatization |
| spaCy | Named Entity Recognition (NER) |
| scikit-learn | TF-IDF vectorizer & cosine similarity |
| NumPy | Matrix operations |
| HTML / CSS / JS | Frontend UI |

---

## 📁 Project Structure

```
faq_chatbot/
├── venv/                  # Virtual environment (do not commit)
├── app.py                 # Flask backend & routes
├── nlp_engine.py          # NLP preprocessing & matching logic
├── faq_data.py            # FAQ questions & answers
├── templates/
│   └── index.html         # Chatbot UI
└── static/
    └── style.css          # Styles
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/faq_chatbot.git
cd faq_chatbot
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask nltk spacy scikit-learn numpy
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab')"
```

### 4. Create folder structure

```bash
mkdir templates static
```

### 5. Place the files

| File | Location |
|---|---|
| `faq_data.py` | `faq_chatbot/` |
| `nlp_engine.py` | `faq_chatbot/` |
| `app.py` | `faq_chatbot/` |
| `index.html` | `faq_chatbot/templates/` |
| `style.css` | `faq_chatbot/static/` |

### 6. Run the application

```bash
python app.py
```

### 7. Open in browser

```
http://127.0.0.1:5000
```

---

## 🧠 NLP Pipeline

Every user question goes through this pipeline before being matched:

```
User Input
    │
    ▼
Lowercase          →  "How do I RESET my Password?" → "how do i reset my password?"
    │
    ▼
Clean (regex)      →  remove special characters & digits
    │
    ▼
Tokenize (NLTK)    →  ["how", "do", "i", "reset", "my", "password"]
    │
    ▼
Remove Stopwords   →  ["reset", "password"]
    │
    ▼
Lemmatize          →  ["reset", "password"]
    │
    ▼
TF-IDF Vectorize   →  numerical vector representation
    │
    ▼
Cosine Similarity  →  compare against all FAQ vectors
    │
    ▼
Best Match Answer  →  returned with confidence score
```

---

## 🗂️ API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Serves the chatbot UI |
| `/chat` | POST | Accepts `{ "message": "..." }` → returns matched answer + confidence |
| `/faqs` | GET | Returns all FAQ questions (used to populate sidebar) |

### Example `/chat` request

```json
POST /chat
Content-Type: application/json

{
  "message": "How do I track my order?"
}
```

### Example response

```json
{
  "answer": "Once your order is shipped, you will receive a tracking number via email...",
  "matched_question": "How can I track my order?",
  "confidence": 87.3,
  "entities": []
}
```

---

## ➕ How to Add Your Own FAQs

Open `faq_data.py` and add a new entry to the `faqs` list:

```python
{
    "question": "Your question here?",
    "answer": "Your detailed answer here."
},
```

Save and restart the server — no other changes needed.

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError` | Make sure venv is activated and `pip install` was run |
| spaCy model not found | Run `python -m spacy download en_core_web_sm` |
| NLTK data missing | Run the NLTK download command from Step 3 |
| Port 5000 already in use | Change port in `app.py`: `app.run(port=5001)` |
| No answer / fallback every time | Lower threshold in `nlp_engine.py` (default: `0.15`) |

---

## 📦 Requirements

```
flask
nltk
spacy
scikit-learn
numpy
```

> You can generate a `requirements.txt` with:
> ```bash
> pip freeze > requirements.txt
> ```

---

## 🙈 .gitignore

Create a `.gitignore` file in the root with the following content to avoid committing unnecessary files:

```
venv/
__pycache__/
*.pyc
*.pyo
.env
.DS_Store
```

---

## 📄 License

This project is open-source and free to use for educational and personal projects.

---

<p align="center">Built with ❤️ using Python · Flask · NLTK · spaCy · scikit-learn</p>
