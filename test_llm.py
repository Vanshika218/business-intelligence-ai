from services.llm_service import generate_response


prompt = """
Say hello in one sentence.
"""

result = generate_response(prompt)

print(result)