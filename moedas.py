import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkcalendar import DateEntry
import pandas as pd
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


# Atualizar/Criar arquivo para guardar as informações
def atualizar_arq():
    dataInicial = selcDataInicial.get()
    anoInicial = dataInicial[-4:]
    mesInicial = dataInicial[3:5]
    diaInicial = dataInicial[:2]

    dataFinal = selcDataFinal.get()
    anoFinal = dataFinal[-4:]
    mesFinal = dataFinal[3:5]
    diaFinal = dataFinal[:2]

    # link = f'https://economia.awesomeapi.com.br/json/daily/USD-BRL?start_date={anoInicial}{mesInicial}{diaInicial}&end_date={anoFinal}{mesFinal}{diaFinal}'

    link = f"https://economia.awesomeapi.com.br/USD-BRL/10?start_date={anoInicial}{mesInicial}{diaInicial}&end_date={anoFinal}{mesFinal}{diaFinal}"

    reqCota = requests.get(link)
    cotacao = reqCota.json()
    # moeda = cotacao[0]['code']
    # valor = cotacao[0]['bid']

    print(cotacao, "\n\n", reqCota, "\n\n", link)


def create_moeda():
    if (respcheck.get() == 0):
        moeda2['state'] = 'normal'
        selcMoeda2['state'] = 'normal'
    else:
        moeda2['state'] = 'disabled'
        selcMoeda2['state'] = 'disabled'


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

respcheck = tk.IntVar()
todasounnao = tk.Checkbutton(text="Quero salvar os dados de todas as moedas.", variable=respcheck, command= create_moeda).grid(
    row=7, column=0, columnspan=7)

moeda2 = tk.Label(text="Escolha a moeda: ", font=("Roboto, 11"))
moeda2.grid(row=8, column=0, sticky="NSEW", pady=10)
selcMoeda2 = ttk.Combobox(values=lista, width=15)
selcMoeda2.grid(row=8, column=1, pady=10, sticky="NSEW")


dataInicial = tk.Label(text="Escolha a data: ", font=("Roboto, 11")).grid(
    row=9, column=0, sticky="NSEW", pady=(0, 5))
selcDataInicial = DateEntry(year=2022, locale='pt_br', width=15)
selcDataInicial.grid(row=9, column=1, sticky="EW")
selcDataFinal = DateEntry(year=2022, locale='pt_br', width=15)
selcDataFinal.grid(row=10, column=1, sticky="NSEW")

botaoSalvar = tk.Button(text="Salvar", font="Roboto, 13", width=15, height=2, command=atualizar_arq).grid(
    row=7, column=2, rowspan=3, padx=(50, 0), pady=(5, 0))

msgSelcErr = tk.Label(text="",
                      font="Roboto, 12", anchor="w", justify="left")
msgSelcErr.grid(row=11, column=2, sticky="NSEW", pady=(10, 40))

janela.mainloop()


# Fazer com que o sistema crie um arquivo novo com os dados
# Fazer com que o usuário possa escolher se quer todas as moedas ou só algumas
