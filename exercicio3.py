num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
soma = num1 + num2
print(f"{num1} + {num2} = {soma}")
resposta = input("Deseja fazer mais uma soma: ")

while resposta == "s":
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    soma = num1 + num2
    print(f"{num1} + {num2} = {soma}")
    resposta = input("Deseja fazer mais uma soma? ")
   