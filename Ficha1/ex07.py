num = int(input("Insira um número inteiro positivo:"))

while(num < 0):
    num = int(input("Erro. Insira um número válido:"))

if(num % 2 == 0):
    num = num / 2

else:
    num = (num * 3) + 1

print(num)