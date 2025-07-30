import streamlit as st
import json
from chatbot import get_greeting, get_fallback, get_closing
from question_generator import generate_tech_questions
from sentiment import analyze_sentiment
from shared import (
    is_end_keyword,
    extract_candidate_info,
)
from database import save_candidate_to_db, init_db
from utils import (personalize_response, save_candidate)

# 🔧 Initialize DB on app start
init_db() 
# Page config and title
st.set_page_config(page_title="TalentScout AI", page_icon="🤖", layout="centered")
st.markdown("<h1 style='text-align: center;'>🤖 TalentScout Hiring Assistant</h1>", unsafe_allow_html=True)

# Language selection
language = st.selectbox("🌐 Select your language", ["English", "Spanish", "French", "German", "Hindi"])

# Session initialization
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.chat_log = []
    st.session_state.complete = False

steps = ["name", "email", "phone", "experience", "position", "location", "tech_stack"]
placeholders = {
    "name": "Your full name",
    "email": "you@example.com",
    "phone": "Phone number",
    "experience": "Years of experience",
    "position": "Desired position(s)",
    "location": "Current location",
    "tech_stack": "List of programming languages, frameworks, databases, etc."
}

# Greeting
if st.session_state.step == 0:
    st.markdown(get_greeting())
    st.session_state.step += 1

# Chat input loop
if not st.session_state.complete:
    current_step = steps[st.session_state.step - 1]
    input_key = f"input_{current_step}"
    user_input = st.text_input(f"Enter {current_step} ({placeholders[current_step]})", key=input_key)

    if user_input:
        sentiment = analyze_sentiment(user_input)
        personalized_msg = personalize_response(current_step, user_input, sentiment)
        st.markdown(personalized_msg)

        if is_end_keyword(user_input):
            st.session_state.complete = True
            st.markdown(get_closing())
        else:
            st.session_state[current_step] = user_input
            st.session_state.step += 1

        if st.session_state.step > len(steps):
            st.session_state.complete = True

            # Extract + Save Candidate Info
            candidate_data = extract_candidate_info(st.session_state)
            save_candidate(candidate_data)

            # Display Questions
            st.subheader("🎯 Generated Technical Questions")
            questions = generate_tech_questions(candidate_data["tech_stack"], language=language)
            st.markdown(questions)

            # --- Download Buttons ---
            st.subheader("⬇️ Download Your Results")

            # Questions as TXT
            st.download_button(
                label="📄 Download Questions (.txt)",
                data=questions,
                file_name="technical_questions.txt",
                mime="text/plain"
            )

            # Candidate Info as JSON
            candidate_json = json.dumps(candidate_data, indent=2)
            st.download_button(
                label="🗂️ Download Candidate Info (.json)",
                data=candidate_json,
                file_name="candidate_info.json",
                mime="application/json"
            )

            st.markdown(get_closing())

else:
    st.success("✅ Session completed. Refresh the page to restart.")
