import time

dominios = ["gmail", "hotmail", "outlook", "yahoo", "icloud", "protonmail"]
simbolos = ["!", "@", "$", "%", "¨¨", "&", "*", "(", ")", "#"]

# Função para cadastrar funcionário
def cadastrar_funcionario():
    nome_completo = input("Nome completo: ")
    usuario = input("Nome de usuário: ")
    email = input("E-mail: ")
    ## Loop enquanto validar_email não retornar True
    while not validar_email(email):
        email = input("E-mail: ")

    senha = input("Senha: ")
    ## Loop enquanto validar_senha não retornar True
    while not validar_senha(senha):
        senha = input("Senha: ")

    confirmacao_senha = input("Confirme sua senha: ")
    ## Tratamento de erro - confirmação de senha
    while confirmacao_senha != senha:
        print("Erro de confirmação de senha. Tente novamente.")
        confirmacao_senha = input("Confirme sua senha: ")

    return nome_completo, usuario, email, senha, confirmacao_senha


def validar_email(email):
    if len(email) < 8: 
        print("E-mail pequeno demais. Tente novamente.")
        return False
    if not "@" in email:
        print("E-mail não contém \"@\". Tente novamente.")
        return False

    partes_endereco_email = email[email.index("@"):]
    ## verifica: se possui domínio e extensão de domínio
    if not any(dominio in partes_endereco_email for dominio in dominios) or not ".com" in partes_endereco_email or ".br" in partes_endereco_email: 
        print("E-mail não é válido. Tente novamente.")
        return False

    return True


def validar_senha(senha):
    if len(senha) < 8:
        print("Senha possui menos de 8 caracteres. Tente novamente.")
        return False
    if senha == senha.lower() or senha == senha.upper():
        print("A senha precisa possuir pelo menos uma letra maiúscula e uma minúscula. Tente novamente.")
        return False
    if not any (simbolo in senha for simbolo in simbolos):
        print("A senha precisa possuir pelo menos um símbolo. Tente novamente.")
        return False

    return True


def login(email_login, senha_login):
    while email_login != email or senha_login != senha:
        print("O e-mail ou senha está errado. Tente novamente.")

        email_login = input("E-mail: ")
        senha_login = input("Senha: ")      
    
    print("Carregando")
    for x in range(8):
        print(".")
        time.sleep(1)

    return email_login, senha_login


nome_completo, usuario, email, senha, confirmacao_senha = cadastrar_funcionario()
print("")
print("Cadastrado realizado!")
print("")
email_login = input("E-mail: ")
senha_login = input("Senha: ")
print(login(email_login, senha_login))
