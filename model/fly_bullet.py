# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:21:04 2019

@author: lwj
"""
from item.bullet import Bullet

from library.point import Point , getLinePos
import math

class FB(Bullet):
    def __init__(self,points,nums=21):
        super().__init__(points[0].pos)
        self.poslist = getLinePos(points,nums)
#        self.poslist = points
        
        self.step = 0
        self.max_step = len(self.poslist) - 1
        
        
        self.t = 5
        self.t0 = 0
        self.setface()
        
    def setface(self):
        p = self.poslist[self.step+1] - self.poslist[self.step]
        dx,dy = p.pos

        radian = math.atan2(-dy,dx)
        direct = math.degrees(radian)
       
        rotate = direct - self.angle

        self.rotate(rotate)
        
        self.vx = dx /self.t
        self.vy = dy /self.t
        
        
    def update(self,ticks):
        super().update()
        self.t0 += 1
        if self.t0 >= self.t :
            self.t0 =0
            self.step +=1
            if self.step >= self.max_step:
                self.kill()
            else :
                self.setface()

            
        
 