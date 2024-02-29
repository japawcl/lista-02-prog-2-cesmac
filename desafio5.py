num = int(input("Insira um número: "))
i = 2
primo = True
while i < num:
    if num % i == 0:
        primo = False
        break
    i += 1
if primo:
    print("O número é primo")
else:
    print("O número não é primo")
