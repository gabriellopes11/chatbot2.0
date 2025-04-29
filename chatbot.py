# chatbot.py
from pln import processar_entrada
from gpt_integration import gerar_resposta
from treinamento_modelo import classificar_intencao

def responder_usuario(entrada):
    # Usar PLN para entender entidades
    entidades = processar_entrada(entrada)
    
    # Verificar se o GPT é a melhor opção (respostas mais naturais)
    if len(entidades) == 0:  # Caso o PLN não encontre entidades específicas
        resposta = gerar_resposta(entrada)
    else:
        # Se houver entidades, podemos usar um modelo de ML para classificar a intenção
        intencao = classificar_intencao(entrada)
        if intencao == "tempo":
            resposta = "Você quer saber a previsão do tempo?"
        elif intencao == "suporte":
            resposta = "Em que posso te ajudar com o suporte?"
        else:
            resposta = "Desculpe, não entendi sua intenção."
    
    return resposta

# Testando o chatbot
entrada = "Qual é o tempo hoje?"
print(responder_usuario(entrada))
