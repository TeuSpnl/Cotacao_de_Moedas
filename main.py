import tkinter as tk
from tkinter import ttk

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
    msg_log = tk.Label(text= "", width= 35, height= 3)
    msg_log.grid(sticky="EW", column= 0, row= 5)
    
    if (login.get() == "admin" and password.get() == "admin"):
        msg_log["text"] = "Usuário logado!"
    else:
        msg_log["text"] = "Usuário ou senha incorretos."

botaoLogin = tk.Button(text = "Entrar", command = entrar)
botaoLogin.grid(row = 6)

janela.mainloop()