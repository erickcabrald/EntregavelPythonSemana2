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

"""
```portugol
programa
{
    funcao inicio()
    {
        real soma = 0.0
        real maior
        real menor
        real numero

        para (inteiro i = 1; i <= 5; i++)
        {
            escreva("Digite o ", i, "º número: ")
            leia(numero)

            soma = soma + numero

            // No primeiro número, inicializamos
            // maior e menor com o próprio número
            se (i == 1)
            {
                maior = numero
                menor = numero
            }
            senao
            {
                se (numero > maior)
                {
                    maior = numero
                }

                se (numero < menor)
                {
                    menor = numero
                }
            }
        }

        real media = soma / 5

        escreva("\n--- Resultados ---\n")
        escreva("Soma dos valores: ", soma, "\n")
        escreva("Média dos valores: ", media, "\n")
        escreva("Maior valor digitado: ", maior, "\n")
        escreva("Menor valor digitado: ", menor, "\n")
    }
}
```

"""