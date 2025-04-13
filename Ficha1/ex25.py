nome = input("Escreva seu nome:")
nota = int(input("Escreva sua nota:"))

resultado=""

if nota <= 49:
    resultado = "Insuficiente"
elif nota <=63:
    resultado ="Suficiente"
elif nota <= 84:
    resultado ="Bom"
else:
    resultado="Excelente"

print(resultado)