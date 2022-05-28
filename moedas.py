import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

lista = ['EUR', 'DOL', 'BRL']

janela.title('Cotação de moedas')

# janela.rowconfigure(0, weight= 1)

mainTitle = tk.Label(text= "Cotação de moedas", font= ("Roboto, 50"))
mainTitle.grid(row= 0, column= 1, sticky= "NSEW", padx= 50, pady= 50, columnspan= 7)

subTitle1 = tk.Label(text= "Cotação de uma única moeda", font= ("Roboto, 13")).grid(row= 1, column= 0, padx= 10, sticky= "NSEW")

moeda1 = tk.Label(text= "Escolha a moeda: ").grid(row= 2, column= 1, columnspan= 3, sticky= "NSEW")
selcmoeda = ttk.Combobox(values= lista, width= 30).grid(row= 3, column= 1, columnspan= 3)

data1 = tk.Label(text= "Escolha a data: ").grid(row= 2, column= 4, columnspan= 3, sticky= "NSEW")
selcdata = ttk.Combobox(values= lista, width= 30).grid(row= 3, column= 4, columnspan= 3)

subTitle2 = tk.Label(text= "Cotação de moedas + data", font= ("Roboto, 13")).grid(row= 7, column= 0, padx= 10, sticky= "NSEW")

janela.mainloop()