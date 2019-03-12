# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:45:38 2019

@author: lwj
"""
import pygame

class Music():
    def __init__(self,sound):
        self.channel = None
        self.sound = sound
    def play(self):
        self.channel = pygame.mixer.find_channel(True)
        self.channel.set_volume(0.5)
        self.channel.play(self.sound)
    def pause(self):
        self.channel.set_volume(0.0)
        self.channel.play(self.sound)
    def repaly(self):
        self.pause()
        self.play()