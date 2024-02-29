array = []
quantidade = int(input("Quantos números quer colocar? "))

while quantidade != len(array):
    numero = int(input("Insira um número entre 0 e 1000: "))
    if numero <= 1000 and numero >= 0:
        array.insert(0, numero)
    else:
        print("ERROR")
        break

if len(array) > 0:
    array.sort()
    print(f"{array[0]} {array[-1]}")
    print(array[0] + array[-1])