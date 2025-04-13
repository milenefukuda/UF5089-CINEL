num = int(input("Escreva um número positivo maior que um: "))

while num < 2:
    num = int(input("Erro."))

div = 1
soma = 0

while div < num:
    if(num % div == 0):
        soma = soma + div
    div = div + 1

if soma == num:
    print(f"Perfeito")
else:
    print(f"Não perfeito")