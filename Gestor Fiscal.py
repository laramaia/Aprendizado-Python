import re
import random

def gerar_registro_fiscal(tamanho):
    novo_registro = []

    for x in range(tamanho):
        num_aleatorio = random.randint(0, 9)
        novo_registro.append(num_aleatorio)

    return novo_registro


def validar_registro_fiscal(registro_fiscal):
    pass


def formatar_registro_fiscal(registro_fiscal):
    pass


def salvar_registro_fiscal(nomearquivo, registro_fiscal):
    with open (f"{nomearquivo}.json", "w") as f:
        json.dump(registro_fiscal, f)


while True:
    menu = "[1] Gerar CPF/CNPJ\n[2] Validar CPF/CNPJ\n[3] Formatar CPF/CNPJ\n[4] Salvar CPF/CNPJ em arquivo\n[5] Sair"
    print(menu)
    escolha = input("Deseja escolher qual opção? ")

    if escolha == "1": # Gerar CPF/CNPJ aleatório
        tipo_registro = input("Tipo de registro fiscal: [1] CPF\n[2] CNPJ")
        # Como o tamanho pode mudar, pedir para o usuário inserir
        tamanho_registro_fiscal = int(input("Quantidade de dígitos do documento: "))

        # Chamar e exibir resultado da função "gerar_registro_fiscal"
        registro = gerar_registro_fiscal(tamanho_registro_fiscal)
        if tipo_registro == "1":
            print(f"CPF gerado!\nCPF: {registro}")
        elif tipo_registro == "2":
            print(f"CNPJ gerado!\nCNPJ: {registro}")
        else:
            print("Opção inválida.")

    elif escolha == "2":
        tipo_validacao = input("Deseja validar CPF ou CNPJ? ")

    elif escolha == "3":
        tipo_formatacao = input("Deseja formatar CPF ou CNPJ? ")

    elif escolha == "4": 
        if registro is None:
            print("CPF/CNPJ não gerado ainda.")
        else:
            nomearquivo = input("Insira o nome do arquivo: ")
            salvar_registro_fiscal(nomearquivo, registro)

    elif escolha == "5":
        break

    else:
        print("Opção inválida.")
