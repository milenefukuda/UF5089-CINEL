cod = int(input("Insira o código do produto desejado:"))
qt = int(input("Insira a quantidade desejada do produto:"))

while(cod != 101 and cod != 102 and cod !=103 and cod != 104 and cod != 105):
    cod = int(input("Erro. Insira um código do produto válido:"))

if(cod == 101):
    valorFinal = qt * 0.25

elif(cod == 102):
    valorFinal = qt * 0.35

elif(cod == 103):
    valorFinal = qt * 0.25

elif (cod == 104):
    valorFinal = qt * 0.40

elif (cod == 105):
    valorFinal = qt * 1.10

print(f"{valorFinal:.2f}€")
