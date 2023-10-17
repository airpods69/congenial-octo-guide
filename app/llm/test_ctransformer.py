from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("marella/gpt-2-ggml")
text = llm("AI will take over the world and ", stream=True)

for word in text:
    print(word, end="", flush=True)
