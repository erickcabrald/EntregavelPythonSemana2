SENHA_CORRETA = "python123"
MAX_TENTATIVAS = 3

tentativas = 0
autenticado = False

print("--- Sistema de Autenticação ---")

while tentativas < MAX_TENTATIVAS and not autenticado:
    senha_digitada = input("Digite a senha de acesso: ")
    tentativas += 1  # Atualização da variável de controle do loop

    if senha_digitada == SENHA_CORRETA:
        autenticado = True
        print("\nAcesso concedido! Bem-vindo ao sistema.")
    else:
        tentativas_restantes = MAX_TENTATIVAS - tentativas
        if tentativas_restantes > 0:
            print(f"Senha incorreta! Tentativas restantes: {tentativas_restantes}\n")

if not autenticado:
    print("\nAcesso bloqueado! Número máximo de 3 erros atingido.")