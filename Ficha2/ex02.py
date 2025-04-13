num = int(input("Escreva um número inteiro:"))

while num < 1:
    num = int(input("Erro!"))

div = 1

while div <= num:
    if(num % div == 0):
        print(div)
    div = div + 1