# 🤖 TalentScout AI – Hiring Assistant Chatbot

**TalentScout AI** is an interactive, multilingual Streamlit-based chatbot that automates the initial technical screening process of job candidates. It collects candidate details, analyzes sentiment, and generates customized technical interview questions based on the user's tech stack—all in real-time.

## 🚀 Project Overview

TalentScout AI serves as a virtual recruiter, streamlining early-stage hiring by:

- Gathering candidate information step-by-step (name, email, experience, etc.)
- Analyzing user sentiment during input to personalize feedback
- Generating tailored technical interview questions based on the tech stack
- Supporting multiple languages (English, Spanish, French, German, Hindi)
- Providing downloadable interview content and candidate details

## 🛠️ Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/talent-scout-ai.git
cd talent-scout-ai
```

### 2. Create & Activate Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Application

```bash
streamlit run app.py
```

## 🧑‍💻 Usage Guide

1. Select your preferred **language**
2. Follow the chatbot's prompts to enter your **personal and technical information**
3. Receive **custom technical questions** based on your tech stack
4. Download your **candidate profile (JSON)** and **question set (TXT)**

> **Note:** Refresh the page to restart a session anytime.

## ⚙️ Technical Details

### Main Libraries Used

- **`streamlit`**: UI and session control
- **`textblob`**: Sentiment analysis via Hugging Face
- **`requests`**: For LLM API calls
- **`sqlite3`**: Persistent storage of candidate info
- **`dotenv`**: Managing API keys

### LLM Used

- **`llama3-8b-8192`** via GROQ API (for question generation and personalization)

### Architecture Highlights

- Modular design (`chatbot.py`, `question_generator.py`, etc.)
- Session state-driven flow control
- Real-time sentiment-aware responses
- Persistent candidate database (`SQLite`)

## 🧠 Prompt Design

### Prompt Strategy

- **System Prompt**: Instructs the LLM to act as a senior technical interviewer
- **User Prompt**: Clearly defines tech stack, question count, desired structure, and language

### Output Format Enforced

```
Question 1: [Technology] — [Question]
Note: [Why it's important]
```

Ensures consistency and human-readability across languages.

## 🧩 Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| **Sentiment Analysis Latency** | Used Hugging Face Transformers locally to avoid API lag |
| **Multilingual Output from LLM** | Explicit language instruction in prompt & dynamic language selection |
| **Session Resets** | Utilized `st.session_state` to persist step-by-step data |
| **Database Integration** | Lightweight `SQLite` solution for easy candidate data storage |
| **Prompt Complexity** | Iterative refinement to balance clarity, output quality, and model cost |

## 📦 Outputs

- **`technical_questions.txt`**: Downloadable set of customized questions
- **`candidate_info.json`**: Exported candidate profile
- **Local `SQLite` DB**: Stores all entries persistently

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit>=1.28.0
textblob
torch>=1.12.0
requests>=2.28.0
python-dotenv>=0.19.0
```

## 🚀 Getting Started

1. **Get GROQ API Key**: Sign up at [GROQ Console](https://console.groq.com/) and obtain your API key
2. **Follow installation steps** above
3. **Run the application** and start screening candidates!

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [GROQ API](https://groq.com/)
- Sentiment analysis via [Hugging Face Transformers](https://huggingface.co/transformers/)

---

**Happy Hiring! 🎯**
link  (https://talentscout-ai-smart-hiring-assistant-chatbot-6pkeprweitfkqbva.streamlit.app/)
