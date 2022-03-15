"""
PROJETO GENIUS:
Objetivo: recriar o programa que rode o jogo genius
"""
import random
import pygame
import time
import playsound
from pygame.locals import *

def escolher_cor_aleatoria():
    pisca_vermelho = {'cor':cor_vermelho, 'posicao': (251,282),'raio':130}
    pisca_verde = {'cor':cor_verde, 'posicao':(251,282),'raio':130}
    pisca_azul = {'cor':cor_azul, 'posicao':(251,282),'raio':130}
    pisca_laranja = {'cor':cor_laranja, 'posicao':(251,282),'raio':130}
    cores = [pisca_laranja,pisca_azul,pisca_verde,pisca_vermelho]
    return random.choice(cores)

def piscar_cores(lista_cores):
    for cor in lista_cores:
        #desenhar 1/4 de círculo com a cor correta
        if cor['cor'] == cor_verde:
            pygame.draw.circle(interface,cor['cor'],cor['posicao'],cor['raio'],draw_top_right= True)
        elif cor['cor'] == cor_vermelho:
            pygame.draw.circle(interface,cor['cor'],cor['posicao'],cor['raio'],draw_bottom_right= True)
        elif cor['cor'] == cor_laranja:
            pygame.draw.circle(interface,cor['cor'],cor['posicao'],cor['raio'],draw_bottom_left= True)
        elif cor['cor'] == cor_azul:
            pygame.draw.circle(interface,cor['cor'],cor['posicao'],cor['raio'],draw_top_left= True)
        pygame.display.update()
        time.sleep(0.4) #tempo para mostrar a próxima cor
        interface.blit(fundo,(0,30))    #retorna à imagem anterior
        pygame.display.update()
        time.sleep(0.4) #tempo para a cor ficar apagada

def obter_resposta(quantidade_cores):
    resposta_usuario = []   #armazena a resposta
    while quantidade_cores > 0:
        #aguarda a resposta do usuário
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_verde.collidepoint(mouse):
                    resposta_usuario.append(cor_verde)
                    quantidade_cores -= 1
                elif botao_laranja.collidepoint(mouse):
                    resposta_usuario.append(cor_laranja)
                    quantidade_cores -= 1
                elif botao_vermelho.collidepoint(mouse):
                    resposta_usuario.append(cor_vermelho)
                    quantidade_cores -= 1
                elif botao_azul.collidepoint(mouse):
                    resposta_usuario.append(cor_azul)
                    quantidade_cores -= 1
    return resposta_usuario

def restart():
    texto_jogar_novamente = fonte_botoes.render('RESTART', True, cor_preto) #texto do botão restart
    interface.blit(fundo, (0,30))
    botao_jogar_novamente =pygame.draw.rect(interface,cor_branco,(175,70,155,60))
    interface.blit(texto_jogar_novamente,(176,73))
    pygame.display.update()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_jogar_novamente.collidepoint(mouse):
                    interface.blit(fundo,(0,30))    #volta para a imagem inicial
                    pygame.display.update()
                    return True

playsound.playsound('musica_tema.mp3', block = False)

pygame.init()   #inicialização do pygame
interface = pygame.display.set_mode((500,530))  #definindo o tamanho da interface, passando largura e altura
fonte_botoes = pygame.font.SysFont('Arial', 40) #definindo a fonte dos botões
fonte_contagem = pygame.font.SysFont('Arial', 30)   #definindo a fonte da barra de status da contagem
barra_status = pygame.Surface((interface.get_width(),30)) #criação da área de contagem de pontos
fundo = pygame.image.load('Imagem.png') #carrega a foto como fundo do jogo

#criando as cores dos botões e geral
cor_preto = (0,0,0)
cor_branco = (255,255,255)
cor_vermelho = (255,0,0)
cor_verde = (0,255,0)
cor_azul = (0,0,255)
cor_laranja = (255,127,0)

#poligonos que detectam os botoes do mouse
botao_azul = pygame.draw.circle(interface, cor_azul, center = (251,282),radius = 130, draw_top_left= True)
botao_verde = pygame.draw.circle(interface, cor_verde, center = (251,282),radius = 130, draw_top_right= True)
botao_vermelho = pygame.draw.circle(interface, cor_vermelho, center = (251,282),radius = 130, draw_bottom_right= True)
botao_laranja = pygame.draw.circle(interface, cor_laranja, center = (251,282),radius = 130, draw_bottom_left= True)

#Textos
texto_comeco = fonte_botoes.render('START', True,cor_preto) #Render() passa o texto para a interface,
# define se vai suaviza-lo (True) e a cor
pontos = 0
cores_sequencia = []    #sequencia de cores que irá piscar aleatoriamente
jogando = False #para gerar o loop infinito

while not jogando:  #enquanto não estiver jogando, faça:
    interface.blit(fundo,(0,30))    #escreve o background
    botao_comecar = pygame.draw.rect(interface, cor_branco,(180,70,150,60)) #desenha o botão de começo e
    # indica as posições inicial e final do botão com as coordenadas
    interface.blit(texto_comeco,(200,74))   #desenha o texto no botão
    pygame.display.update() #atualiza a interface para o usuário
    for evento in pygame.event.get():   #para cada clique no jogo, faça:
        if evento.type == QUIT:
            quit()  #fecha a interface
        if evento.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()  #pega a posição do mouse
            if botao_comecar.collidepoint(mouse):   #testa se o mouse colide(aperta) na posição onde se encontra o botão_começar
                jogando = True  #coloca jogando como True para finalizar o loop

interface.blit(fundo, (0,30))   #atualiza o fundo para tirar o botão START
pygame.display.update()

while jogando:
    barra_status.fill(cor_preto)    #sobreescreve o texto antigo para o novo
    pontuacao = fonte_contagem.render('Pontos: '+str(pontos),True,(cor_branco))
    barra_status.blit(pontuacao,(0,0))  #desenha a pontuação
    interface.blit(barra_status,(0,0))  #desenha a barra de status
    pygame.display.update()
    time.sleep(0.5) #delay entre uma jogada e outra
    for evento in pygame.event.get():
        if evento.type ==  QUIT:
            quit()
    cores_sequencia.append(escolher_cor_aleatoria())    #escolhe uma cor aleatória e adiciona na sequência
    piscar_cores(cores_sequencia)
    resposta_jogador = obter_resposta(len(cores_sequencia))
    sequencia_cores = [] #lista vazia para comparar as respostas do usuário com as cores escolhidas aleatoriamente
    for cor in cores_sequencia:
        sequencia_cores.append(cor['cor']) #adiciona as cores em sequência a partir da chave cor
    if sequencia_cores == resposta_jogador: #caso o usuário acerte, atualiza os pontos
        pontos +=1
    else:   #caso erre, dá a opção de reiniciar o jogo
        jogando = restart()
        if jogando: #se retornar verdadeiro, reinicia o loop
            pontos = 0  #zera os pontos
            cores_sequencia = []    #zera a sequência de cores
