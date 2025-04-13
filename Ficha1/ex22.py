a = int(input("Insira um valor: "))
b = int(input("Insira um valor: "))
c = int(input("Insira um valor: "))

soma = a + b

if (soma > c):
    print(f"A soma de {a} + {b} é maior que {c}")

elif (soma < c):
    print(f"A soma de {a} + {b} é menor que {c}")

else:
    print(f"A soma de {a} + {b} é igual a {c}")