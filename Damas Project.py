import os
import platform
# -------------------------------------------------------------------------
#|                          Jogo de Damas                                  |
#| Projeto proposto na disciplina de Algoritmos e programação              |
#| Desenvolvido por Rafael Trajano Ferreira e Paulo Henrique Santos Felipe |
#| Data de inicio: 01/12/2022                                              |
#| Ultima modificação: 22/12/2022                                          |
# -------------------------------------------------------------------------

#Variáveis contendo valores UNICODE que são responsáveis pela coloração das letras de output
#Regras de uso:
RED= "\033[1;31m"   #Erros do usuário
BOLD = "\033[;1m"   #Destaque de alguma letra de instrução
CYAN = "\033[1;36m" #Informação de apoio ao usuário
GREEN= "\033[0;32m" #Declaração de vitória
RESET = "\033[0;0m" #Uso obrigatorio pós fim de uso de qualquer outra cor, para que não interfira nas proximas letras coloridas
#------------------------------------------------------------------------------------------
#A matriz abaixo é o elemento chave do projeto, pois é nela que tudo vai se processar
pecas = [["-",0,"-",0,"-",0,"-",0],[0,"-",0,"-",0,"-",0,"-",],["-",0,"-",0,"-",0,"-",0],[" ","-"," ","-"," ","-"," ","-"],["-"," ","-"," ","-"," ","-"," "],[1,"-",1,"-",1,"-",1,"-"],["-",1,"-",1,"-",1,"-",1],[1,"-",1,"-",1,"-",1,"-"]]
#------------------------------------------------------------------------------------------
#Função responsável por traduzir as informações da matriz para um tabuleiro visual
def geratab (vez,matriz,cont_br,cont_pr):
        #---------Indices e topo do tabuleiro------------
        print("   1 2 3 4 5 6 7 8", " |-----------------|", sep = "\n")
        x = 0
        #---------Geraçao do tabuleiro em geral-----------
        for i in range(len(matriz)):
            x += 1
            print(x, end = "")
            #-------Print dos elementos do tabuleiro---------
            for j in range(len(matriz[i])):
                if j == (0):
                    print("|", end= " ")
                if j == (len(matriz[i]) - 1):
                    if i == 3 and j == 7:     
                        print(matriz[i][j],"|", BOLD+"Quantidade: brancas", cont_br, "x", "pretas"+RESET, cont_pr)
                    else: 
                        print(matriz[i][j],"|")
                else:
                    print(matriz[i][j],end=" ")  
        #Aqui fica a impressão do placar do jogo
        print(" |-----------------|")
        if vez == 1:
            print(CYAN+"Vez das peças Pretas"+RESET)
        else:
            print(CYAN+"Vez das peças Brancas"+RESET)
#------------------------------------------------------------------------------------------
#Função responsável pela coordenação da vez de jogada (alternando entre branco e preto)
def jogador(contador):
    if contador % 2 == 0:
        return(1)
    else:
        return(0)
#------------------------------------------------------------------------------------------
#Função responsável pelos números do placar do jogo
def placar(matriz):
    cont_branca = 0
    cont_preta = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                cont_branca += 1
            elif matriz[i][j] == 1:
                cont_preta += 1
    return(cont_branca,cont_preta)
#------------------------------------------------------------------------------------------
#Função para limpar a tela para que as mensagens de erro nao atrapalhem o jogo
def erro(msgerro):
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    geratab(vez,pecas,qtd_pecas[0],qtd_pecas[1])
    print(RED+msgerro+RESET)
#------------------------------------------------------------------------------------------
#Funçao que recebe,processa e armazena a peça que o usuário quer mover
def seleciona_jogada(matriz):
    while True:
        #Tipos de erros e suas mensagens
        erro_1 = "Você deve digitar um numero inteiro!"
        erro_2 = "Cuidado, voce nao pode mover o invisivel!"
        erro_3 = "Opa, voce nao pode mover esta peça, cuidado com a vez de jogada!"
        erro_4 = "Intervalo inválido. Tente novamente"
        #Entradas com verificações de apenas numeros inteiros
        try:
            l = int(input("Digite a linha da peça que quer mover ou digite -1 para sair: "))
        #Supondo que o usuário queira retornar por qualquer outro motivo
            if l == -1:
                print(BOLD+"Fim de jogo"+RESET)
                return(l)
        except:
            erro(erro_1) #Você deve digitar um numero inteiro!
            continue
        try:
            c = int(input("Digite a coluna da peca que quer mover: "))
        except:
            erro(erro_1) #Você deve digitar um numero inteiro!
            continue
        #Verificaçao se os inteiros estão do intervalo permitido
        if (l >= 1 and l <=8) and (c >= 1 and c <=8):
            #Verificação se o usuário não está tentando mover peça do adversário
            if vez == matriz[l-1][c-1]:
                return (l-1, c-1)
            #erro de tentar mover um local vazio
            elif matriz[l-1][c-1] == "-" or matriz[l-1][c-1] == " ":
                erro(erro_2)   #Cuidado, voce nao pode mover o invisivel!
            else:
                erro(erro_3)   #Opa, voce nao pode mover esta peça, cuidado com a vez de jogada!
        else:
            erro(erro_4)    #Intervalo inválido. Tente novamente
#------------------------------------------------------------------------------------------
#Função responsável pelas movimentações comuns e de captura(coração do projeto)       
def movimentacao(peca_selecionada,pecas,vez):
    l1 = peca_selecionada[0]
    c1 = peca_selecionada[1]
    #Tipos de erros e suas mensagens
    erro_1 = "Você deve digitar um numero inteiro!"
    erro_2 = "ALÔ JOGADOR(A) DAS PEÇAS BRANCAS, SEU OPONENTE ESTÁ TENTANDO TRAPACEAR"
    erro_3 = "ALÔ JOGADOR(A) DAS PEÇAS PRETAS, SEU OPONENTE ESTÁ TENTANDO TRAPACEAR"
    erro_4 = "Voce está tentando capturar de forma errada"
    erro_5 = "Movimento incorreto, tente novamente"
    erro_6 = "Intervalo incorreto, tente novamente"
    while True:
        #Entradas com verificaçoes de apenas números inteiros
        try:
            l2 = int(input("Digite a linha para onde quer mover a peça ou pressione -2 para retornar: "))
        #Supondo que o usuário queira retornar por qualquer motivo
            if l2 == -2:
                return(-2)
        except:
            erro(erro_1) #Você deve digitar um numero inteiro!
            continue
        try:
            c2 = int(input("Digite a coluna para onde quer mover a peça: "))
        except:
            erro(erro_1) #Você deve digitar um numero inteiro!
            continue
        l2 -= 1
        c2 -= 1
        #Condições de possiveis tipos de capturas baseados na rosa dos ventos,
        #Reservado em variaveis para facilitar a visualização
        #-------------------------------------------
        nordeste = ((l1-2) == l2 and (c1+2) == c2)
        sudoeste = ((l1+2) == l2 and (c1-2) == c2)
        sudeste = ((l1+2) == l2 and (c1+2) == c2)
        noroeste = ((l1-2) == l2 and (c1-2) == c2)
        #-------------------------------------------
        #Condições das movimentações padrões de peças brancas e pretas
        branco = ((l2 == l1+1) and (c2 == c1-1)) or ((l2 == l1+1) and (c2 == c1+1))
        preto = ((l2 == l1-1) and (c2 == c1-1)) or ((l2 == l1-1) and (c2 == c1 + 1))
        #----------------------------------------------------------------------------
        #verificaçao se ele nao ultrapassa as bordas
        if (l2 >= 0 and l2 <=7) and (c2 >= 0 and c2 <=7):
            #verificaçao se ele nao tenta mover a mais ou voltar para trás
            if (vez == 1 and preto) or (vez == 0 and branco):
                #verificaçao se o local alvo está livre para movimentar a peça selecionada até lá
                if pecas[l2][c2] == " ":
                    pecas[l2][c2] = vez
                    pecas[l1][c1] = " "
                    break
            #Caso o movimento nao obedeça "Branco" ou "Preto" ele pode ser considerado um movimento de captura
            #caindo na condição abaixo e ocorrendo as verificações necessárias para a captura
            if pecas[l2][c2] == " ":
                #Captura Nordeste 
                if nordeste and (pecas[l1-1][c1+1] != vez and pecas[l1-1][c1+1] != "-" and pecas[l1-1][c1+1] != " "):
                    pecas[l1-1][c1+1] = " "
                    pecas[l2][c2] = vez
                    pecas[l1][c1] = " "
                    break
                #Captura Sudoeste 
                elif sudoeste and (pecas[l1+1][c1-1] != vez and pecas[l1+1][c1-1] != "-" and pecas[l1+1][c1-1] != " "):
                    pecas[l1+1][c1-1] = " "
                    pecas[l2][c2] = vez
                    pecas[l1][c1] = " "
                    break
                #Captura Sudeste 
                elif sudeste and (pecas[l1+1][c1+1] != vez and pecas[l1+1][c1+1] != "-" and pecas[l1+1][c1+1] != " " ):
                    pecas[l1+1][c1+1] = " "
                    pecas[l2][c2] = vez
                    pecas[l1][c1] = " "
                    break
                #Captura Noroeste 
                elif noroeste and (pecas[l1-1][c1-1] != vez and pecas[l1-1][c1-1] != "-" and pecas[l1-1][c1-1] != " "):
                    pecas[l1-1][c1-1] = " "
                    pecas[l2][c2] = vez
                    pecas[l1][c1] = " "
                    break
                else: 
                    #Verificações se o usuário não tenta avançar duas casas de uma vez com alerta de 
                    #trapaça e de captura incorreta (caso tente passar pro cima de uma peça propria)
                    if vez == 1:
                        try:
                            if pecas[l1-1][c1+1] == " " or pecas[l1-1][c1-1] == " ":
                                erro(erro_2) #ALÔ JOGADOR(A) DAS PEÇAS BRANCAS, SEU OPONENTE ESTÁ TENTANDO TRAPACEAR
                            else:
                                erro(erro_4) #Voce está tentando capturar de forma errada
                        except:
                            erro(erro_4)
                    elif vez == 0:
                        try:
                            if pecas[l1+1][c1+1] == " " or pecas[l1+1][c1-1] == " ":
                                erro(erro_3) #ALÔ JOGADOR(A) DAS PEÇAS PRETAS, SEU OPONENTE ESTÁ TENTANDO TRAPACEAR
                            else:
                                erro(erro_4) #Voce está tentando capturar de forma errada
                        except:
                            erro(erro_4)
            #Caso nao seja nem captura nem movimento comum, então é um movimento incorreto
            else:
                erro(erro_5) #Movimento incorreto, tente novamente
                continue
        #Caso o usuário insira um número menor ou maior que o permitido a mensagem de erro é essa:
        else:
            erro(erro_6) #Intervalo incorreto, tente novamente
#------------------------------------------------------------------------------------------
#A partir daqui inicia-se o jogo de maneira geral fazendo a chamada de funçoes e etc.
contador = 1
while True:
    #Qtd_pecas[0] = Pecas brancas
    #Qtd_pecas[1] = Pecas pretas
    qtd_pecas = placar(pecas)
    vez = jogador(contador)
    #Redesenhamento do terminal após uma jogada
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    geratab(vez,pecas,qtd_pecas[0],qtd_pecas[1])
    #------------------------------------------------
    #declaração do vencedor da partida
    if qtd_pecas[0] == 0:
        print(GREEN+"Pretas venceram o jogo!"+RESET)
        break
    if qtd_pecas[1] == 0:
        print(GREEN+"Brancas venceram o jogo!"+RESET)
        break
    #------------------------------------------------
    #Condições em que o usuário decide voltar a seleção da peça ou do movimento
    peca_selecionada = seleciona_jogada(pecas)
    if peca_selecionada == -1:
        break
    if movimentacao(peca_selecionada,pecas,vez) == -2:
        continue
    else:
        contador += 1
