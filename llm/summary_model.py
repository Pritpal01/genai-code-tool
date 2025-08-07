from transformers import pipeline

summarizer = pipeline("text2text-generation", model="Salesforce/codet5-small")

def summarize_code(code, level="simple"):
    level_prompts = {
        "simple": "Explain this code to a beginner:\n",
        "medium": "Explain this code to someone with some experience:\n",
        "expert": "Give an expert-level technical summary of this code:\n"
    }
    prompt = level_prompts.get(level, level_prompts["simple"]) + code
    result = summarizer(prompt, max_length=256, clean_up_tokenization_spaces=True)
    return result[0]["generated_text"]
