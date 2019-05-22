import pygame
import sys
import os

class Jugador(pygame.sprite.Sprite):
    '''
        Clase que representa un Jugador con físicas incluidas
    '''
    def __init__(self, xInicial, yFinal,width, height):
        """
            Constructor del Jugador
        :param xInicial: posición x inicial del Jugador
        :param yFinal: posición y inicial del Jugador
        :param width: anchura del jugador
        :param height: altura del jugador
        """
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.image = pygame.Surface([width, height])
        self.image.fill((150, 150, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, (150, 150, 0), [xInicial, yFinal, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = xInicial
        self.rect.y = yFinal

    def control(self,x,y):
        '''
            Control del movimiento del jugador
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
            Actualiza posición del jugador
        '''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.movex = 0
        self.movey = 0

    def draw(self, surface):
        """
            Pintar Surface Jugador
        """
        surface.blit(self.image, (self.rect.x, self.rect.y))