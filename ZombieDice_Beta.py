import random 
import sys
import copy
from os import remove
from ast import If, Try
from re import I
from typing import Counter

# Função para colorir criada pelo colega de curso Nicolas Melo e publicada no Discord
# pip install console-colorsys
def functionColorirTexto(color: str, text: str):
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CGREY    = '\33[90m'
    if color.lower() == "red":
        return CRED+text+CGREY
    elif color.lower() == "green":
        return CGREEN+text+CGREY
    elif color.lower() == "yellow":
        return CYELLOW+text+CGREY
    elif color.lower() == "blue":
        return CBLUE+text+CGREY
    elif color.lower() == "violet":
        return CVIOLET+text+CGREY

print(functionColorirTexto("green","\nPUCPR - Pontifícia Universidade Católica do Paraná"))
print(functionColorirTexto("green","Curso: Superior de Tecnologia em Gestão da Tecnologia da Informação"))
print(functionColorirTexto("green","Diciplina: Raciocínio Computacional"))
print(functionColorirTexto("green","Professor Tutor: Galbas Milleo Filho"))
print(functionColorirTexto("green","\nAluno: Edson Luiz Machado RA: 1112022208857"))
print(functionColorirTexto("green","\nProjeto da Disciplina: Implementação de jogo digital ZOMBIE DICE By Steve Jackson"))
print(functionColorirTexto("green","Estágio de Desenvolvimento: SEMANA 4 | ATIVIDADE SOMATIVA 1: Protótipo inicial\n"))

'''
     "..":  Perguntar ao Professor !? 
#    obs1:  anotações do programador, eu no caso :)
# #  obs2:  anotações do professor ou do check list a ser respondido
'''
# # Definição das variaveis globais de controle dos totais por jogador
# # Criou as variáveis para contabilizar os tiros, cérebros e passos adicionando na estrutura de repetição
jogadorContinua         = 0
jogadorNovaPartida      = 0
JogadorVerRegras        = 0
numeroJogadores         = 0
jogadorAtual            = 0
jogadorVenceu           = False
jogadorSaiu             = False
listaDadosCopo          = [] # "tabela" para copiar e manipular a listaDadosOriginal que serão usados;
listaMostraCopo         = [] # "tabela" para copiar e mostrar a listaDadosCopo por cor de dado;
listaDadosOriginal      = () # "tabela" para criar a tupla de dados originais imutáveis "constate";
listaContadorCerebros   = {} # "tabela" do tipo dicionário para contabilizar os totais por jogador
listaContadorTiros      = {} # "tabela" do tipo dicionário para contabilizar os totais por jogador
listaContadorPassos     = {} # "tabela" do tipo dicionário para contabilizar os totais por jogador

nomeJogoOriginal  = functionColorirTexto("red","ZOMBIE DICE")
nomeUniversidade  = functionColorirTexto("violet","Apoio PUCPR - Pontifícia Universidade Católica do Paraná | 2022.") # puxando o saco :)
nomeDesenvolvedor = functionColorirTexto("violet","By Edson Luiz Machado") # autopromoção por que sim, :) 

# # Esta utilizando funções para modularizar o código
# # Efetuou otimização no código seguindo boas práticas
def functionDarAdeus():
    print("\nEncerrando o jogo...\nPronto! Terminou.")
    print("\nAté breve!")
    print("\n"+nomeJogoOriginal + "\n")
    print(nomeDesenvolvedor)
    print(nomeUniversidade + "\n")    

# # Criou uma função para verificar se o jogador deseja parar ou continuar a jogar
def functionJogadorContinua():
    global jogadorContinua

    jogadorContinua = int(input("\n"  + functionColorirTexto("blue",str(nomeJogador)) + ", é você quem joga agora. \n "
                                + functionColorirTexto("green", "\nVocê vai continuar ou vai passar a vez de jogar ? \n ") + functionColorirTexto("violet","\nDigite> 1 (Jogar agora) ou 2 (passar a vez): "))) 

# Recarrega todas as opções de dados conforme listaDadosOriginal para (re)começar o jogo
# # termina (adicionado novamente os 13 dados no copo)
def functionCarregarDadosOriginais():
    global listaDadosOriginal

    # criando a lista de tipos por cor
    # # O caractere “C” na string corresponde ao cérebro, caractere “P” são os passos e por fim o “T” é o tiro.
    # # Modificou a estrutura dos dados de string para tupla
    ladosDadoVerde    = "CPCTPC" # constante 
    ladosDadoAmarelo  = "TPCTPC" # constante 
    ladosDadoVermelho = "TPTCPT" # constante 

    # criando lista de dados disponiveis
    listaDadosOriginal = ([
                ladosDadoVerde,ladosDadoVerde,ladosDadoVerde,ladosDadoVerde,ladosDadoVerde,ladosDadoVerde,
                ladosDadoAmarelo,ladosDadoAmarelo,ladosDadoAmarelo,ladosDadoAmarelo,
                ladosDadoVermelho,ladosDadoVermelho,ladosDadoVermelho ])   

# Carregar a listaDadosCopo com base no listaDadosOriginais
# # Utilizou uma estrutura para armazenar os dados do jogo (simular o copo)
# # Criou uma função para inicializar os dados no copo
def functionCarregarDadosCopo():
    global listaDadosCopo
    global listaDadosOriginal
    functionCarregarDadosOriginais
    
    listaDadosCopo *= 0
    del listaDadosCopo[:]
    functionCarregarDadosOriginais()
    random.shuffle(listaDadosOriginal)
    while (not len(listaDadosCopo) >=1):
        listaDadosCopo = listaDadosOriginal
    random.shuffle(listaDadosCopo)

# # Apresentar a quantidade de dados no copo, quais os dados que estão no copo
# # Utilizou uma estrutura para armazenar os dados do jogo (simular o copo)
# # Imprime na saída do console quais os dados que estão armazenados no copo 
# # Criou uma função para mostrar os dados que estão no copo
def functionMostrarDadosCopo():
    global listaDadosCopo
    global listaMostraCopo
    global functionRetornarCor
    
    i = 0
    listaMostraCopo *= 0
    del listaMostraCopo[:]
    # recebe a carga dos dados completos disponives listaDadosCopo
    for i in (listaDadosCopo):
        listaMostraCopo.append(functionRetornarCor(i))
    print("\nO copo tem agora " + str(len(listaMostraCopo)) + " dados, nas cores: ")
    print(*listaMostraCopo, sep = ", ")

# Limpar todos os contadores
# # Reinicia a lista que armazena os dados sempre que o turno de um jogador
# # Reinicia a pontuação de tiros na lista sempre que o jogador finalizar seu turno 
def functionLimparContadores():
    global listaDadosCopo
    global listaDadosOriginal
    global listaContadorCerebros
    global listaContadorPassos
    global listaContadorTiros

    listaContadorTiros.clear()
    listaContadorPassos.clear()
    listaContadorCerebros.clear()
        
# Define quem será o proximo jogador ainda vivo
def functionChamarJogador():
    global jogadorAtual
    global jogadorVenceu
    global nomeJogador
    global listaDadosCopo
    global listaJogadores
    global listaDadosOriginal
    global listaContadorPassos
    global listaContadorTiros
    global functionCarregarDadosOriginais

    # # No seu turno após lançar os dados o jogador pode decidir parar ou continuar a jogar. 
    # # Caso decida parar você contabiliza os cérebros para próxima jogada, já os dados de tiro são zerados para próxima rodada
    listaContadorPassos[nomeJogador] = 0 # zera os contadores de passos para a proxima rodada
    listaContadorTiros[nomeJogador] = 0 # zera os contadores de tiros para a proxima rodada
    jogadorAtual = jogadorAtual + 1
    if (jogadorAtual >= len(listaJogadores)):
        jogadorAtual = int(0)
    # Define o nomeJogador da listaJogadores atual
    nomeJogador = listaJogadores[int(jogadorAtual)]   

# # Mensagem para informar que o jogador perdeu
# # Criou uma função para verificar se o jogador jogador ganhou ou perdeu               
def functionRemoverJogador():
    global jogadorVenceu
    global nomeJogador
    global jogadorAtual
    global listaJogadores
    global functionChamarJogador

    print("\n" + functionColorirTexto("blue",str(nomeJogador)) + ", você "+ functionColorirTexto("red","morreu!!!\n"))
    listaJogadores.remove(nomeJogador) # Remove jogador que morreu
    jogadorAtual = jogadorAtual - 1
    nomeJogador = listaJogadores[int(jogadorAtual)]
                
    print("Jogadores que ainda estão na disputa: ")
    print(*listaJogadores, sep = ", ")
                    
    # Verificar se tem mais jogadores, se não tem, acabou a partida
    if len(listaJogadores) <= 1:
        jogadorVenceu = True # vai acionar o else do while principal
        jogadorAtual = 0
    else:
        jogadorVenceu = False

# # Implementou a rotina para sortear os dados (selecionar três dados)    
# # Implementou a rotina para jogar os dados (sortear a tipo de um dos dados)
# # Criou uma função para pegar cada um dos dados (verde, amarelo e vermelho)
# # Criou uma função para remove os dados do copo (remover da lista em cada jogada)
# # Criou uma função para lançar os dados (sortear a face do dado )
# # Imprime na saída do console a face de cada um dos dados sorteados
# # calcula pontuação atual e remove o dado sorteado do tipo "C" e "T" para o turno atual
# # Armazena a pontuação dos jogadores na lista (quantidade de cérebros e tiros)
# # Remove os dados da lista em cada jogada
def functionSortearDados():
    global functionRetornarCor
    global functionRetornarMensagem
    global listaContadorPassos
    global listaContadorCerebros
    global listaContadorTiros
    global listaDadosCopo   
    i = 0
    p = 0
    print("\nOs dados sorteados aleatóriamente foram: ")
    
    # Verifica se teve dados do tipo "P" usar eles na proxima rolagem 
    if listaContadorPassos.get(nomeJogador,0):
        p =  listaContadorPassos.get(nomeJogador,0) # pega o total de passos acumulados
        listaContadorPassos[nomeJogador] = 0 # limpa contador de passos do jogador
    while (i <= 2):
        i = i + 1
        # aplicar regra para quando tiver dados do tipo "P" usar o mesmo dado proxima rolagem 
        if p >= 1:
            marcador = p
            p = p - 1
        else:
            random.shuffle(listaDadosCopo) 
            marcador = random.randint(0,len(listaDadosCopo)-1)

        escolhido = listaDadosCopo[int(marcador)] # pegou o dado conforme a posicao short 
        lado = escolhido # pega um dado já sorteado
        cor = functionRetornarCor(str(lado)) # descobre a cor do dado
        letra = random.randint(0,5) # sorteia uma posicao de 0,5
        tipo = str(lado[int(letra)]) # pega o valor da posicao short
        jogada = functionRetornarMensagem(tipo) # mostra ao jogador qual foi sua jogada

        print(cor + " com o lado virado para o " + jogada) 
        if tipo == "C":
            if listaContadorCerebros.get(nomeJogador,0):
                listaContadorCerebros[nomeJogador] = int(listaContadorCerebros.get(nomeJogador,0)) + 1
            else:
                listaContadorCerebros[nomeJogador] = 1
            if(escolhido in listaDadosCopo): # remove da listaDadosCopo no turno por que comeu um cerebro
                listaDadosCopo.remove(escolhido)
        elif tipo == "T":
            if listaContadorTiros.get(nomeJogador,0):
                listaContadorTiros[nomeJogador] = int(listaContadorTiros.get(nomeJogador,0)) + 1 # deixar 0 para testes de loop
            else:
                listaContadorTiros[nomeJogador] = 1
            if(escolhido in listaDadosCopo): # remove da listaDadosCopo no turno por que tomou tiro
                listaDadosCopo.remove(escolhido)
        elif tipo == "P":
            if listaContadorPassos.get(nomeJogador,0):
                listaContadorPassos[nomeJogador] = int(listaContadorPassos.get(nomeJogador,0)) + 1
            else:
                listaContadorPassos[nomeJogador] = 1
        else:
            print("Erro: tipo de dado não definido!!!\n") 
        
# # Mensagem para apresentar a quantidade de cérebros que o jogador possui
# # Mensagem para apresentar a quantidade de tiros que o jogador levou
# # Mensagem para apresentar a quantidade de passos de vítimas que fugiu
# # Criou uma função para apresentar a pontuação do jogo
def functionMostrarScore():
    global nomeJogador

    print("\n" + functionColorirTexto("blue",str(nomeJogador)) + ", o seu SCORE atual nesse TURNO é: \n")
    print(functionColorirTexto("yellow","CÉREBROS: ")  + str(listaContadorCerebros.get(nomeJogador,0)))
    print(functionColorirTexto("red","TIROS: ")     + str(listaContadorTiros.get(nomeJogador,0)))
    print(functionColorirTexto("green","PASSOS: ")    + str(listaContadorPassos.get(nomeJogador,0)))

# # Mensagem que o jogador comeu 1 cérebro
# # Mensagem que o jogador levou 1 tiro
# # Mensagem que a vitima escapou, o jogador deverá lançar este dado novamente
def functionRetornarMensagem(quetipo):
    
    if quetipo == "C":
        msg = "(C) CÉREBRO (Parabéns!!! Você comeu um cérebro.)"
    elif quetipo == "T":
        msg  = "(T) TIRO (Deu Ruim!!! Você levou um tiro.)"
    elif quetipo == "P":
        msg = "(P) PASSOS (Deu Ruim!!! Uma vítima escapou.)"
    else:
        msg = "Atenção! tipo de dado não encontrado"
    return msg

# # Criou uma função para mostrar a cor dos que foram sorteados
# # Imprime na saída do console a cor de cada um dos três dados sorteados
def functionRetornarCor(todascombinacoes):

    if (todascombinacoes == "CPCTPC"):
        cor ="VERDE"
    elif (todascombinacoes == "TPCTPC"):
        cor ="AMARELO"
    elif (todascombinacoes == "TPTCPT"):
        cor ="VERMELHO"
    else:
        cor = "Não foi possível identificar a cor pela combicação informada!!!"
    return cor    

# -------------------------------------------------------------------------------------- #
#                                                                                        #
#                                     START do JOGO                                      #
#                                                                                        #
# -------------------------------------------------------------------------------------- #

print("# ------------------------------------------------------------------------- #")
print("|                                                                           |")
print("|                                "+nomeJogoOriginal+"                                |")
print("|                          "+nomeDesenvolvedor+"                            |")
print("|                                                                           |")
print("# ------------------------------------------------------------------------- #\n")

print(functionColorirTexto("violet","Seja Bem Vindo ao Zombie Dice!"))
print(functionColorirTexto("red","\nDevore cérebros. Não leve um tiro na cabeça...\n"))

# # Mensagem para perguntar se o jogador quer ver as regras do jogo
JogadorVerRegras = int(input(functionColorirTexto("green", "\nGostaria de ver as regras do jogo? \n ") + functionColorirTexto("violet","\nDigite> 1 (SIM) ou 2 (NÃO): ")))
if (JogadorVerRegras == 1):

    print("\nNeste jogo o jogador é um zumbi faminto por cérebros, que deve comer mais cérebros que seus amigos, porém, cuidando com os tiros de espingarda.")
    print("\nDinâmica do Jogo:  \nO jogo é composto por um copo que armazena 13 dados de 6 tipos. \nExistem 3 tipos de dados diferentes: verdes, vermelhos e amarelos.") 
    print("Os dados possuem 3 símbolos diferentes (tiro, cérebro e passos).")
    print("Os dados vermelhos são os mais difíceis, possuem um número maior de tipos com o símbolo tiro.") 
    print("Os verdes são os mais fáceis, o maior número de tipos do dado é de cérebro.") 
    print("Os dados amarelos são intermediários os tipos dos dados possuem a mesma quantidade cérebros, tiros e passos.") 
    print("Em uma rodada, cada jogador tem um turno para jogar.") 
    print("No turno, o jogador deve pegar aleatoriamente 3 dados do copo e lançar, sempre os três dados juntos.") 
    print("Quando o tipo do dado cair virado com símbolo para ""cérebro"", é porque o jogador comeu um cérebro.") 
    print("Caso o tipo do dado cair virado com o símbolo para ""passos"", a vítima fugiu, se o jogador decidir continuar a lançar os dados em seu turno, os dados que caíram com o tipo para “passos” deverão ser lançados novamente.") 
    print("Para lançar novamente os três dados o jogador completa a quantidade retirando outros dados do tubo, sempre lançando os três dados.") 
    print("O objetivo é comer 13 cérebros para vencer o jogo, no entanto, existem os tiros de espingarda! Se por acaso o jogador levar três tiros de espingarda ele perde e sai do jogo.")
    print("No seu turno, após lançar os dados, o jogador pode decidir parar ou continuar a jogar.") 
    print("Caso decida parar, você contabiliza os cérebros para próxima jogada, já os dados de tiro são zerados para próxima rodada.")
elif (JogadorVerRegras == 2):
    print("\nCarregando o jogo no seu computador...\nPronto! \nVamos começar...\n")
else:
    print(functionColorirTexto("red","\nErro: Opção inválida, tente novamente..."))

# # Implementou a lógica e a jogabilidade do jogo
# # Utilizou as estruturas repetição (for e while)
# # Realiza a Interação do jogador utilizando a estrutura de repetição

# -------------------------------------------------------------------------------------- #
#                                                                                        #
#                                      PLAY do JOGO                                      #
#                                                                                        #
# -------------------------------------------------------------------------------------- #

while (not jogadorSaiu):

    jogadorNovaPartida = int(input(functionColorirTexto("green", "\nVamos jogar uma nova partida ? \n ")+ functionColorirTexto("violet","\nDigite> 1 (SIM) ou 2 (SAIR): ")))
    if (jogadorNovaPartida == 1):

        # # Mensagem para solicitar a quantidade de jogadores
        # # Implementou a entrada para receber a quantidade de jogadores
        # # Efetua checagem se foi adicionado pelo menos dois jogadores
        jogadorVenceu = False
        numeroJogadores = 0
        while (numeroJogadores < 2 ):
            print(functionColorirTexto("red", "\nAtenção! São necessários no minimo dois jogadores!!!"))
            numeroJogadores = int(input("\nEntre com a quantidade de jogadores: "))

        else:
            print("\nOK, vamos começar o jogo...\n")

            # Criando a lista de jogadores (Passo 2)
            # # Utilizou uma estrutura para armazenar os jogadores
            listaJogadores = []
            for i in range(numeroJogadores):
                if i > numeroJogadores: 
                    break

                # Usando o append() para incluir jogadores na lista
                nomeJogador = input("Qual o nome do " + str(i + 1) + "º jogador ? :")
                listaJogadores.append(nomeJogador)
            else:
                # após imprimir a lista de jogadores, dar uma mensagem de borá lá :)
                print(functionColorirTexto("red","\nAgora vocês são Zombies, vamos começar a comer Céeeeerebros!\n"))
        
                # Recarrega todas os dados conforme listaDadosOriginal e começar o jogo
                functionCarregarDadosOriginais #carregar todos os dados originais
                functionCarregarDadosCopo() #carrega os dados para jogar o turno 
                functionLimparContadores() #limpar todas as listas de contadores

        # # Criou uma função para verificar se o jogador jogador ganhou ou perdeu
        while (not jogadorVenceu):

            # Define o primeiro jogador da listaJogadores e seguimos daqui
            nomeJogador = listaJogadores[int(jogadorAtual)]
            
            # # Mensagem para informar usuário informando que o copo está vazio
            if ((len(listaDadosCopo)) + (listaContadorPassos.get(nomeJogador,0))) <= 3:
                # Jogador atual vai passar a vez para o proximo nomeJogador 
                # Perguntar ao professor? 
                ''' Se o copo estiver vazio ou -3 dados obrigatórios para lançar, o 
                    jogador passa a vez para o proximo jogador vivo ?! '''
                print("\nAtenção! O copo tem menos que 3 dados para jogar, você perdeu a vez! \n")
                functionChamarJogador() #define qual o proximo nomeJogador
                functionMostrarScore() #mostrar score atual (depois)
                functionCarregarDadosCopo() #recarrega os 13 dados originais

            # # Mensagem para perguntar se o jogador ainda quer continuar a lançar dos dados    
            functionJogadorContinua() 
            if (jogadorContinua == 1):
                print("\n"  + functionColorirTexto("blue",str(nomeJogador))   
                            + ", decidiu continuar! ele tirou 3 dados do copo e está rolado os dados...")
                # # Implementou a rotina para jogar os dados dentro da estrutura de repetição
                functionSortearDados() #sortear dados aleatoriamente
                functionMostrarScore() #mostrar score atual (depois)
                functionMostrarDadosCopo() #mostra os dados que restaram no copo 

                # # Mensagem para informar que o jogador VENCEU porque atingiu 13 cerébros
                if listaContadorCerebros.get(nomeJogador,0) >= 13:
                    jogadorVenceu = True # vai acionar o else do while principal
                else:
                    # # Mensagem para informar que o jogador MORREU
                    if listaContadorTiros.get(nomeJogador,0) >= 3:
                        functionRemoverJogador() # Remove jogador que morreu
                        functionChamarJogador() # define qual o proximo jogador
                        functionMostrarScore() #mostrar score atual (depois)
                        functionCarregarDadosCopo() #recarrega os 13 dados originais
            
            elif (jogadorContinua == 2):
                # o jogqador PASSOU a VEZ para outro usuário usando a opção 2(Não)
                print(functionColorirTexto("blue", str(nomeJogador)) + ", tá com " + functionColorirTexto("red", "medinho") +" e passou a vez!")
                functionCarregarDadosCopo() #recarrega os 13 dados originais
                functionChamarJogador() # define qual o proximo jogador
                functionMostrarScore() #mostrar score atual (depois)

            else:
                print(functionColorirTexto("red", "\nErro: Opção inválida, tente novamente..."))

        else:
            # # Mensagem para informar que o jogador VENCEU
            # # Criou uma função para verificar se o jogador jogador ganhou ou perdeu               
            print("\nParabéns " + functionColorirTexto("blue",str(nomeJogador)) + ", você " + functionColorirTexto("violet","venceu!!!\n"))
            print("Fim do Jogo!\n")
            functionLimparContadores() #clear em todas as listas
    
    elif(jogadorNovaPartida == 2):
        jogadorSaiu = True
        
    else:
        print(functionColorirTexto("red", "\nErro: Opção inválida, tente novamente..."))
else:
    functionDarAdeus() 
# -------------------------------------------------------------------------------------- #
#                                                                                        #
#                                       FIM do JOGO                                      #
#                                                                                        #
# -------------------------------------------------------------------------------------- #
