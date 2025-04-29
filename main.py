from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # To handle CORS if the frontend is on a different port
from retriever import train_embeddings, retrieve_relevant_context
from generator import generate_answer
from chat_history import store_chat, get_history

app = Flask(__name__)

# Enable CORS for all routes (allow cross-origin requests)
CORS(app)

@app.route("/")
def index():
    """Route to render the main HTML page."""
    return render_template('index.html')

@app.route("/train", methods=["POST"])
def train():
    """Route to train embeddings using the data."""
    try:
        train_embeddings()
        return jsonify({"status": "Training complete"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chat", methods=["POST"])
def chat():
    """Route to process a user's query and return a response."""
    data = request.json
    query = data.get("query")
    
    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Retrieve relevant context from the database
    context = retrieve_relevant_context(query)
    
    # If context is not found, return a fallback message
    if context.startswith("Knowledge base"):
        return jsonify({"response": context})

    # Generate an answer using the retrieved context
    answer = generate_answer(context, query)
    
    # Store the chat history in the database
    store_chat(query, answer)
    
    # Return the answer as a response
    return jsonify({"response": answer})

@app.route("/history", methods=["GET"])
def history():
    """Route to fetch all previous chat history."""
    try:
        return jsonify(get_history()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
