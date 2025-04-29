# gpt_integration.py
import openai

# Defina sua chave de API da OpenAI
openai.api_key = 'sua-api-key-aqui'

def gerar_resposta(prompt):
    # Solicita uma resposta do modelo GPT-3 ou GPT-4
    response = openai.Completion.create(
        engine="text-davinci-003",  # Ou use GPT-4 se disponível
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Exemplo de uso:
# resposta = gerar_resposta("Qual é o tempo hoje?")
# print(resposta)
