# ==============================================================================
# SISTEMA DE GESTÃO DE NOTAS DE ALUNOS
# ==============================================================================

# 1. FUNÇÕES DO SISTEMA (Declaradas fora do laço para melhor performance)
def calc_media(lista_notas):
    """Calcula e retorna a média aritmética de uma lista de notas."""
    return sum(lista_notas) / len(lista_notas)

# Funções anônimas para formatação e lógica de negócios
arred_media = lambda media: round(media, 2)
aprov_reprov = lambda media: 'APROVADO' if media >= 7.0 else 'REPROVADO'


# 2. LAÇO PRINCIPAL (Cadastro de múltiplos alunos)
while True:
    print(f"\n{' CADASTRO DE NOVO ALUNO ':^40}")
    print("-" * 40)

    nome_aluno = input("Nome do aluno: ").strip().title()
    idade = input("Idade do aluno: ").strip()

    print("\nInsira as notas do aluno (máximo 5 períodos).")

    # Laço para validação e garantia de dados corretos
    while True:
        coloca_notas_str = input("Insira 5 notas separadas por vírgula (ex: 8.5, 7.0, 9.0, 6.5, 8.0):\n> ")
        coloca_notas = coloca_notas_str.split(',')

        # Verifica quantidade de notas
        if len(coloca_notas) != 5:
            print(f"\n Erro: Você inseriu {len(coloca_notas)} notas, mas o sistema exige 5. Tente novamente.")
            continue

        # Validação se as entradas são numéricas
        validas = True
        for nota in coloca_notas:
            nota_limpa = nota.strip()
            if not nota_limpa.replace('.', '', 1).isdigit():
                validas = False
                break

        if not validas:
            print("\n Erro: Entrada inválida! Digite apenas números decimais separados por vírgula.")
            continue

        # Converte para float após validação bem-sucedida
        notas = [float(nota.strip()) for nota in coloca_notas]
        break

    # 3. PROCESSAMENTO DOS RESULTADOS
    media_calculada = calc_media(notas)
    media_final = arred_media(media_calculada)
    situacao = aprov_reprov(media_calculada)

    # 4. EXIBIÇÃO DO RELATÓRIO FINAL (Estética limpa e alinhada)
    print("\n" + "=" * 40)
    print(f"{'RELATÓRIO FINAL':^40}")
    print("=" * 40)
    print(f" Aluno: {nome_aluno:<2} |  Idade: {idade}")
    print(f" Notas: {str(notas)}")
    print(f" Média: {media_final}")
    print(f" Situação:  {situacao}")
    print("=" * 40 + "\n")

    # Controle de encerramento do sistema
    stop = input("Deseja encerrar a execução do sistema? (Sim / Nao): ").lower().strip()
    if stop in ["sim", "s"]:
        print(f"\n{'='*40}\n{'SISTEMA FINALIZADO COM SUCESSO!':^40}\n{'='*40}")
        break
