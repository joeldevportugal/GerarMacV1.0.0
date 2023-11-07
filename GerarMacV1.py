import customtkinter
import random
from tkinter import Listbox, messagebox


# Função para gerar um endereço MAC aleatório
def gerar_mac():
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    mac_str = ':'.join(f'{x:02X}' for x in mac)
    return mac_str

# Função para adicionar 15 endereços MAC diferentes na Listbox
def adicionar_macs():
    Lmac.delete(0, 'end')  # Limpa a Listbox antes de adicionar os novos MACs
    for _ in range(15):
        mac = gerar_mac()
        Lmac.insert('end', mac)

# Função para guardar os MACs em um arquivo de texto
def guardar_macs_em_txt():
    messagebox.showinfo('Gerar', 'Ficheiro Gerado com sucesso')    
    macs = Lmac.get(0, 'end')
    with open('enderecos_mac.txt', 'w') as file:
        for mac in macs:
            file.write(mac + '\n')

# Função para limpar a Listbox e a entrada de texto
def limpar():
    Lmac.delete(0, 'end')  # Limpa a Listbox
    EGerar.delete(0, 'end')  # Limpa a entrada de texto


# Função para perguntar ao usuário se deseja sair
def sair():
    resposta = messagebox.askquestion("Sair", "Deseja sair do programa?")
    if resposta == "yes":
        janela.destroy()

janela = customtkinter.CTk()
janela.geometry('700x390+100+100')
janela.resizable(False, False)
janela.title('Gerar Mac V1.0.0')

Lmac = customtkinter.CTkLabel(janela, text='Endereço Mac:')
Lmac.place(x=10, y=30)

EGerar = customtkinter.CTkEntry(janela, placeholder_text='Insira o endereço Mac', width=450)
EGerar.place(x=95, y=30)

Bgerar = customtkinter.CTkButton(janela, text='Gerar', command=adicionar_macs)
Bgerar.place(x=550, y=30)

Lmac = Listbox(janela, width=55, height=10, font=('arial 20'))
Lmac.place(x=10, y=95)

Guardar = customtkinter.CTkButton(janela, text='Guardar txt', command=guardar_macs_em_txt)
Guardar.place(x=10, y=350)

Limpar = customtkinter.CTkButton(janela, text='Limpar', command=limpar)
Limpar.place(x=160, y=350)

Sair = customtkinter.CTkButton(janela, text='Sair', command=sair)
Sair.place(x=305, y=350)

janela.mainloop()
