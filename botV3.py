import openai
openai.api_key = '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'

def enviar_mensagem(mensagem):
    resposta = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt=mensagem,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return resposta.choices[0].text.strip()


#Versão 3

mensagem_inicial = """
Você: Olá, como posso te ajudar?
Modelo: Eu sou um assistente virtual treinado para responder suas perguntas sobre produtos.
"""

mensagem_usuario = 'Qual é o seu nome? '
conversa_com_contexto = mensagem_inicial + 'Você: ' + mensagem_usuario

resposta = enviar_mensagem(conversa_com_contexto)
