num = int(input("Insira um número igual ou maior que 2: "))

while num <=2:
    num = int(input("Erro."))

copia = num
soma = 0

while num > 0:
    resto = num % 10
    soma = soma + resto
    num = num // 10

print(f"A soma do número {copia} é {soma}")