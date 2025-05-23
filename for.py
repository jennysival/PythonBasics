# A Hello Kitty resolveu organizar uma festa para seus amigos da Sanrio e vai distribuir presentinhos!
# Ela quer que você a ajude a escrever um programa que:
# Leia um número inteiro positivo N, que representa a quantidade de convidados.
# Depois, usando uma estrutura de repetição for, exiba uma mensagem personalizada de entrega de presente para cada convidado, numerando de 1 até N.

convidados = 15

for x in range(1, convidados + 1):
    print("Entregando presente para o convidado ", x)

# Você é responsável por um aquário de peixes coloridos. Sua missão é escrever um programa que:
# Peça para o usuário digitar um número inteiro, que representa a quantidade de peixes no aquário.
# Para cada peixe (de 1 até N), use um laço for para numerá-los.
# Se o número do peixe for par, o programa deve dizer que ele é um peixe Azul.
# Se for ímpar, diga que ele é um peixe Rosa.
# Ao final, mostre quantos peixes azuis e quantos peixes rosas havia no aquário.

quantidade = int(input("Digite quantos peixes tem no seu aquário: "))
rosa = 0
azul = 0

for i in range(1, quantidade + 1):
    if i % 2 == 0:
        azul += 1
        print("Peixe", i, "é azul!")
    else:
        rosa += 1
        print("Peixe", i, "é rosa!")
