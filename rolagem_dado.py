import pygame
from pygame.locals import *
from sys import exit 
from random import randint
import os
from pygame import mixer

mixer.init()
mixer.music.load('sounds/background_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)


diretorio_principal = os.path.dirname(__file__)
diretorio_imagem = os.path.join(diretorio_principal, 'sprite_sheets')

spritesheet1 = pygame.image.load(os.path.join(diretorio_imagem, 'spritesheet1.png'))
spritesheet2 = pygame.image.load(os.path.join(diretorio_imagem, 'spritesheet2.png'))
spritesheet3 = pygame.image.load(os.path.join(diretorio_imagem, 'spritesheet3.png'))
spritesheet4 = pygame.image.load(os.path.join(diretorio_imagem, 'spritesheet4.png'))
spritesheet5 = pygame.image.load(os.path.join(diretorio_imagem, 'spritesheet5.png'))
spritesheet6 = pygame.image.load(os.path.join(diretorio_imagem, 'spritesheet6.png'))

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

        self.sprite1 = []
        self.sprite2 = []
        self.sprite3 = []
        self.sprite4 = []
        self.sprite5 = []
        self.sprite6 = []

        for i in range(34):
            img1 = spritesheet1.subsurface((i * 240, 0), (240, 320))
            self.sprite1.append(img1)
        for i in range(34):
            img2 = spritesheet2.subsurface((i * 240, 0), (240, 320))
            self.sprite2.append(img2)
        for i in range(34):
            img3 = spritesheet3.subsurface((i * 240, 0), (240, 320))
            self.sprite3.append(img3)
        for i in range(34):
            img4 = spritesheet4.subsurface((i * 240, 0), (240, 320))
            self.sprite4.append(img4)
        for i in range(34):
            img5 = spritesheet5.subsurface((i * 240, 0), (240, 320))
            self.sprite5.append(img5)
        for i in range(34):
            img6 = spritesheet6.subsurface((i * 240, 0), (240, 320))
            self.sprite6.append(img6)

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
        self.image = pygame.transform.scale(self.image, (480, 640))
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
        if self.animar == True:
            pygame.event.set_blocked(MOUSEBUTTONDOWN)
            self.atual += 1
            if self.atual >= len(self.sprites[self.face]):
                dicesound()
                self.atual = 0 
                self.animar = False
                pygame.event.set_allowed(MOUSEBUTTONDOWN)
            self.image = self.sprites[self.face][self.atual] 
            self.image = pygame.transform.scale(self.image, (480, 640))
    
relogio = pygame.time.Clock()
todas_sprites = pygame.sprite.Group()
dado = Dado()
todas_sprites.add(dado)

while True:
    relogio.tick(30)
    tela.fill(preto)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                jump()                  
                face = randint(1, 6)
                if face == 1:
                    dado.rolar1()  
                elif face == 2:
                    dado.rolar2()        
                elif face == 3:
                    dado.rolar3()    
                elif face == 4:
                    dado.rolar4()    
                elif face == 5:
                    dado.rolar5()     
                elif face == 6:
                    dado.rolar6()       
            print(face)  
    
    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()
