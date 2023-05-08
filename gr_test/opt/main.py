from model import generate_text
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_text(prompt, model_name='gpt2', max_length=50, temperature=1.0):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, temperature=temperature)

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

if __name__ == "__main__":
  generated_sentence = generate_text(input("文字を入力してください。"))
  print(generated_sentence)