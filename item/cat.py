# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:04:03 2019

@author: lwj
"""
import pygame


        
from library.mysprite import Sprite_DI

from item import resource
        
   

r = resource.cat

image_path = r.image_path


class Cat(Sprite_DI):
    image = None
    
    def __init__(self,pos):
        if Cat.image == None:
            Cat.image = pygame.image.load(image_path).convert_alpha()
            
        super().__init__()
        super().load(Cat.image, 100, 100, 4)
        self.position = pos
        
        self.y_low = self.Y
        self.vy = 0
        self.ay = 0
        self.isRise = False
        self.isFall = False
    
        
    def jump(self):
        if not (self.isRise or self.isFall):
            self.isRise = True
            self.vy = -15
            self.ay = -2*self.vy / 45
            
    def move(self,direction=0):
        step = 5
        if direction == 0:
            self.X += step
        else :
            self.X -=step
            
    def update(self,current_time,rate=60):
        super().update(current_time,rate)
        
        if self.isRise or self.isFall:
            self.Y += int(self.vy+0.5)
            self.vy  += self.ay
        if self.isRise and self.vy>=0:
            self.isRise = False
            self.isFall = True
        if self.isFall and self.Y>=self.y_low:
            self.Y = self.y_low
            self.isFall = False
            self.vy =0
        
        
        
        
        
        
        
        
        
        
        
        
