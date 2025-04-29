from transformers import pipeline
from huggingface_hub import login
import os

login(os.getenv("HF_TOKEN"))

pipe = pipeline("text-generation", model="gpt2")

def generate_answer(context, query):
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    result = pipe(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)[0]['generated_text']
    return result.split("Answer:")[-1].strip()