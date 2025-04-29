# treinamento_modelo.py
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Dados de exemplo de treinamento (exemplo simples)
dados = [
    ("Qual é o tempo hoje?", "tempo"),
    ("Preciso de ajuda com meu pedido", "suporte"),
    ("Qual é o horário de funcionamento?", "horario"),
    # Adicione mais exemplos conforme necessário
]

# Divida os dados em textos e rótulos
textos, labels = zip(*dados)

# Vetorização de texto (transformando texto em números)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(textos)

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

# Treinando o modelo
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

# Avaliar o modelo
print("Acurácia:", modelo.score(X_test, y_test))

# Função para classificar a intenção de uma nova entrada
def classificar_intencao(texto):
    texto_vetorizado = vectorizer.transform([texto])
    return modelo.predict(texto_vetorizado)[0]

# Exemplo de uso:
# intencao = classificar_intencao("Qual é o tempo hoje?")
# print(intencao)
