def is_end_keyword(user_input: str) -> bool:
    end_keywords = ["exit", "quit", "bye", "end"]
    return any(word in user_input.lower() for word in end_keywords)

def extract_candidate_info(session_state: dict) -> dict:
    return {
        "name": session_state.name,
        "email": session_state.email,
        "phone": session_state.phone,
        "experience": session_state.experience,
        "position": session_state.position,
        "location": session_state.location,
        "tech_stack": session_state.tech_stack,
    }
