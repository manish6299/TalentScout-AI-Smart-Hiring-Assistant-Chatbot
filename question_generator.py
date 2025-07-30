from chatbot import call_llm

def generate_tech_questions(tech_stack: str, num_questions=6, language="English"):
    system_prompt = {
        "role": "system",
        "content": (
            "You are a senior technical interviewer at a top-tier tech company. "
            "Your goal is to assess candidates applying for technical roles by generating structured, well-crafted, and skill-specific interview questions. "
            "You must adapt your questions to match the candidate's declared tech stack, ensuring depth, relevance, and increasing difficulty. "
            "Always respond in the language specified by the user."
        ),
    }

    user_prompt = {
        "role": "user",
        "content": (
            f"Language: {language}\n\n"
            f"Please generate {num_questions} technical interview questions for a candidate who is proficient in the following tech stack:\n"
            f"{tech_stack}\n\n"
            "🔹 Guidelines:\n"
            "- Include a mix of coding, design, and conceptual questions.\n"
            "- Target both practical implementation and theoretical understanding.\n"
            "- If multiple technologies are listed, generate questions that touch each 2 or 3.\n"
            "- Questions should progress from easy to medium to hard.\n\n"
            "🔹 Output Format:\n"
            "Question 1: [Technology Name] — [Question content]\n"
            "Note: [Why this question is relevant or what it tests]\n\n"
            "Repeat for each question.\n\n"
            f"Please provide the questions in {language}."
        ),
    }

    return call_llm([system_prompt, user_prompt])
