# import torch
# from transformers import T5Tokenizer, AutoModelForCausalLM

# # トークナイザーとモデルのロード
# tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
# model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")

# # GPU使用（※GPUを使用しない場合、文章生成に時間がかかります）
# if torch.cuda.is_available():
#     model = model.to("cuda")
    

# # # 初めの文章
# prompt = "むかしむかしあるところにおじいさんとおばあさんがいました。おじいさんは"
# # # 生成する文章の数
# num = 1 

# input_ids = tokenizer.encode(prompt, return_tensors="pt",add_special_tokens=False).to("cuda")
# with torch.no_grad():
#     output = model.generate(
#         input_ids,
#         max_length=100, # 最長の文章長
#         min_length=100, # 最短の文章長
#         do_sample=True,
#         top_k=500, # 上位{top_k}個の文章を保持
#         top_p=0.95, # 上位{top_p}%の単語から選択する。例）上位95%の単語から選んでくる
#         pad_token_id=tokenizer.pad_token_id,
#         bos_token_id=tokenizer.bos_token_id,
#         eos_token_id=tokenizer.eos_token_id,
#         bad_words_ids=[[tokenizer.unk_token_id]],
#         num_return_sequences=num # 生成する文章の数
#     )
# decoded = tokenizer.batch_decode(output,skip_special_tokens=True)
# for i in range(num):
#   print(decoded[i])

# from transformers import T5Tokenizer, AutoModelForCausalLM


# tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
# tokenizer.do_lower_case = True


from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt2-small", use_fast=False)
tokenizer.do_lower_case = True  # due to some bug of tokenizer config loading

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# 学習したモデルを読み込む
#model = AutoModelForCausalLM.from_pretrained("output/")
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-small")
model.to(device)
model.eval()

# 初めの文章
prompt = "こんにちは！昨日何食べた？"
# 生成する文章の数
num = 1 

input_ids = tokenizer.encode(prompt, return_tensors="pt",add_special_tokens=False).to(device)

with torch.no_grad():
    output = model.generate(
        input_ids,
        max_length=100, # 最長の文章長
        min_length=100, # 最短の文章長
        do_sample=True,
        top_k=500, # 上位{top_k}個の文章を保持
        top_p=0.95, # 上位{top_p}%の単語から選択する。例）上位95%の単語から選んでくる
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        bad_words_ids=[[tokenizer.unk_token_id]],
        num_return_sequences=num # 生成する文章の数
    )

decoded = tokenizer.batch_decode(output,skip_special_tokens=True)

for i in range(num):
  print(decoded[i])