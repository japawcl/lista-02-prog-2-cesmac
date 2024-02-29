array = []
quantidade = int(input("Quantos números quer colocar? "))

while quantidade != len(array):
    numero = int(input("Insira um número: "))
    array.insert(0, numero)
    

array.sort()

print(f"{array[0]} {array[-1]}")

print(array[0] + array[-1])