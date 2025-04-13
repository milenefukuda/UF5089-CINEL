a, b, c = int(input("Insira as medidas dos três lados: ")), int(input()), int(input())

if(a == b == c):
    print("O triângulo é equilátero")

elif(a == b) or (b == c) or (a == c):
    print("O triângulo é Isóscele")

else:
    print("O triângulo é escaleno")