num = int(input("Insira um número positivo:"))

while num < 1:
    num = int(input("Erro."))

div = 1
soma = 0

while div <= num:
    if num % div == 0:
        soma = soma + div
    div = div + 1

print(f"A soma de {num} é {soma}")
