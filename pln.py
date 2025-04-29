# pln.py
import spacy

# Carregar o modelo em português do spaCy
nlp = spacy.load("pt_core_news_sm")

def processar_entrada(texto):
    # Processa o texto de entrada e extrai as entidades
    doc = nlp(texto)
    
    # Extrair as entidades encontradas
    entidades = [entidade.text for entidade in doc.ents]
    
    # Retorna as entidades encontradas
    return entidades

# Exemplo de uso:
# entidades = processar_entrada("Qual é o tempo hoje?")
# print(entidades)
