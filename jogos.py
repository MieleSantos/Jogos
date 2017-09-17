import forca
import  Adivinhacao

print("*********************************")
print("Escolha o seu jogo!")
print("*********************************")

print("(1) Forca\n(2)Adivinhação!")

jogo= int(input("Qual jogo dejesa joga? "))

if(jogo ==1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    Adivinhacao.jogar()