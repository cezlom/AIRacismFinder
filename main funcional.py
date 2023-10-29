import openai
from requirement import API_KEY
import tkinter as tk
from tkinter import messagebox
import json

openai.api_key = API_KEY
model_id = 'gpt-3.5-turbo'

def ler_arquivo(arquivo):
    with open(arquivo, 'r') as file:
        return file.read()

def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()  # Hides the root window
    messagebox.showwarning(title, message)
    root.destroy()

def send_message(message, arquivo, conversation=[]):
    texto = ler_arquivo(arquivo)
    
    conversation.append({"role": "user", "content": """Olá, ChatGPT! Recentemente, ouvi um comentário de um integrante do meu grupo e estou incerto sobre se ele continha elementos racistas. 
Peço que você extraia o máximo de sua capacidade analítica para avaliar o contexto da situação. 
Se detectar sinais de racismo, por favor, retorne um veredicto depois de analizar o contexto inteiro, veredito geral será a primeira coisa a ser mostrada no formato como {"resultado:true"} e me dê o motivo {"motivo:""escreva a justificativa aqui"}.
Caso contrário, simplesmente retorne "(resultado)" com o valor "false" e não precisa se justificar. Seja atendo à estrutura da decisão. Agradeço sua atenção e cuidado com essa situação sensível."""})
    conversation.append({"role": "system", "content": "Por favor, forneça o comentário completo, e eu farei o meu melhor para analisar a situação e fornecer um veredicto apropriado e sempre na estrutura mencionada - {""resultado:true;motivo:"'motivo da conversa ser racista e adicione conscientização'"} para verdadeiro e {""motivo:false""} para falso. A RESPOSTA DEVE SEMPRE ESTAR DENTRO DESTA ESTRUTURA, NUNCA SAIA DELA POR FAVOR!"})
    
    conversation.append({"role": "user", "content": texto})

    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )

    conversation.append({"role": "assistant", "content": response.choices[0].message.content})
    return conversation

def analyze_response(response):
    try:
        # Extract the result and reason from the response
        parsed_response = json.loads(response.split('\n')[0])
        result = parsed_response.get("resultado", False)
        reason = parsed_response.get("motivo", "")
        return result, reason
    except json.JSONDecodeError:
        return False, ""

def main():
    conversation = []
    user_input = "analisando este contexto esta conversa foi racista?"
    conversation = send_message(user_input, 'contexto.txt', conversation)
    assistant_response = conversation[-1]['content'].strip()
    
    # Analyze the assistant's response
    result, reason = analyze_response(assistant_response)
    
    if result:
        show_popup("CUIDADO - Você pode estar cometendo um erro", reason)
    else:
        print(f'Assistant: {assistant_response}\n')

if __name__ == "__main__":
    main()
