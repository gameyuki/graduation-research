import torch
from peft import PeftModel
from transformers import BertJapaneseTokenizer, AutoModelForMaskedLM,AutoModelForCausalLM ,AutoTokenizer,AutoModel
from transformers import GPTNeoXJapaneseForCausalLM, GPTNeoXJapaneseTokenizer

model = GPTNeoXJapaneseForCausalLM.from_pretrained("abeja/gpt-neox-japanese-2.7b")
tokenizer_jp = GPTNeoXJapaneseTokenizer.from_pretrained("abeja/gpt-neox-japanese-2.7b")

def generate_text(raw_inputs):
    
    input_ids = tokenizer_jp(raw_inputs, return_tensors="pt").input_ids

    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.9,
        max_length=100,
    )
    gen_text = tokenizer_jp.batch_decode(gen_tokens, skip_special_tokens=True)[0]

    return gen_text