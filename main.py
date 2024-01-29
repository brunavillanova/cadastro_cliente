from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect("clientes.bd")
cursor = conn.cursor()

# Criar a tabela se ela não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        cod INTEGER PRIMARY KEY,
        nome_cliente TEXT,
        telefone TEXT,
        cidade TEXT
    )
""")

# Commit para salvar as alterações e fechar a conexão
conn.commit()
conn.close()

class Func():
        def limpar_tela(self):
            self.codigo_entry.delete(0, END)
            self.nome_entry.delete(0, END)
            self.telefone_entry.delete(0, END)
            self.cidade_entry.delete(0, END)

        def conecta_bd(self):
            self.conn = sqlite3.connect("clientes.bd")
            self.cursor = self.conn.cursor()
            print("Conectando ao banco de dados")

        def desconecta_bd(self):
            self.conn.close()
            print("Desconectando ao banco de dados")

        def variaveis(self):
            self.codigo = self.codigo_entry.get()
            self.nome = self.nome_entry.get()
            self.telefone = self.telefone_entry.get()
            self.cidade = self.cidade_entry.get()

        def add_cliente(self):
            self.variaveis()
            self.conecta_bd()

            self.cursor.execute("""
                INSERT INTO clientes (nome_cliente, telefone, cidade)
                VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))

            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()

        def onedoubleclick(self, event):
            self.limpar_tela()
            selected_item = self.listcli1.selection()
            if selected_item:
                col1, col2, col3, col4 = self.listcli1.item(selected_item, "values")
                self.codigo_entry.insert(END, col1)
                self.nome_entry.insert(END, col2)
                self.telefone_entry.insert(END, col3)
                self.cidade_entry.insert(END, col4)

        def deleta_cliente(self):
            self.variaveis()

            self.conecta_bd()
            self.cursor.execute("DELETE FROM clientes WHERE cod = ?", (self.codigo,))
            self.conn.commit()

            self.desconecta_bd()
            self.limpar_tela()
            self.select_lista()

        def select_lista(self):
            self.listcli1.delete(*self.listcli1.get_children())
            self.conecta_bd()
            lista = self.cursor.execute("""
                SELECT cod, nome_cliente, telefone, cidade FROM clientes
                ORDER BY nome_cliente ASC;
            """).fetchall()

            for i in lista:
                self.listcli1.insert("", END, values=i)

            self.desconecta_bd()
            self.limpar_tela()

class Aplicacao(Func):
        def __init__(self):
            self.root = Tk()
            self.tela()
            self.frame_da_tela() 
            self.criando_botoes()
            self.lista_frame2()
            self.select_lista()
            self.Menus()
            self.root.mainloop()

        def tela(self):
            self.root.title("Cadastro")
            self.root.configure(background='#1e3743')
            self.root.geometry("788x588")
            self.root.resizable(True, True)
            self.root.maxsize(width=900, height=700)
            self.root.minsize(width=500, height=400)

        def frame_da_tela(self):
            self.frame_1 = tk.Frame(self.root, border=4, bg='#dfe3ee', highlightbackground='#759feb', highlightthickness=3)
            self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
            
            self.frame_2 = tk.Frame(self.root, border=4, bg='#dfe3ee', highlightbackground='#759feb', highlightthickness=3)
            self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        def criando_botoes(self):
            self.bt_limpar = Button(self.frame_1, text='Limpar', bd=5, bg='#4682B4', font=('verdana', 8, 'bold'), command=self.limpar_tela)
            self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

            self.bt_buscar = Button(self.frame_1, text='Buscar', bd=5, bg='#4682B4', font=('verdana', 8, 'bold'))
            self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

            self.bt_novo = Button(self.frame_1, text='Novo', bd=5, bg='#4682B4', font=('verdana', 8, 'bold'), command=self.add_cliente)
            self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

            self.bt_alterar = Button(self.frame_1, text='Alterar', bd=5, bg='#4682B4', font=('verdana', 8, 'bold'))
            self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

            self.bt_apagar = Button(self.frame_1, text='Apagar', bd=5, bg='#4682B4', font=('verdana', 8, 'bold'), command=self.deleta_cliente)
            self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

            self.lb_codigo = Label(self.frame_1, text="Código", bg='#4682B4')
            self.lb_codigo.place(relx=0.05, rely=0.05)

            self.codigo_entry = Entry(self.frame_1)
            self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

            self.lb_nome = Label(self.frame_1, text="Nome", bg='#4682B4')
            self.lb_nome.place(relx=0.05, rely=0.35)

            self.nome_entry = Entry(self.frame_1)
            self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.80)

            self.lb_telefone = Label(self.frame_1, text="Telefone", bg='#4682B4')
            self.lb_telefone.place(relx=0.05, rely=0.60)

            self.telefone_entry = Entry(self.frame_1)
            self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

            self.lb_cidade = Label(self.frame_1, text="Cidade", bg='#4682B4')
            self.lb_cidade.place(relx=0.5, rely=0.6)

            self.cidade_entry = Entry(self.frame_1)
            self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.3)

        def lista_frame2(self):
            self.listcli1 = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4"))
            self.listcli1.heading("#0", text="")
            self.listcli1.heading("#1", text="Código")
            self.listcli1.heading("#2", text="Nome")
            self.listcli1.heading("#3", text="Telefone")
            self.listcli1.heading("#4", text="Cidade")

            self.listcli1.column("#0", width=1)
            self.listcli1.column("#1", width=50)
            self.listcli1.column("#2", width=200)
            self.listcli1.column("#3", width=125)
            self.listcli1.column("#4", width=125)

            self.listcli1.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

            self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
            self.listcli1.configure(yscroll=self.scroolLista.set)
            self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
            self.listcli1.bind("<Double-1>", self.onedoubleclick)

        def Menus(self):
            Menubar = Menu(self.root)
            self.root.config(menu=Menubar)
            filemenu = Menu(Menubar)
            filemenu2 = Menu(Menubar)

            def Quit(): self.root.destroy()

            Menubar.add_cascade(label="Opções", menu=filemenu)
            Menubar.add_cascade(label="sobre", menu=filemenu2)

            filemenu.add_command(label="sair", command=Quit)
            filemenu2.add_command(label="Limpa Cliente", command=self.limpar_tela)


    # Create an instance of the Aplicacao class
app = Aplicacao()
