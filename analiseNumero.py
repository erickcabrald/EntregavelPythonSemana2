soma = 0.0
maior = None
menor = None

# O range(1, 6) percorre as iterações de 1 até 5
for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

    if i == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / 5

print("\n--- Resultados ---")
print(f"Soma dos valores: {soma:.2f}")
print(f"Média dos valores: {media:.2f}")
print(f"Maior valor digitado: {maior:.2f}")
print(f"Menor valor digitado: {menor:.2f}")