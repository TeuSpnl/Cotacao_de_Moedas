import tkinter as tk
from tkinter import ANCHOR, ttk
from tkinter.filedialog import askopenfilename
from tkcalendar import DateEntry
from datetime import date, datetime
import pandas as pd
import requests
import numpy as np

req = requests.get('https://economia.awesomeapi.com.br/json/all')
dicio = req.json()
lista = list(dicio.keys())


def pegar_cotacao():
    moeda = selcMoeda1.get()

    data = selcData1.get()
    ano = data[-4:]
    mes = data[3:5]
    dia = data[:2]

    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL? \
                start_date={ano}{mes}{dia}& \
                end_date={ano}{mes}{dia}'

    reqCota = requests.get(link)
    cotacao = reqCota.json()
    valor = cotacao[0]['bid']

    result1["text"] = f"Na data {data}, a moeda {moeda} custava R${valor}"


#Seleciona arquivo
def selecionar():
    pass
    caminhoGot = askopenfilename(title= "Selecione o arquivo xls")
    caminho.set(caminhoGot)
    if (caminhoGot):
        msgSelcErr["text"] = f"{caminhoGot}"

# Habilita/desabilita a caixa de seleção de moedas
def all_or_not():
    if (respcheck.get() == 0):
        moeda2['state'] = 'normal'
        selcMoeda2['state'] = 'normal'
    else:
        moeda2['state'] = 'disabled'
        selcMoeda2['state'] = 'disabled'

def adicionar_moeda():
    entry = selcMoeda2.get()
    
    if entry in moedas:
        msgSelcErr["text"] = f"A moeda {entry} já foi inserida na lista."
    else:
        moedas.append(entry)
        msgSelcErr["text"] = f"Moeda {entry} foi inserida na lista."

# Atualizar/Criar arquivo para guardar as informações
def atualizar_arq():
    todas = respcheck.get()
    
    dataInicial = selcDataInicial.get()
    anoInicial = dataInicial[-4:]
    mesInicial = dataInicial[3:5]
    diaInicial = dataInicial[:2]

    dataFinal = selcDataFinal.get()
    anoFinal = dataFinal[-4:]
    mesFinal = dataFinal[3:5]
    diaFinal = dataFinal[:2]
    
    reqs = []
    
    final = date(int(anoFinal), int(mesFinal), int(diaFinal))
    inicial = date(int(anoInicial), int(mesInicial), int(diaInicial))
    dias = abs(final - inicial).days
    
    if (todas == 1):
        for moeda in lista:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/{dias}?" \
                        f"start_date={anoInicial}{mesInicial}{diaInicial}&" \
                        f"end_date={anoFinal}{mesFinal}{diaFinal}"
            
            reqCota = requests.get(link)
            cotacoes = reqCota.json()
            print("\n", cotacoes)
            reqs.append([cotacoes[0]['code'], cotacoes[0]['bid']])
            
            print(link)
        
    else:
        for moeda in moedas:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/{dias}?" \
                        f"start_date={anoInicial}{mesInicial}{diaInicial}&" \
                        f"end_date={anoFinal}{mesFinal}{diaFinal}"
            
            reqCota = requests.get(link)
            cotacoes = reqCota.json()
            print("\n", cotacoes)
            
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.timestamp(timestamp)
                data = datetime.strftime('%d/%n/%Y')
            
            print(link)
            
    print("\n", reqs)
            
    try:
        # Editar o arquivo que já existe
        
        pass
    except:
        # Cria um novo arquivo
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


moeda1 = tk.Label(text="Escolha as moedas: ", font=("Roboto, 11")).grid(
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
result1.grid(row=5, pady=(10, 10), column=0, columnspan=6, sticky="NSEW")

# Cotação de Várias Moedas

subTitle2 = tk.Label(text="Cotação de moedas + data", anchor="w", padx=15,
                     font=("Roboto, 14")).grid(row=6, column=0, sticky="NSEW")


selcArq = tk.Button(text="Selecione o arquivo", font="Roboto, 11", command=selecionar)
selcArq.grid(row=7, column=0, pady=10, padx=(5, 0), sticky="NS")

caminho = tk.StringVar()

opcional = tk.Label(text= "*Opcional").grid(row=7, column=0, padx= (230, 0), pady= (0, 10))


respcheck = tk.IntVar()
todasounnao = tk.Checkbutton(text="Quero salvar os dados de todas as moedas.", variable=respcheck, command= all_or_not).grid(
    row=9, column=1, columnspan=7, padx= (50,0))


moeda2 = tk.Label(text="Escolha a moeda: ", font=("Roboto, 11"))
moeda2.grid(row=9, column=0, sticky="NSEW", pady=10)

selcMoeda2 = ttk.Combobox(values=lista, width=15)
selcMoeda2.grid(row=9, column=0, pady=10, columnspan= 3)

addMoeda = tk.Button(text= "+", font="Roboto, 9", command= adicionar_moeda)
addMoeda.grid(row= 9, column= 1, padx= (40, 0))

moedas = []

dataInicial = tk.Label(text="Escolha a data: ", font=("Roboto, 11")).grid(
    row=10, column=0, sticky="NSEW", pady=(0, 5))

selcDataInicial = DateEntry(year=2022, locale='pt_br', width=15)
selcDataInicial.grid(row=10, column=0, columnspan= 3)

selcDataFinal = DateEntry(year=2022, locale='pt_br', width=15)
selcDataFinal.grid(row=11, column=0, columnspan= 3)


botaoSalvar = tk.Button(text="Salvar", font="Roboto, 13", width=15, height=2, command=atualizar_arq).grid(
    row=8, column=2, rowspan=4, padx=(50, 0), pady=(50, 0))


msgSelcErr = tk.Label(text="Nenhum arquivo selecionado.",font="Roboto, 12")
msgSelcErr.grid(row=12, column=0, sticky="NSEW", columnspan= 5, pady=(25, 40))


janela.mainloop()


# Fazer com que o sistema crie um arquivo novo com os dados ou atualize um arquivo