# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:34:41 2019

@author: lwj
"""
import pygame
from sys import exit

class PygameMain:
    def __init__(self,screen_size=(800,600),title=''):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(title)
        self.framerate = pygame.time.Clock()
        self.ticks = 0
        
        self.update_list = []
        self.draw_list = []
        self.produce_init = False
        
#    def __del__(self):
#        pygame.quit()
    
    def run(self):
        while True:
            self.framerate.tick(60)
            self.ticks = pygame.time.get_ticks()

            self.produce()
         
            self.update()
            
            self.event_response()
            
            self.draw()
    
    def produce(self):
        if not self.produce_init:
            self.produce_init = True
            pass
        pass
    
    def event_response(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
    
    def list_add(self,item,order,kind='update'):
        if order > 20 :return
        
        if kind =='update':
            lists = self.update_list 
        elif kind =='draw' :
            lists = self.draw_list
        else :
            raise Exception('No such kind:'+kind)
        if order >= len(lists):
            for _ in range(order - len(lists)+1):
                lists.append([])
        lists[order].append(item)       
        
    def update(self):
        for items in self.update_list:
            for item in items:
                item.update(self.ticks)

    def draw(self):
        for items in self.draw_list:
            for item in items:
                item.draw(self.screen)
        pygame.display.update()
