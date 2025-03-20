from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = """Citi’s Overdraft Protection policy allows customers to link eligible accounts to cover overdrafts.
Fees may apply, and coverage is subject to bank discretion. Customers can enable this feature through online banking."""
tokens = tokenizer.encode(text)

print(f"Token count: {len(tokens)}")

