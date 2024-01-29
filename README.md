# cadastro_cliente

O código Python em questão é um programa de cadastro de clientes com interface gráfica usando a biblioteca Tkinter. Ele realiza as seguintes operações:

    Conexão com o Banco de Dados:
        Estabelece conexão com um banco de dados SQLite chamado "clientes.bd".
        Cria um cursor para interação com o banco.

    Criação da Tabela "clientes":
        Verifica se a tabela "clientes" existe no banco.
        Se não existir, cria a tabela com colunas para código, nome, telefone e cidade.

    Definição de Funções:
        Funções para limpar a tela, conectar e desconectar do banco, obter variáveis do formulário, adicionar, deletar, alterar, buscar e exibir clientes.

    Interface Gráfica (Tkinter):
        Cria uma janela com frames para organização.
        Adiciona botões para limpar, buscar, adicionar, alterar e deletar clientes.
        Inclui campos para inserção de código, nome, telefone e cidade.
        Mostra uma lista de clientes em um Treeview.

    Menu de Opções e Relatórios:
        Adiciona menus para sair, limpar tela e gerar relatórios.
        Implementa a geração de um relatório simples em PDF usando a biblioteca ReportLab.

    Inicialização do Programa:
        Cria uma instância da classe principal (Aplicacao) para iniciar a aplicação.
