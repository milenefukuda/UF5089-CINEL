num = int(input("Escreva um número maior que 1:"))

while num < 2:
    num = int(input("Erro. Insira um número válido"))

div = 1
qt = 0

while div <= num:
    if(num % div == 0):
        qt = qt + 1
    div = div + 1

if qt == 2:
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")