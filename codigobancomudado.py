
import tkinter as tk

saldo = 0

def depositar():
    global saldo
    valor = float(entrada.get())
    saldo += valor
    atualizar_saldo()

def sacar():
    global saldo
    valor = float(entrada.get())
    if valor <= saldo:
        saldo -= valor
        atualizar_saldo()
    else:
        rotulo_resultado.config(text="Saldo insuficiente!")

def atualizar_saldo():
    rotulo_resultado.config(text=f"Saldo atual: R$ {saldo:.2f}")

janela = tk.Tk()
janela.title("Banco Simples")

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Depositar", command=depositar).pack()
tk.Button(janela, text="Sacar", command=sacar).pack()

rotulo_resultado = tk.Label(janela, text="Saldo atual: R$ 0.00")
rotulo_resultado.pack()

janela.mainloop()

