from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

torch.set_default_device("cuda")



def main():
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    text = "generate a random number."
    encoded_input = tokenizer(text, return_tensors='pt')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    output = model.generate(**encoded_input, max_new_tokens=20)
    decoded = tokenizer.decode(output[0])
    print(decoded)


def main2():
    tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2-xl")
    model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2-xl")

    text = 'Paraphrase this sentence: "The expected property price is higher than average for this type of property due to the large lot size, but is reduced slightly due to poor condition of the single bathroom"'
    inputs = tokenizer(text, return_tensors="pt")

    outputs = model.generate(**inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))


def main3():
    model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)
    text = 'Instruct: Paraphrase this sentence: "The expected property price is higher than average for this type of property due to the large lot size, but is reduced slightly due to poor condition of the single bathroom"\nOutput:'
    inputs = tokenizer(text, return_tensors="pt", return_attention_mask=False)

    outputs = model.generate(**inputs, max_length=200, pad_token_id=tokenizer.eos_token_id)
    text = tokenizer.batch_decode(outputs)[0]
    print(text)


if __name__ == '__main__':
    main3()
