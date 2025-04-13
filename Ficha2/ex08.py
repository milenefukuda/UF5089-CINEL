num = int(input("Insira um número positivo maior ou igual a 2: "))

while num < 2:
    num = int(input("Erro"))

div = 2

while num > 1:
    if(num % div == 0):
        print(div)
        num = num // div

    else:
        div = div + 1
