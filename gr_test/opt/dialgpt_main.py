from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name_1 = "microsoft/DialoGPT-large"
model_name_2 = "microsoft/DialoGPT-medium"

tokenizer_1 = AutoTokenizer.from_pretrained(model_name_1,padding_side='left')
tokenizer_2 = AutoTokenizer.from_pretrained(model_name_2,padding_side='left')

model_1 = AutoModelForCausalLM.from_pretrained(model_name_1)
model_2 = AutoModelForCausalLM.from_pretrained(model_name_2)

# 初期の入力テキスト
text = "Hello! How are you?"

for step in range(5):
    
    #モデル１の文字生成
    input_ids_1 = tokenizer_1.encode(text + tokenizer_1.eos_token, return_tensors="pt")
    bot_input_ids_1 = torch.cat([chat_history_ids_1, input_ids_1], dim=-1) if step > 0 else input_ids_1
    
    chat_history_ids_1 = model_1.generate(
        bot_input_ids_1,
        max_length=100,
        pad_token_id=tokenizer_1.eos_token_id,
    )
    output_1 = tokenizer_1.decode(chat_history_ids_1[:, bot_input_ids_1.shape[-1]:][0], skip_special_tokens=True)
    print(f"Model1: {output_1}")
    
     #モデル2の文字生成
    input_ids_2 = tokenizer_2.encode(output_1 + tokenizer_2.eos_token, return_tensors="pt")
    bot_input_ids_2 = torch.cat([chat_history_ids_2, input_ids_2], dim=-1) if step > 0 else input_ids_2
    
    chat_history_ids_2 = model_2.generate(
        bot_input_ids_2,
        max_length=100,
        pad_token_id=tokenizer_2.eos_token_id,
    )
    output_2 = tokenizer_2.decode(chat_history_ids_2[:, bot_input_ids_2.shape[-1]:][0], skip_special_tokens=True)
    print(f"Model2: {output_2}")
    
    # モデル1の次の入力はモデル2の出力
    text = output_2