import time

# ---Funções---
def buscar_mensagem(mensagem):
    while True:
        trecho_alvo = input("Qual palavra deseja modificar? ")

        if " " in trecho_alvo:
            print("No momento, só é possível selecionar uma palavra.")
            print(" ")
            continue

        ## Verificar se a mensagem que o usuário deseja modificar está dentro do texto
        if trecho_alvo in mensagem:
        ## Se estiver, transformar em lista para verificar índice depois
            lista_palavras = mensagem.split()

            return trecho_alvo, lista_palavras

        else:
            ## Loop
            print("Palavra não encontrada. Tente novamente")
            print(" ")


def modificar_mensagem(acao, lista_mensagem, trecho_alvo, novo_trecho=None):
    nova_lista = []
    for i, palavra in enumerate (lista_mensagem):
        ## Adicionar novo_trecho após identificar trecho_alvo
        if acao == "adicionar" and palavra == trecho_alvo:
            nova_lista.append(palavra)
            nova_lista.append(novo_trecho)
        ## Pular trecho_alvo
        elif acao == "remover" and palavra == trecho_alvo:
            continue
        ## Passar elemento original para nova lista, caso não atenda às condições acima
        else:
            nova_lista.append(palavra)

    return nova_lista

# ---Código Principal---
print("="*100 + "\n" + " " * 40 + "Editor de Texto\n" + "="*100)
sair = "N"

while sair == "N":
    texto = input("\nEscreva....\n\n")
    menu = int(input("\n\nO que deseja fazer (selecione o número correspondente)?\n\n[1] Inserir palavra.\n[2] Excluir palavra.\n[3] Contar palavra.\n[4] Substituir texto\n\n"))
    print(" ")
    print(" ")

    # Acrescentar texto
    if menu == 1:
        palavra_alvo, lista_texto = buscar_mensagem(texto)
        palavra_nova = input("Insira a nova palavra: ")
        novo_texto = modificar_mensagem("adicionar", lista_texto, palavra_alvo, palavra_nova)
        print(f"Texto atualizado!\n\n{' '.join(novo_texto)}")

    # Remover texto
    elif menu == 2:
        palavra_alvo, lista_texto = buscar_mensagem(texto)
        novo_texto = modificar_mensagem("remover", lista_texto, palavra_alvo)
        print(f"Texto atualizado!\n\n{' '.join(novo_texto)}")

    # Contar texto
    elif menu == 3:
        ## Converter texto e palavra_a_contar em minúsculas para contagem precisa
        texto = texto.lower()
        palavra_a_contar = input("Insira qual palavra deseja contar: ").lower()
        contador = texto.count(palavra_a_contar)
        print(f"\"{palavra_a_contar}\" foi encontrada {contador}x.")

    # Substituir texto
    elif menu == 4:
        palavra_alvo, lista_texto = buscar_mensagem(texto)
        palavra_nova = input("Insira a nova palavra: ")
        print(" ")
        novo_texto = texto.replace(palavra_alvo, palavra_nova)
        print(f"Texto atualizado!\n\n{novo_texto}")

    else:
        print("Opção inválida.")

    print(" ")
    sair = input("Deseja sair [S/N]? ").upper()
    print(" ")
    for x in range(5):
        print(".")
        time.sleep(1)
