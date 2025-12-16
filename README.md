# Q&A ChatBot using LangChain, Groq, and Streamlit

This project is a **Q&A ChatBot** built using **LangChain**, **Groq LLMs**, and **Streamlit**. It allows users to ask questions through a simple web interface and receive concise AI-generated answers.

The application supports multiple Groq-hosted large language models and provides configurable parameters like temperature and maximum tokens.

---

## Streamlit Deployment

**Link** : https://chatbot-by-sam.streamlit.app/

---

## 🚀 Features

* Interactive **Streamlit UI**
* Uses **Groq LLMs** via `langchain-groq`
* Supports multiple models:

  * `llama-3.3-70b-versatile`
  * `llama-3.1-8b-instant`
  * `qwen/qwen3-32b`
* Adjustable **temperature** and **max tokens**
* **LangSmith tracing** enabled for monitoring
* Secure API key handling via **.env file**

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Frontend UI
* **LangChain** – Prompt & chain management
* **Groq API** – Large Language Models
* **LangSmith** – Tracing & observability
* **python-dotenv** – Environment variable management

---

## 📁 Project Structure

```
├── app.py               # Main Streamlit application
├── .env                 # Environment variables (not committed)
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add:

```
LANGCHAIN_API_KEY=your_langsmith_api_key
```

> ⚠️ **Note:** The Groq API key is entered securely via the Streamlit sidebar and is not stored.

---

## 📦 Installation (Using Conda – Recommended)

```bash
conda create -n genai python=3.10 -y
conda activate genai
pip install streamlit langchain langchain-groq python-dotenv
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User enters a question in the Streamlit UI
2. The question is injected into a **ChatPromptTemplate**
3. The selected Groq LLM processes the prompt
4. Output is parsed using `StrOutputParser`
5. The response is displayed on the UI

LangChain Expression Language (LCEL) is used:

```
prompt | model | output_parser
```

---

## ⚙️ Configuration Options

| Parameter   | Description                     |
| ----------- | ------------------------------- |
| Model       | Choose Groq-hosted LLM          |
| Temperature | Controls randomness (0.0 – 1.0) |
| Max Tokens  | Limits response length          |

---

## 📊 LangSmith Integration

LangSmith tracing is enabled using:

```python
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = 'Q&A ChatBot'
```

This allows monitoring prompt execution, latency, and errors.

---

## 🧪 Example Use Cases

* Learning & education
* Quick AI-powered Q&A
* GenAI project demos

---

## 📌 Future Improvements

* Chat history / memory support
* Streaming responses
* Authentication
* UI enhancements
* RAG integration (PDF / Docs)

---

## 👨‍💻 Author

**Samarth Prajapati**
AI / ML & Generative AI Enthusiast

---

## ⭐ Acknowledgements

* Krish Naik – GenAI guidance
* LangChain team
* Groq platform

---

⭐ If you like this project, give it a star and feel free to contribute!
