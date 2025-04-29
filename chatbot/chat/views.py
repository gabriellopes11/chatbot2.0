from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse  # Adicione essa linha
from .models import ChatMessage  # Importação do modelo ChatMessage
import random

def chatbot_response(request):
    user_message = request.GET.get('message', '')

    # Respostas baseadas na mensagem do usuário
    if 'olá' in user_message.lower():
        bot_response = random.choice(["Olá! Como posso ajudar você hoje?", "Oi! Em que posso te ajudar?"])
    elif 'tchau' in user_message.lower():
        bot_response = random.choice(["Tchau! Até logo!", "Foi um prazer conversar com você!"])
    elif 'como você está' in user_message.lower():
        bot_response = random.choice([
            "Eu estou bem, obrigado por perguntar! E você?",
            "Estou ótimo! Como você está?",
            "Estou muito bem, obrigado! E você?"
        ])
    elif 'qual é o seu nome' in user_message.lower():
        bot_response = "Eu sou o Chatbot, prazer em te conhecer!"
    else:
        bot_response = "Desculpe, não entendi sua mensagem. Pode tentar novamente?"

    # Salvar a conversa no banco de dados
    ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)

    return JsonResponse({'response': bot_response})

def home(request):
    # Recupera as últimas 20 mensagens, em ordem crescente
    history = ChatMessage.objects.order_by('-timestamp')[:20][::-1]
    return render(request, 'chat/home.html', {'history': history})
