#Importando a biblioteca "random"
import random
#Pegar nome e status
input("Bem vindo ao rpg do justus, presione enter para continuar.")
nome=input("Qual é seu nome aventureiro/a: ")
forca=random.randint(1,10)
inteligencia=random.randint(1,10)
classe=0
#Definindo classe
if inteligencia>forca:
    print("Você é",nome,"o mago com muita inteligência.")
    classe=1
    hp=20
    danob=inteligencia
elif forca>inteligencia:
    print("Você é",nome,"o guerreiro com muita força.")
    classe=2
    hp=25
    danob=forca
elif forca==inteligencia:
    print("Você é",nome,"um arqueiro com a mesma quantidade de força e inteligência.")
    classe=3
    hp=20
    danob=(forca+inteligencia)/2
#Iniciando o jogo
input("Com seu personagem criado,clique enter para começar sua aventura.")
pergunta=""
resultado=0
while pergunta!="1" or pergunta!="2":
    pergunta=input("Voçê se encontra em frente de um enorme golem,você quer tentar distrair o golem com sua inteligência(1) ou tentar o derrubar para trás com sua força(2):")
    if not pergunta=="1" or pergunta==2:
        print("Responda com 1 ou 2!!!")
        break
#Criando variaveis da batalha
batalha=0
golem=50
dbgolem=3
cachorro=20
dbcachorro=5
acao=0
dano=0
#Definindo a batalha
if pergunta==1:
    resultado=random.randint(inteligencia,10)
elif pergunta==2:
    resultado=random.randint(forca,1)
if resultado<7:
    print("Seu plano falhou,você não consguiu passar pelo golem,prepare-se para uma batalha!")
    batalha=1
else:
    print("Você conseguiu e prossegue sua aventura")
    batalha=2
#Batalha
if batalha==2:
    print("A não,um cachorro com raiva chegou pra te atacar,preoaresse para uma batalha!")
    while cachorro>0 or hp>0:
        if cachorro<=0 or hp<=0:
            break
        acao=int(input("Você quer desviar ou atacar:").lower())
        if acao=="atacar":
            dano=danob*random.randint(1,3)
            dcachorro=dbcachorro*random.randint(1,3)
            print("Você ataca e dá",dano,"de dano")
            cachorro=cachorro-dano
            print("O cachorro te ataca e da",dcachorro,"de dano!")
            hp=hp-dcachorro
            print("Você está com",hp,"de hp")
            print("O cachorro está com",cachorro,"de hp")
        elif acao=="desviar":
            print("Você desvia,ninguém toma dano")
elif batalha==1:
    while golem>0 or hp>0:
        if golem<=0 or hp<=0:
            break
        acao=input("Você quer desviar ou atacar:").lower()
        if acao=="atacar":
            dano=danob*random.randint(1,3)
            dgolem=dbgolem*random.randint(1,3)
            print("Você ataca e dá",dano,"de dano")
            golem=golem-dano
            print("O golem te ataca e da",dgolem,"de dano!")
            hp=hp-dgolem
            print("Você está com",hp,"de hp")
            print("O golem está com",golem,"de hp")
        elif acao=="desviar":
            print("Você desvia,ninguém toma dano")
#Definindo vitória ou derrota
if cachorro>0 or golem>0:
    print("Você venceu,obrigado por jogar!!!!!")
elif hp<0:
    print("Você perdeu bobão hahaha.")