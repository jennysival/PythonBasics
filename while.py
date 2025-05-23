# Escreva um programa que leia um grupo de valores (não sabemos quantos são) para calcular e visualizar a
# média desses valores e, também, determinar e visualizar o maior deles. Utilize uma estrutura de repetição
# while ou for.

soma = 0
quantidade = 0
maior = 0
continuar = True

while continuar:
    nota = int(input("Digite sua nota do bimestre ou digite 0 para encerrar: "))
    if(nota == 0):
        continuar = False
        # aqui poderia ser um break
    else:
        soma += nota
        quantidade += 1

    if(nota > maior):
        maior = nota

media = soma/quantidade
print("Sua média de notas é ", media)
print("Sua maior nota foi ", maior)
