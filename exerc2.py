# todos os numeros impares entre valores

valor1 = int(input(" Digite o primeiro número: "))
valor2 = int(input(" Digite o segundo número: "))
cont = valor1
while cont <= valor2:
    numero = (cont % 2)
    if numero > 0:
       print(cont,end=" ")
    cont += 1