nome = input("Insira um nome: ")
if len(nome) < 3:
    while len(nome) < 3:
        print("Erro, o nome tem que ser com mais de 3 caracteres.")
        nome = input("Insira novamente um nome: ")

idade = int(input("Insira uma idade: "))
if idade < 0 or idade >= 150:
    while idade < 0 or idade >= 150:
        print("Erro, a idade tem que estar entre 0 e 150.")
        idade = int(input("Insira novamente uma idade: "))

salario = int(input("Insira um salario: "))
if salario < 0:
    while salario < 0:
        print("Erro, o salario tem que ser positivo.")
        salario = int(input("Insira novamente um salario: "))

sexo = input("Insira o sexo: ")
if sexo != "m" and sexo != "f":
    while sexo != "m" and sexo != "f":
        print("Erro, o sexo tem que ser masculino (m) ou feminino (f)")
        sexo = input("Insira novamente um salario: ")

estado = input("Insira o estado civil: ")
if estado != "s" and estado != "c" and estado != "v" and estado != "d":
    while estado != "s" and estado != "c" and estado != "v" and estado != "d":
        print("Erro, o estado civil tem que ser solteiro (s), casado (c), viuvo (v) ou divorciado (d)")
        estado = input("Insira novamente um estado civil: ")

texto = input("Insira um texto: ")

print(nome)
print(idade)
print(salario)
print(sexo)
print(estado)
print(len(texto))