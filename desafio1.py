num0 = 0
num1 = 1
num2 = 1

print(num0)
print(num1)
print(num2)

while num2 < 500:
    num0 = num1
    num1 = num2
    num2 = num0 + num1
    print(num2)