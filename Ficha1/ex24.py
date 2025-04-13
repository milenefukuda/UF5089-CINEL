nome = input("Insira seu nome: ")
x, y, z = int(input("Insira suas três notas: \n")), int(input()), int(input())

media = x + y + z / 3

if media >=10:
    resultado = "Aprovado"

else:
    resultado = "Reprovado"

print(f"{nome} sua média foi de {media:.2f} e por isso estás {resultado}")