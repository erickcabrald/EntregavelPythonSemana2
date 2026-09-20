idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda do cliente (R$): "))

if idade < 18 or renda < 2000.0:
    categoria = "Bronze"
elif 2000.0 <= renda < 5000.0:
    categoria = "Prata"
elif 5000.0 <= renda < 10000.0:
    categoria = "Ouro"
else:
    categoria = "Diamante"

print(f"O cliente foi classificado na categoria: {categoria}")