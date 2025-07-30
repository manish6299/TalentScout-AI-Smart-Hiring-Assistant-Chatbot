import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def call_llm(messages):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # ✅ Supported model
        "messages": messages,
        "temperature": 0.6
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        return f"[Error calling LLM] {str(e)}"

def get_greeting():
    return "👋 Hi! I'm TalentScout's assistant. I'm here to help with your screening. Let's begin!"

def get_fallback():
    return "Sorry, I didn't get that. Could you rephrase?"

def get_closing():
    return "Thanks! Your info is recorded. We'll be in touch shortly. 👋"
