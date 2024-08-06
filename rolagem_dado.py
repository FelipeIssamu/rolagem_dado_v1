import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os
from pygame import mixer
import math

mixer.init()
mixer.music.load('sounds/background_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)


diretorio_principal = os.path.dirname(__file__)
diretorio_imagem = os.path.join(diretorio_principal, 'sprite_sheets')

spritesheet1 = pygame.image.load(
    os.path.join(diretorio_imagem, 'spritesheet1.png'))
spritesheet2 = pygame.image.load(
    os.path.join(diretorio_imagem, 'spritesheet2.png'))
spritesheet3 = pygame.image.load(
    os.path.join(diretorio_imagem, 'spritesheet3.png'))
spritesheet4 = pygame.image.load(
    os.path.join(diretorio_imagem, 'spritesheet4.png'))
spritesheet5 = pygame.image.load(
    os.path.join(diretorio_imagem, 'spritesheet5.png'))
spritesheet6 = pygame.image.load(
    os.path.join(diretorio_imagem, 'spritesheet6.png'))

pygame.init()

jump_sound = pygame.mixer.Sound('sounds/jump_sound.wav')

dice_sound = pygame.mixer.Sound('sounds/dice_sound.wav')

largura = 480
altura = 640

preto = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Dado')


def dicesound():
    pygame.mixer.Sound.play(dice_sound)
    pygame.mixer.Sound.set_volume(dice_sound, 0.4)


def jump():
    pygame.mixer.Sound.play(jump_sound)
    pygame.mixer.Sound.set_volume(jump_sound, 0.25)


class Dado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite1 = [spritesheet1.subsurface(
            (i * 240, 0), (240, 320)) for i in range(34)]
        self.sprite2 = [spritesheet2.subsurface(
            (i * 240, 0), (240, 320)) for i in range(34)]
        self.sprite3 = [spritesheet3.subsurface(
            (i * 240, 0), (240, 320)) for i in range(34)]
        self.sprite4 = [spritesheet4.subsurface(
            (i * 240, 0), (240, 320)) for i in range(34)]
        self.sprite5 = [spritesheet5.subsurface(
            (i * 240, 0), (240, 320)) for i in range(34)]
        self.sprite6 = [spritesheet6.subsurface(
            (i * 240, 0), (240, 320)) for i in range(34)]

        self.sprites = {
            'face1': self.sprite1,
            'face2': self.sprite2,
            'face3': self.sprite3,
            'face4': self.sprite4,
            'face5': self.sprite5,
            'face6': self.sprite6
        }
        self.atual = 0
        self.image = self.sprites['face1'][self.atual]
        self.image = pygame.transform.scale(self.image, (largura, altura))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.face = 'face1'
        self.animar = False

    def rolar1(self):
        self.face = 'face1'
        self.animar = True

    def rolar2(self):
        self.face = 'face2'
        self.animar = True

    def rolar3(self):
        self.face = 'face3'
        self.animar = True

    def rolar4(self):
        self.face = 'face4'
        self.animar = True

    def rolar5(self):
        self.face = 'face5'
        self.animar = True

    def rolar6(self):
        self.face = 'face6'
        self.animar = True

    def update(self):
        if self.animar is True:
            pygame.event.set_blocked(MOUSEBUTTONDOWN)
            self.atual += 1
            if self.atual >= len(self.sprites[self.face]):
                dicesound()
                self.atual = 0
                self.animar = False
                pygame.event.set_allowed(MOUSEBUTTONDOWN)
            self.image = self.sprites[self.face][self.atual]
            self.image = pygame.transform.scale(self.image, (largura, altura))


relogio = pygame.time.Clock()
todas_sprites = pygame.sprite.Group()
dado = Dado()
todas_sprites.add(dado)
color = (71, 24, 176)
color1 = (81, 34, 186)
smallfont = pygame.font.SysFont('ARCADECLASSIC', 35)

menu1 = pygame.image.load('Menu/menu.png')
menu1 = pygame.transform.scale(menu1, (largura, altura))
menu2 = pygame.image.load('Menu/menu_hover_1.png')
menu2 = pygame.transform.scale(menu2, (largura, altura))
menu3 = pygame.image.load('Menu/menu_hover_2.png')
menu3 = pygame.transform.scale(menu3, (largura, altura))
botaovoltar = pygame.image.load('Menu/voltar.png')
botaovoltar = pygame.transform.scale(botaovoltar, (largura, altura))
botaovoltar_hover = pygame.image.load('Menu/voltar_hover.png')
botaovoltar_hover = pygame.transform.scale(
    botaovoltar_hover, (largura, altura))


def menu():
    while True:
        relogio.tick(30)
        tela.fill((174, 190, 220))
        tela.blit(menu1, (0, 0))
        mouse = pygame.mouse.get_pos()

        if 66*2 <= mouse[0] <= 183*2 and 184*2 <= mouse[1] <= 212*2:
            tela.blit(menu2, (0, 0))

        if 48*2 <= mouse[0] <= 198*2 and 223*2 <= mouse[1] <= 251*2:
            tela.blit(menu3, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 66*2 <= mouse[0] <= 183*2 and 184*2 <= mouse[1] <= 212*2:
                        jogo1()
                    if 48*2 <= mouse[0] <= 198*2 and 223*2 <= mouse[1] <= 251*2:
                        jogo2()

        pygame.display.flip()


def match_face(face):
    match face:
        case 1:
            dado.rolar1()
            return 1
        case 2:
            dado.rolar2()
            return 2
        case 3:
            dado.rolar3()
            return 3
        case 4:
            dado.rolar4()
            return 4
        case 5:
            dado.rolar5()
            return 5
        case 6:
            dado.rolar6()
            return 6


def jogo1():
    pontos = 0
    while True:

        relogio.tick(30)
        mouse = pygame.mouse.get_pos()
        d = math.sqrt(((219*2-mouse[0])**2)+((20.5*2-mouse[1])**2))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if d <= 26:
                        menu()

                    jump()
                    face = randint(1, 6)
                    pontos += match_face(face)

                    print(face)

        todas_sprites.draw(tela)
        todas_sprites.update()
        tela.blit(smallfont.render(f'player 1   {
                  pontos}', True, color), ((largura/2)-200, altura/5.5))

        tela.blit(botaovoltar, (0, 0))

        if d <= 26:
            tela.blit(botaovoltar_hover, (0, 0))
        pygame.display.flip()


def jogo2():
    pontos = 0
    pontos2 = 0
    cont = 0
    contador = 0
    while True:
        relogio.tick(30)
        mouse = pygame.mouse.get_pos()
        d = math.sqrt(((219*2-mouse[0])**2)+((20.5*2-mouse[1])**2))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if d <= 26:
                        menu()

                    cont += 1
                    jump()
                    face = randint(1, 6)

                    if cont % 2 == 0:
                        contador += 1
                        pontos2 += match_face(face)
                        print(contador)
                    else:
                        pontos += match_face(face)

                # print(face)

        todas_sprites.draw(tela)
        todas_sprites.update()
        tela.blit(smallfont.render(f'player 1   {
                  pontos}', True, color), ((largura/2)-200, altura/5.5))
        tela.blit(smallfont.render(f'player 2   {
                  pontos2}', True, color), ((largura/2+40), altura/5.5))
        tela.blit(botaovoltar, (0, 0))
        if d <= 26:
            tela.blit(botaovoltar_hover, (0, 0))
        pygame.display.flip()


menu()
