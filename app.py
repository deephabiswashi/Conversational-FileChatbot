import werkzeug.urls
import urllib.parse
werkzeug.urls.url_quote = urllib.parse.quote

from flask import Flask, request, jsonify, render_template
import os
from utils import file_processing, langchain_integration, database

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

# Initialize database connection (if using MongoDB)
db_client = database.get_db_client()  # adjust connection settings in database.py

# Global variable to store the extracted document text
document_text = ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    global document_text
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    file_ext = os.path.splitext(file.filename)[1].lower()
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)
    
    # Process the file based on its type
    if file_ext == ".pdf":
        document_text = file_processing.process_pdf(file_path)
    elif file_ext in [".doc", ".docx"]:
        document_text = file_processing.process_docx(file_path)
    elif file_ext in [".xls", ".xlsx"]:
        document_text = file_processing.process_excel(file_path)
    else:
        return jsonify({"error": "Unsupported file format"}), 400

    return jsonify({"message": "File processed successfully", "text_snippet": document_text[:200]})

@app.route("/chat", methods=["POST"])
def chat():
    global document_text
    data = request.get_json()
    query = data.get("query", "")
    selected_model = data.get("model", "llama3.1:8b")
    
    if document_text == "":
        return jsonify({"error": "No document content available. Please upload a file first."}), 400

    # Combine the document text and user query as context for the LLM.
    prompt = f"Document Context:\n{document_text}\n\nUser Query: {query}\n\nAnswer:"
    
    # Initialize your custom LLM (integrated with LangChain) 
    llm = langchain_integration.OllamaLLM(model=selected_model)
    response = llm.generate(prompt)

    # Log conversation in MongoDB (if enabled)
    database.log_conversation(db_client, query, response)
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
