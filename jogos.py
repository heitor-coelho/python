import forca
import jogo_da_adivinhacao

print("*******************")
print("Jogos!")
print("*******************")

print("[1] Forca  [2] adivinhação")
jogo = int(input("Escolha seu jogo!"))

if jogo == 1:
    print("Jogando Forca.")
    forca.jogar()
elif jogo == 2:
    print("jogando adivinhação.")
    jogo_da_adivinhacao.jogar()


