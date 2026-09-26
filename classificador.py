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

"""
```portugol id="m4k8zp"
programa
{
    funcao inicio()
    {
        inteiro idade
        real renda
        cadeia categoria

        escreva("Digite a idade do cliente: ")
        leia(idade)

        escreva("Digite a renda do cliente (R$): ")
        leia(renda)

        se (idade < 18 ou renda < 2000.0)
        {
            categoria = "Bronze"
        }
        senao se (renda >= 2000.0 e renda < 5000.0)
        {
            categoria = "Prata"
        }
        senao se (renda >= 5000.0 e renda < 10000.0)
        {
            categoria = "Ouro"
        }
        senao
        {
            categoria = "Diamante"
        }

        escreva(
            "O cliente foi classificado na categoria: ",
            categoria,
            "\n"
        )
    }
}
```

"""