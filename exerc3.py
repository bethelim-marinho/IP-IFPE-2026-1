# maiores de idade e a media da idade
qtd_pessoa = int(input(" Digite a quantidade pessoas: "))
cont = qtd_pessoa
soma_idades = 0
maior = 0

while cont != 0:
    idade = int(input(" Digite a idade: "))
    soma_idades += idade
    if idade >= 18:
        maior += 1
    cont -= 1
    media = soma_idades/qtd_pessoa
print(f"Maiores: {maior} | Média: {media}")
    
