print("************************")
print("Bem-Vindo ao jogo!")
print("************************")

numero_secreto = 50
total_de_tentativas = 3


for rodada in range( 1 , total_de_tentativas + 1  ):
    print(f"tentativa {rodada} de {total_de_tentativas}")
    chute = int(input("Digite um número entre 1 a 100: "))

    if (chute < 1 or chute > 100):
        print("Voce deve digitar um número entre 1 e 100!")
        continue
    acertou = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if acertou:
        print("Parabéns, você acertou!")
        break
    else:
        if(maior):
            print("você errou, o numero é maior que a resposta.")
        elif(menor):
            print("você errou, o numero é menor que a resposta.")


print("Fim de Jogo. ")