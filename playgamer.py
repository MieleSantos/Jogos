from gamers import forca
#from gamers import  adivinhacao

print("*********************************")
print("Informe o numero para opção do jogo!")
print("*********************************")

print("\n(1) Adivinhação!")

# print("\n(1) Forca\n(2) Adivinhação!")

jogo = int(input("Qual jogo dejesa joga? "))

#Definindo qual jogo foi selecionado e executando
if(jogo == 1):
    print("Iniciando o jogo da Forca")
    forca.jogar()

# elif(jogo == 2):
#     print("Iniciando o jogo da adivinhação")
#     adivinhacao.jogar()
