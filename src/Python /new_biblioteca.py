# Passo a passo para criar uma biblioteca em Python
import matplotlib.pyplot as plt
import json as js 
import os
from collections import defaultdict
# aqui fica salvo em js a biblioteca, para que seja possivel salvar e carregar os livros cadastrados
# Inicia em uma lista vazia para armazenar os livros
ARQUIVO = 'biblioteca.json'

 # #func para cadastrar 
def cadastrar_livro(titulo, autor, genero, quantidade):
    """Cadastra um novo livro na biblioteca."""
    livro = {
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
        'quantidade': quantidade
    }
    return livro

# os livros ficam em um .json para que seja possivel salvar e carregar ou enviar
# para outro lugar, e para que seja possivel salvar e carregar os livros cadastrados
class Dicionario:

    def __init__(self):
        self.livros = []
        if os.path.exists(ARQUIVO):
            try:
                with open(ARQUIVO, 'r', encoding='utf-8') as f:
                    self.livros = js.load(f)
            except js.JSONDecodeError:
                print(f"Erro ao ler o arquivo {ARQUIVO}. \nO arquivo pode estar corrompido ou vazio. Iniciando com uma lista vazia.")
                self.livros = []

    # adicionar um livro ao dicionario e salvar no arquivo .json          
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            js.dump(self.livros, f, ensure_ascii=False, indent=4)

    #listar os livros cadastrados, todos
    def listar_livros(self):
        return self.livros
    
# buscar livros por título, todos os livros que tiverem o titulo igual ao que 
# foi digitado, independente de maiusculas ou minusculas
    def buscar_por_titulo(self, titulo):
        return [livro for livro in self.livros if livro['titulo'].lower() == titulo.lower()]
       
# gerar grafico com a quantidade de livros por genero? categoria?
# tem realmente que fazer em matplotlib? 
def grafico():
    with open(ARQUIVO, 'r', encoding='utf-8') as f:
        livros = js.load(f)

    if not livros:
        print("Nenhum livro para graficar.")
        return
    #aqui puxo diretamente do arquivo .json os titulos, quantidades e generos dos livros cadastrados
    titulos = [f"{l['titulo']} ({l['autor']})" for l in livros]
    quantidades = [l['quantidade'] for l in livros]
    generos = [l['genero'] for l in livros]

    # aqui mostra o grafico de barras com a quantidade de livros por titulo, mas poderia ser por genero, ou por autor, ou por quantidade, ou por qualquer outra coisa que seja relevante para o usuario
    soma = defaultdict(int)
    for l in livros:
        soma[l['genero']] += l['quantidade']

    plt.figure(figsize=(9, 6))   # cria a figura primeiro
    plt.bar(soma.keys(), soma.values(), color='steelblue')  # desenha DENTRO dela
    plt.xlabel('Gêneros', color='steelblue')
    plt.ylabel('Quantidade')
    plt.title('Quantidade por Gênero')
    plt.tight_layout()
    plt.show()

    # tentei fazer um grafico de pizza com a quantidade de livros por genero, 
    # consegui fazer funcionar, entao comentei o codigo, pois so um grafico de barras ja é suficiente, 
    # deixei o codigo comentado para caso queira usar futuramente

    # from collections import Counter
    # contagem = Counter(generos)
    # plt.figure(figsize=(6, 6))
    # plt.pie(contagem.values(), labels=contagem.keys(), autopct='%1.0f%%')
    # plt.title('Livros por Gênero')
    # plt.show()

#aqui onde funciona tudo, a interfaçe com o usuario, o menu, e as opções de cadastrar, listar e buscar livros
def main():
    livro = Dicionario()

    while True:
        print("\n=== BIBLIOTECA ===")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar por título")
        print("4. Gerar gráfico de quantidade por livro")
        print("5. Sair")
        opcao = input("Escolha: ")

        if opcao == "1" or opcao == "Cadastrar livro".lower() or opcao == "cadastrar":
            
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Gênero: ")
               
            # Validação para garantir que a quantidade seja um número inteiro
            while True:
                try:
                    quantidade = int(input("Quantidade: "))
                    break
                except ValueError:
                      print("Digite um número inteiro (ex: 5).")
        
            #aqui manda para o .json o livro cadastrado, e salva no mesmo
            cadastrar = cadastrar_livro(título, Autor, Gênero, quantidade)
            livro.adicionar_livro(cadastrar)
            print("✓ Salvo!")

        #aqui percorre a lista e adiciona um numero para cada livro, e mostra 
        #o titulo, autor, genero e quantidade de cada livro cadastrado
        elif opcao == "2":
            livros = livro.listar_livros()
            if livros:
                for i, l in enumerate(livros, 1):
                    print(f"\n{i}. {l['titulo']} — {l['autor']} ({l['genero']}) x{l['quantidade']}")
            else:
                print("Nenhum livro cadastrado.")
        #busxca por titulo, e mostra o resultado, se nao encontrar, mostra que nao encontrou
        elif opcao == "3":
            t = input("Título: \n")
            resultado = livro.buscar_por_titulo(t)
            if resultado:
                for i, l in enumerate(resultado, 1):
                    print(f"\n{i}. {l['titulo']} — {l['autor']} ({l['genero']}) x{l['quantidade']}")
                # print(f"Encontrado: {resultado[0]}")
            else:
                print("Não encontrado.")
        #o grafico mostra a quantidade de livros por titulo, mas poderia ser por genero, ou por autor, ou por quantidade, ou por qualquer outra coisa que seja relevante para o usuario
        elif opcao == "4":
            grafico()

        elif opcao == "5" or opcao == "Sair".lower() or opcao == "sair":
            print("Até!")
            break

if __name__ == "__main__":
    main()
#esse final e caso eu importe ele em outro arquivo, para que nao execute o main() automaticamente,
# e sim apenas quando eu chamar o arquivo diretamente, e nao quando eu importar ele em outro arquivo
#o principal, testa o sistema