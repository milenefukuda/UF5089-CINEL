num = int(input("Insira um número positivo menor que 50: "))

while (num > 49) or (num < 1):
    num = int(input("Erro. Insira um número válido!"))

x = 1
fatorial = 1

while x <= num:
    fatorial = fatorial * x
    x = x + 1

print(f"O fatorial de {num} é {fatorial}")