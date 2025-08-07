from transformers import pipeline

explainer = pipeline("text2text-generation", model="bigcode/starcoderbase")

def explain_error(error_text):
    prompt = f"""Explain this error and how to fix it in simple steps:\n\n{error_text}"""
    result = explainer(prompt, max_length=256)
    return result[0]["generated_text"]
