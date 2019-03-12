# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:53:10 2019

@author: lwj
"""
import pygame



from library.mysprite import Sprite_DI



from item import resource 

r = resource.explosion

image_path = r.image_path
sound_path = r.sound_path



class Explosion(Sprite_DI):
    image = None
    sound = None
    
    def __init__(self,pos,voice=False):

        if Explosion.image == None:
            Explosion.image = pygame.image.load(image_path).convert_alpha()
        if Explosion.sound == None:
            Explosion.sound = pygame.mixer.Sound(sound_path)
        sound = None
        if voice:
            sound = Explosion.sound

        super().__init__(1,sound)
        super().load(Explosion.image,128,128,6)

        self.position = pos
         
        
    def update(self,current_time,rate=60):
        super().update(current_time,rate)
        
    
            
