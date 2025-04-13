num = int(input("Escreva um número positivo:"))

while num < 1:
    num = int(input("Erro"))

soma = 0
x = 1

while x <= num:
    soma = soma + x
    print(soma)
    x = x + 1
    input(f"soma={soma} e a seguir vai juntar o x={x}")


print(f"A soma é {soma}")