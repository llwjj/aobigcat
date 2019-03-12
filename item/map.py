# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 16:30:25 2019

@author: lwj
"""
import pygame

image_path = "./resource/img/background.png"

class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._bg = pygame.image.load(image_path).convert()
        self._len = self._bg.get_width()
        self._x = self._len
        self._rate =5
    def update(self,*a):
        self._x -=self._rate
        if self._x <= 0:
            self._x+=self._len
    def draw(self,screen):
        screen.blit(self._bg,(self._x,0))
        screen.blit(self._bg,(self._x-self._len,0))