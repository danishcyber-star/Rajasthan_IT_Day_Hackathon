# from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
# import torch
#
#
# BART_PATH = 'model/bart-large'
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#
# bart_model = BartForConditionalGeneration.from_pretrained(BART_PATH)
# bart_tokenizer = BartTokenizer.from_pretrained(BART_PATH)
#
# bart_model.to(device)
# bart_model.eval()
#
# def bart_summarize(input_text, num_beams, num_words):
#     input_text = str(input_text)
#     input_text = ' '.join(input_text.split())
#     input_tokenized = bart_tokenizer.encode(input_text, return_tensors='pt').to(device)
#     summary_ids = bart_model.generate(input_tokenized,
#                                       num_beams=int(num_beams),
#                                       no_repeat_ngram_size=3,
#                                       length_penalty=2.0,
#                                       min_length=30,
#                                       max_length=int(num_words),
#                                       early_stopping=True)
#     output = [bart_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
#     return output[0]