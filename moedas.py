import tkinter as tk

janela = tk.Tk()

janela.title('Cotação de moedas')

# janela.rowconfigure(0, weight= 1)

mainTitle = tk.Label(text= "Cotação de moedas", font= ("Roboto", 50))
mainTitle.grid(row= 0, column= 3, sticky= "EW", padx= 50, pady= 50)

subTitle1 = tk.Label(text= "Cotação de uma única moeda").grid(row= 1, column= 1)


janela.mainloop()