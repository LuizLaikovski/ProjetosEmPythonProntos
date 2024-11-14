from tkinter import *
from tkinter import ttk
from random import randint

numeroParaAdivinhar = randint(1, 50)
tentativas_restantes = 5


janela = Tk()
janela.title("Jogo de Advinhação")
janela.geometry("600x400")
janela.config(bg="lightblue")

def ConferirNumero():
    global tentativas_restantes
    try:
        valor = int(num.get())
        if tentativas_restantes > 1:
            if valor < numeroParaAdivinhar:
                resposta.config(text="Maior")
            elif valor > numeroParaAdivinhar:
                resposta.config(text="Menor")
            else:
                resposta.config(text="Acertouuu!!!!!!")
                txt3.config(text="Parabéns! Você acertou o número!")
                botao.config(state="disabled")
                return  # Encerrar a função se o jogador acertou
            
            # Reduz uma tentativa e atualiza o texto com as tentativas restantes
            tentativas_restantes -= 1
            txt3.config(text=f"Você possui {tentativas_restantes} tentativas restantes.")
        else:
            resposta.config(text="Game Over! Suas tentativas acabaram.")
            txt3.config(text=f"O número era {numeroParaAdivinhar}. Tente novamente!")
            # Bloquear o botão após o fim das tentativas
            botao.config(state="disabled")
    except ValueError:
        resposta.config(text="Por favor, insira um número válido.", font="Arial", fg="blue", bg="lightblue")


txt1 = Label(janela, text="Seja bem vindo ao Jogo de Adivinhação!!", font=("Arial", 16), fg="blue", bg="lightblue")
txt1.grid(column=0, row=0, padx=100, pady=10)

txt2 = Label(janela, text="Digite um númeor entre 1 e 50.", font=("Arial", 13), fg="blue", bg="lightblue")
txt2.grid(column=0, row=1, padx=25, pady=10)

txt3 = Label(janela, text=f"Você possui apenas {tentativas_restantes} tentativas.", font=("Arial", 13), fg="blue", bg="lightblue")
txt3.grid(column=0, row=2, padx=25, pady=10)

num = StringVar()
numero = Entry(janela, textvariable=num)
numero.grid(column=0, row=3, padx=150, pady= 10)

botao = Button(janela, command=ConferirNumero, text="Enviar", font=("Arial"), fg="white", bg="red")
botao.grid(column=0, row=6, padx=100, pady=10)

resposta = Label(janela, text="", font="Arial", fg="blue", bg="lightblue")
resposta.grid(column=0, row=7, padx=100, pady=10)

janela.mainloop()