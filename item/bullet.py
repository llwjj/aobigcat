# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:40:58 2019

@author: lwj
"""
import pygame


from item.explosion import Explosion

from library.mysprite import Sprite_SI

from item import resource 

r = resource.bullet

image_path = r.image_path
sound_path = r.sound_path



class Bullet(Sprite_SI):

    image = None
    sound = None 
    
    def __init__(self,pos,voice=False):   
        if Bullet.image == None:
            Bullet.image = pygame.image.load(image_path)
            w,h = Bullet.image.get_size()
            Bullet.image = pygame.transform.scale(Bullet.image,(w//4,h//4))

        if Bullet.sound == None:
            Bullet.sound = pygame.mixer.Sound(sound_path)  
        
        sound = None
        if voice:
            sound = Bullet.sound
        super().__init__(Bullet.image,pos,sound) 
        
        self.angle = 270
        self.image_angle = 270
        self.vx = 0
        self.vy = 0
    
    
    def scale(self,value):
        (w,h)=self.base_image.get_size()
        w = round(w*value)
        h = round(h*value)
        self.base_image = pygame.transform.scale(Bullet.image,(w,h))
        self.image = self.base_image
    def update(self,*args,**kw):
        self.X += self.vx
        self.Y += self.vy
        if self.rect.right <-10:
            self.kill()
    
    def boomb(self):
        self.kill()
        return Explosion(self.rect.center)
    

        
        
        
        
        
        
