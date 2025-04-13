cod = int(input("Insira o código do produto: "))
qt = int(input("Insira a quantidade do produto: "))

while(cod != 101 and cod != 102 and cod != 103 and cod != 104 and cod !=105):
    cod = int(input("Erro. Insira código válido"))

if(cod == 101):
    nome = "café"
    prod = qt * 0.25
    print(prod)

elif(cod == 102):
    nome = "meia de leite"
    prod = qt * 0.35
    print(prod)

elif(cod == 103):
    nome = "galão"
    prod = qt * 0.25
    print(prod)

elif(cod == 104):
    nome = "abatanado"
    prod = qt *0.40
    print(prod)

elif(cod == 105):
    nome ="carioca de limão"
    prod = qt * 1.10
    print(prod)

print(f"O total a pagar por essa quantidade de {nome} é {prod:.2f}€")
