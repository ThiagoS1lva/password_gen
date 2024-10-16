from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn.functional as F

# Carregar o tokenizador e o modelo pré-treinado para classificação de sentimentos
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Texto de exemplo
texto = "Não deu um mês que recebi o produto e a case parou de carregar. Não consegui obter suporte do fabricante e muito menos do vendedor."

# Tokenizar o texto
inputs = tokenizer(texto, return_tensors='pt', max_length=512, truncation=True, padding=True)
# Fazer a previsão
with torch.no_grad():
    outputs = model(**inputs)

# Obter as previsões
logits = outputs.logits
probabilidades = F.softmax(logits, dim=-1)

# Ver as probabilidades de cada classe
print(probabilidades)

# Identificar a classe com a maior probabilidade
predicao = torch.argmax(probabilidades).item()
print(f"A classe prevista é: {predicao}")
