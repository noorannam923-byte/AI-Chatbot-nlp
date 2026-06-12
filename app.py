from flask import Flask, render_template, request, jsonify
from nlp_engine import get_best_match
from faq_data import faqs

app = Flask(__name__)

# ─── Home Route ───────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


# ─── Chat API Route ───────────────────────────────────────────────────────────
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    result = get_best_match(user_message)

    return jsonify({
        "answer":           result["answer"],
        "matched_question": result["matched_question"],
        "confidence":       result["confidence"],
        "entities":         result["entities"]
    })


# ─── FAQ List Route (for sidebar) ─────────────────────────────────────────────
@app.route("/faqs")
def get_faqs():
    return jsonify([faq["question"] for faq in faqs])


# ─── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)