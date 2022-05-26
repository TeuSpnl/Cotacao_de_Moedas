import tkinter as tk
from turtle import width

janela = tk.Tk()
janela.title("Cylinder")

janela.rowconfigure([0, 1, 2, 3], weight = 1)
janela.columnconfigure(0, weight = 1)

mensagem = tk.Label(text = "Login", width = 35, height = 3)
mensagem.grid(sticky='NSEW')

login = tk.Entry()
login.grid()

mensagem1 = tk.Label(text = "Senha", width = 35, height = 3)
mensagem1.grid(sticky='NSEW')

password = tk.Entry()
password.grid()

def entrar():
    if (login.get() == "admin" and password.get() == "admin"):
        print("Você está logado!")
    else:
        print("Usuário ou senha incorretos.")

botaoLogin = tk.Button(text = "Entrar", command = entrar)
botaoLogin.grid(row = 5)

janela.mainloop()