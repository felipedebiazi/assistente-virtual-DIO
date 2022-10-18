print("testando")

from fileinput import close
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import wikipedia
import pyaudio
import webbrowser

#Função para chamar a resposta do sistema
def resposta_sistema(text):
    tts = gTTS(text=text, lang= 'pt-BR')
    filename = 'voice.mp3'
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)
    close()


#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        #print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        frase = ''
        
        try:
            
            #Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')
            
        #Se nao reconheceu o padrao de fala, exibe a mensagem
        except Exception as e:
            #resposta_sistema('Desculpe, eu nao entendi.')
            print("Não entendi")

    return frase
   
        
while True:
        
    print('Eu estou escutando...')
    text = ouvir_microfone().lower()
    
    if "navegador" in text:
        resposta_sistema('Abrindo navegador.')
        os.system("start Chrome.exe")

    elif "excel" in text:
        resposta_sistema('Abrindo Excel.')
        os.system("start Excel.exe")
        
    elif 'youtube' in text:
        resposta_sistema("Abrindo YouTube")
        url = f'https://www.youtube.com'
        webbrowser.get().open(url)
    
    elif "sair do programa" in text:
        resposta_sistema('Certo! Até a próxima.')
        exit()
        break
    
    #Retorna a frase pronunciada
    print("Você disse: " + text)
        
    