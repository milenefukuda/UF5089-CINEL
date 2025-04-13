num = int(input("Insira valor positivo: "))

div = 1 #candidato a ser divisor
soma = 0 #acumula as somas dos divisores à medida que encontra

while div <= num:
    resto = num % div
    if resto == 0:
        print(div) #mostra o valor do divisor
        soma = soma + div #adiciona valor do divisor à soma

    div = div + 1 #proximo candidato a divisor

print(f"A soma dos divisores é {soma}")