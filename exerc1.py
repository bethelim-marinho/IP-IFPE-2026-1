# Receber numero,parar no negativo. Printar soma e média
cont = 0
soma = 0
while True:
    numero = int(input("informe um número: "))
    if numero >= 0:
        soma += numero
        cont += 1
        media = soma/cont
    else:
        print(f"Quantidade: {cont} | Soma: {soma} | Média: {media}")
        break