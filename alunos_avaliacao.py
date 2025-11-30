def cadastrar_alunos():
    nomes = []
    medias = []
    while True:
        try:
            n = int(input("Digite o número de alunos a cadastrar: "))
            if n <= 0:
                print("Por favor, digite um número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    for i in range(n):
        nome = input(f"Digite o nome do aluno {i+1}: ").strip()
        notas = []
        for avaliacao in ["força", "resistência", "flexibilidade"]:
            while True:
                try:
                    nota = float(input(f"Digite a nota de {avaliacao} do aluno {nome}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número válido.")
        media = sum(notas) / len(notas)
        nomes.append(nome)
        medias.append(media)
    return nomes, medias

def exibir_todas_medias(nomes, medias):
    print("\nMédias dos alunos:")
    for nome, media in zip(nomes, medias):
        print(f"{nome}: {media:.2f}")

def exibir_aptos(nomes, medias):
    print("\nAlunos totalmente aptos (média > 7.0):")
    for nome, media in zip(nomes, medias):
        if media > 7.0:
            print(f"{nome}: {media:.2f}")

def exibir_consideraveis(nomes, medias):
    print("\nAlunos com resultado considerável (5.0 <= média <= 7.0):")
    for nome, media in zip(nomes, medias):
        if 5.0 <= media <= 7.0:
            print(f"{nome}: {media:.2f}")

def exibir_nao_aptos(nomes, medias):
    print("\nAlunos não aptos (média < 5.0):")
    for nome, media in zip(nomes, medias):
        if media < 5.0:
            print(f"{nome}: {media:.2f}")

def resumo_resultados(medias):
    abaixo = sum(1 for m in medias if m < 5.0)
    consideravel = sum(1 for m in medias if 5.0 <= m <= 7.0)
    apto = sum(1 for m in medias if m > 7.0)

    print("\nResumo de desempenho:")
    print(f"Teste abaixo do recomendado (média < 5.0): {abaixo}")
    print(f"Teste com valor considerável (5.0 <= média <= 7.0): {consideravel}")
    print(f"Aluno apto em todas avaliações físicas (média > 7.0): {apto}")

def menu_principal(nomes, medias):
    while True:
        print("\nMENU PRINCIPAL:")
        print("1 - Exibir todas as médias")
        print("2 - Exibir apenas os alunos totalmente aptos à atividade")
        print("3 - Exibir apenas os alunos com resultado considerável")
        print("4 - Exibir apenas os alunos não aptos à atividade física")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            exibir_todas_medias(nomes, medias)
            resumo_resultados(medias)
        elif opcao == "2":
            exibir_aptos(nomes, medias)
        elif opcao == "3":
            exibir_consideraveis(nomes, medias)
        elif opcao == "4":
            exibir_nao_aptos(nomes, medias)
        elif opcao == "5":
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    while True:
        nomes, medias = cadastrar_alunos()
        menu_principal(nomes, medias)
        novamente = input("\nDeseja cadastrar novos alunos? (s/n): ").strip().lower()
        if novamente != 's':
            print("Até a próxima!")
            break

if __name__ == "__main__":
    main()
