```markdown
<h1 align="center">Conversational Chatbot with Any Files</h1>
<p align="center">A vibrant and interactive chatbot that processes PDF, Word, and Excel documents and answers user queries using a locally hosted language model (Ollama) via LangChain and Flask, with optional MongoDB logging.</p>
---
## <div align="center">Overview</div>
This project enables users to upload documents (PDF, Word, Excel) and interact with a conversational chatbot that leverages a local LLM (via Ollama) for context-aware responses. The Flask backend handles file uploads, text extraction, and chat routing, while MongoDB (optional) stores conversation logs. The modern, vibrant UI includes features like a theme toggle and model selection.
---
## <div align="center">Features</div>
- **Document Upload:** Process PDF, Word, and Excel files.  
- **Interactive Chat:** Ask questions about the uploaded document and receive context-aware answers.  
- **Model Selection:** Choose from available LLM models (e.g., "llama3.1:8b").  
- **Theme Toggle:** Switch between light and dark modes.  
- **MongoDB Logging (Optional):** Store chat logs for future reference.  
- **Modern UI:** Clean and vibrant design with centered headings.
---
## <div align="center">Project Structure</div>
```
chatbot_project/
├── app.py                   # Main Flask application with routes (/ , /upload, /chat)
├── requirements.txt         # Python dependencies
├── .gitignore               # Git ignore rules
├── README.md                # Project documentation
├── templates/
│   └── index.html           # HTML template for the UI
├── static/
│   ├── css/
│   │   └── style.css        # CSS styling (modern, vibrant)
│   └── js/
│       └── script.js        # Client-side JavaScript for interactivity
├── uploads/                 # Folder for uploaded documents
└── utils/
    ├── file_processing.py   # Functions to extract text from PDF/Word/Excel files
    ├── langchain_integration.py  # Custom LLM wrapper for Ollama
    └── database.py          # MongoDB integration for conversation logging
```
---
## <div align="center">Installation & Setup</div>
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/your_username/Conversational-FileChatbot.git
   cd Conversational-FileChatbot
   ```
2. **Create and Activate a Virtual Environment:**  
   On macOS/Linux:
   ```bash
   python3 -m venv env3
   source env3/bin/activate
   ```  
   On Windows:
   ```bash
   python -m venv env3
   env3\Scripts\activate
   ```
3. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure MongoDB (Optional):**  
   Ensure MongoDB is running on `localhost:27017` for logging chat history. To disable logging, comment out the `database.log_conversation(...)` call in `app.py`.
5. **Start Ollama:**  
   Pull your desired model (e.g., `llama3.1:8b`) and run:
   ```bash
   ollama serve
   ```  
   Ensure the model is accessible at `http://127.0.0.1:11434/api/generate`.
6. **Run the Flask App:**  
   ```bash
   python app.py
   ```  
   Open [http://localhost:5000](http://localhost:5000) in your browser.
---
## <div align="center">Usage</div>
1. **Upload a Document:**  
   Use the file upload section to select a PDF, Word, or Excel file. The server extracts text for processing.
2. **Interact via Chat:**  
   Type your query in the chat box; the chatbot uses the document content and your query to generate a response.
3. **Toggle Theme:**  
   Click the "Toggle Theme" button to switch between light and dark modes.
4. **Select Model:**  
   Use the dropdown to choose the desired language model.
---
## <div align="center">Contributing</div>
Contributions are welcome! To contribute, please fork this repository, create a new branch for your feature or bug fix, commit your changes, and open a pull request with a detailed description of your improvements.
---
## <div align="center">License</div>
This project is licensed under the **MIT License**. See the LICENSE file for details.
<p align="center">Made with ❤️ by Deep</p>
