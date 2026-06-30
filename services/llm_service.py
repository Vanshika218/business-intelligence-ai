from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"""
❌ AI Service is temporarily unavailable.

Reason:
{str(e)}

Please try again after a few minutes.
"""