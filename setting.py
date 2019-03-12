# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:32:06 2019

@author: lwj
"""
import os.path as op

# =============================================================================
# resource path
# =============================================================================

class resource:
 
    class item:
        
        class bullet:
   
            image_path = op.abspath("./resource/img/fish.png")
            sound_path = op.abspath("./resource/sound/bullet.wav")
            
        class cat:
            
            image_path = op.abspath("./resource/img/sprite.png")
        
        class explosion:
            
            image_path = op.abspath("./resource/img/explosion.png")
            sound_path = op.abspath("./resource/sound/exlposion.wav")
            
            
    class library:
        pass
# =============================================================================
# params
# =============================================================================
class params:
     backgroudMoveSpeed = (-5,0)
        
