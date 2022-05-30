from os import link
import tkinter as tk
from tkinter import ttk
from pyparsing import anyOpenTag
from tkcalendar import DateEntry
import requests

req = requests.get('https://economia.awesomeapi.com.br/json/all')
dicio = req.json()
lista = list(dicio.keys())


def pegar_cotacao():
    moeda = selcMoeda1.get()
    
    data = selcData1.get()
    ano = data[-4:]
    mes = data[3:5]
    dia = data[:2]
    
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    
    reqCota = requests.get(link)
    cotacao = reqCota.json()
    valor = cotacao[0]['bid']
    
    result1["text"] = f"Na data {data}, a moeda {moeda} custava R${valor}"

def selecionar():
    pass


def atualizar_arq():
    pass


janela = tk.Tk()

janela.title('Cotação de moedas')

# janela.rowconfigure(0, weight= 1)

# Título

mainTitle = tk.Label(text="Cotação de moedas", font=("Roboto, 50")).grid(
    row=0, column=0, sticky="NSEW", padx=50, pady=50, columnspan=7)

# Cotação de uma moeda

subTitle1 = tk.Label(text="Cotação de uma única moeda", anchor="w", padx=15, font=(
    "Roboto, 14")).grid(row=1, column=0, sticky="NSEW")

moeda1 = tk.Label(text="Escolha a moeda: ", font=("Roboto, 11")).grid(
    row=2, column=0, sticky="NSEW", pady=(10, 0))
selcMoeda1 = ttk.Combobox(values=lista)
selcMoeda1.grid(row=3, column=0, pady=(0, 10))

data1 = tk.Label(text="Escolha a data: ", font=("Roboto, 11")).grid(
    row=2, column=2, sticky="NSEW", pady=(10, 0))

selcData1 = DateEntry(year=2022, locale='pt_br', width=15)
selcData1.grid(row=3, column=2, pady=(0, 10))

botaoBusca = tk.Button(text="Buscar", command=pegar_cotacao, width=10, font="Roboto, 11").grid(
    column=0, row=4, columnspan=6, sticky="NS")

result1 = tk.Label(text="", font="Roboto, 11")
result1.grid(row=5, pady=(10, 20), column=0, columnspan=6, sticky="NSEW")

# Cotação de Várias Moedas

subTitle2 = tk.Label(text="Cotação de moedas + data", anchor="w", padx=15,
                     font=("Roboto, 14")).grid(row=6, column=0, sticky="NSEW")

selcArq = tk.Button(text="Selecione o arquivo", font="Roboto, 11",
                    command=selecionar).grid(row=7, column=0, pady=10, padx=(5, 0), sticky="NS")

msgSelcErr = tk.Label(text="Nenhum arquivo selecionado.", font="Roboto, 12",
                      anchor="e", justify="left").grid(row=7, column=2, columnspan=3, sticky="NSEW")

moeda2 = tk.Label(text="Escolha a moeda: ", font=("Roboto, 11")).grid(
    row=8, column=0, sticky="NSEW", pady=10)
selcMoeda2 = ttk.Combobox(values=lista, width=15)
selcMoeda2.grid(row=8, column=1, pady=10, sticky="NSEW")

botaoSalvar = tk.Button(text="Salvar", font="Roboto, 13", width=15, height=2, command=atualizar_arq).grid(
    row=7, column=2, rowspan=3, padx=(50, 0), pady=(5, 0))

data2 = tk.Label(text="Escolha a data: ", font=("Roboto, 11")).grid(
    row=9, column=0, sticky="NSEW", pady=(0, 50))
selcData2 = DateEntry(year=2022, locale='pt_br', width=15)
selcData2.grid(row=9, column=1, pady=(0, 50), sticky="NSEW")

janela.mainloop()
