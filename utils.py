from database import save_candidate_to_db
import json
def save_candidate(data: dict):
    """
    Save candidate data to the SQLite database.
    """
    save_candidate_to_db(data)

def personalize_response(field: str, value: str, sentiment: str = "neutral") -> str:
    """
    Generate a personalized response based on input type and sentiment.
    """
    field = field.lower()

    if field == "name":
        return f"👋 Nice to meet you, **{value}**!"
    elif field == "experience":
        return f"🛠️ {value} years of experience—great! That helps us tailor questions to your level."
    elif field == "position":
        return f"🎯 {value} sounds exciting. Let’s align the questions accordingly."
    elif field == "tech_stack":
        return f"💻 Understood: **{value}**. We'll craft the technical questions around this stack."
    elif sentiment == "positive":
        return "😊 Glad to hear that!"
    elif sentiment == "negative":
        return "😟 Thanks for sharing. We’ll make this process easier."
    else:
        return f"✔️ Got it: **{value}**"
