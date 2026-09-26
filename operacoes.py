print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = int(input("Escolha uma opção (1-4): "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match opcao:
    case 1:
        resultado = num1 + num2
        print(f"Resultado da Soma: {resultado:.2f}")
    case 2:
        resultado = num1 - num2
        print(f"Resultado da Subtração: {resultado:.2f}")
    case 3:
        resultado = num1 * num2
        print(f"Resultado da Multiplicação: {resultado:.2f}")
    case 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da Divisão: {resultado:.2f}")
        else:
            print("Erro: Não é possível dividir por zero.")
    case _:
        print("Opção inválida! Escolha um número de 1 a 4.")



"""
```portugol
programa
{
    funcao inicio()
    {
        inteiro opcao
        real num1
        real num2
        real resultado

        escreva("1 - Soma (+)\n")
        escreva("2 - Subtração (-)\n")
        escreva("3 - Multiplicação (*)\n")
        escreva("4 - Divisão (/)\n")

        escreva("Escolha uma opção (1-4): ")
        leia(opcao)

        escreva("Digite o primeiro número: ")
        leia(num1)

        escreva("Digite o segundo número: ")
        leia(num2)

        escolha (opcao)
        {
            caso 1:
                resultado = num1 + num2
                escreva("Resultado da Soma: ", resultado, "\n")
                pare

            caso 2:
                resultado = num1 - num2
                escreva("Resultado da Subtração: ", resultado, "\n")
                pare

            caso 3:
                resultado = num1 * num2
                escreva("Resultado da Multiplicação: ", resultado, "\n")
                pare

            caso 4:
                se (num2 != 0)
                {
                    resultado = num1 / num2
                    escreva("Resultado da Divisão: ", resultado, "\n")
                }
                senao
                {
                    escreva("Erro: Não é possível dividir por zero.\n")
                }
                pare

            caso contrario:
                escreva("Opção inválida! Escolha um número de 1 a 4.\n")
        }
    }
}
```

"""