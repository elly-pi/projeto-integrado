pacientes = []  # Lista que guarda dicionários com dados dos pacientes

def cadastrar_paciente():
    print("\n=== CADASTRAR PACIENTE ===")

    nome = input("Nome do paciente: ").strip()

    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Erro: digite um número válido para idade!")

    telefone = input("Telefone: ").strip()

    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!\n")


def ver_estatisticas():
    print("\n=== ESTATÍSTICAS ===")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.\n")
        return

    total = len(pacientes)
    soma_idades = sum(p["idade"] for p in pacientes)
    media = soma_idades / total

    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f}")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)\n")


def buscar_paciente():
    print("\n=== BUSCAR PACIENTE ===")

    nome_busca = input("Digite o nome para buscar: ").strip().lower()

    encontrados = [p for p in pacientes if nome_busca in p["nome"].lower()]

    if not encontrados:
        print("Nenhum paciente encontrado.\n")
        return

    print("Pacientes encontrados:")
    for p in encontrados:
        print(f"- {p['nome']} | {p['idade']} anos | Tel: {p['telefone']}")
    print()

def listar_pacientes():
    print("\n=== LISTA DE PACIENTES ===")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.\n")
        return

    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nome']} | {p['idade']} anos | Tel: {p['telefone']}")
    print()

def menu():
    while True:
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print("Saindo... Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

menu()