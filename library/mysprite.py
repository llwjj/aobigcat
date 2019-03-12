
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:39:48 2019

@author: lwj
"""
import pygame
from pygame.locals import Rect

from library.music import Music



class Sprite_0(pygame.sprite.Sprite):
    def __init__(self,sound=None):
        super().__init__()
        self.image=None
        
        self.__x = 0
        self.__y = 0
        
        self.rect = Rect(0,0,0,0)
        
        
        self.music = None
        if sound:
            self.music = Music(sound)
            self.music.play()
        
    def __del__(self):
        if not self.music == None:
            self.music.pause()
            
    #X property 
    def _getx(self): return self.__x
    def _setx(self,value): 
        self.__x = value
        self.rect.x = round(self.__x)
    X = property(_getx,_setx)

    #Y property
    def _gety(self): return self.__y
    def _sety(self,value):
        self.__y = value
        self.rect.y = round(self.__y)
    Y= property(_gety,_sety)    
    
    
    def _getpos(self): 
        x = self.__x + self.rect.w/2 
        y = self.__y + self.rect.h/2
        return x,y
    def _setpos(self,pos): 
        if type(pos) in [tuple,list]:
            self.__x = pos[0] - self.rect.w/2
            self.__y = pos[1] - self.rect.h/2
        else:
            self.__x = pos.x - self.rect.w/2
            self.__y = pos.y - self.rect.h/2
        self.rect.x = round(self.__x)
        self.rect.y = round(self.__y)
    position = property(_getpos,_setpos)
    
    

    def draw(self,screen):
        screen.blit(self.image,self.rect.topleft)
            


class Sprite_SI(Sprite_0):
    
    def __init__(self,image,pos=(0,0),sound=None):         
        super().__init__(sound)
        self.base_image = image
        self.image = image
        self.rect.size = image.get_size()
        self.position = pos
        
        self.angle = 0
        self.image_angle =0
            
    def update(self,*args,**kw):
        pass

        
    def rotate(self,angle):
        self.angle += angle
        if self.angle >=360:
            self.angle -= 360
            
        old_size = self.image.get_size()
        self.image = pygame.transform.rotate(self.base_image,self.angle-self.image_angle)
        new_size = self.image.get_size()
        
        dx = (old_size[0]-new_size[0])/2
        dy = (old_size[1]-new_size[1])/2
 
        self.rect.size = new_size

        self.X += dx
        self.Y += dy
        
        
class Sprite_DI(Sprite_0):
    def __init__(self,times=0,sound=None):
        super().__init__(sound)
        self.total_run_times = times
        
        self.images = []
        self.frame =0
        self.old_frame =-1
        self.last_frame = 0
        
        self.last_time = 0
        
        self.run_times = 0
    
    def load(self, image, width, height, columns):
        self.rect.size = (width,height)
        r = image.get_rect()
        self.last_frame = (r.width // width) * (r.height // height) - 1
        for f in range(self.last_frame+1):
            frame_x = (f % columns) * width
            frame_y = (f // columns) * height
            img = image.subsurface(Rect(frame_x, frame_y, width, height))
            self.images.append(img)
        
    def update(self, current_time, rate=30):
        #update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = 0
            self.last_time = current_time

        #build current frame only if it changed
        if self.frame != self.old_frame:
            self.image = self.images[self.frame]
            self.old_frame = self.frame  
            
        if self.total_run_times > 0:
            if self.old_frame == self.last_frame:
                self.run_times += 1
            if self.run_times >= self.total_run_times:
                self.kill()

        
        
        
        
