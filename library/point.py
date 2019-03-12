class Point:	
    def __init__(self,*args):
        if len(args)==1:
            self.__x ,self.__y =args[0]  
        elif len(args)==2:
            self.__x ,self.__y= args
        elif len(args)==0:
            self.__x ,self.__y= 0,0
        else:
            raise TypeError()
    def getx(self):return self.__x
    def setx(self,x):self.__x =x
    x = property(getx, setx)
	
    def gety(self):return self.__y
    def sety(self,y):self.__y =y
    y = property(gety, sety)
	
    def getpos(self):return self.__x,self.__y
    def setpos(self,pos):self.__x ,self.__y = pos
    pos = property(getpos,setpos)
	
    def __add__(self,pos):
        if type(pos) in (tuple,list):
            return Point(self.x+pos[0],self.y+pos[1])
        else:
            return Point(self.x+pos.x,self.y+pos.y)
    def __radd__(self,pos):
        if type(pos) in (tuple,list):
            return Point(self.x+pos[0],self.y+pos[1])
        else:
            return Point(self.x+pos.x,self.y+pos.y)
    def __sub__(self,pos):
        if type(pos) in (tuple,list):
            return Point(self.x-pos[0],self.y-pos[1])
        else:
            return Point(self.x-pos.x,self.y-pos.y)
    def __rsub__(self,pos):
        if type(pos) in (tuple,list):
            return Point(pos[0]-self.x,pos[1]-self.y)
        else:
            return Point(pos.x-self.x,pos.y-self.y)
    def __neg__(self):
        return Point()-self.pos
    
    def __mul__(self,value):
        return Point(self.x*value,self.y*value)
    def __rmul__(self,value):
        return Point(self.x*value,self.y*value)
    def __truediv__(self,value):
        return Point(self.x/value,self.y/value)
    
    def __str__(self):
        return "Point(%.2f,%.2f)"%(self.x,self.y)
    def __repr__(self):
        return "Point(%.2f,%.2f)"%(self.x,self.y)
    
def getLinePos(Points,nums=5):
    result = []
    wid = 1/(nums-1)
    for i in range(nums):
        ps = Points.copy()
        r = i*wid
        

        for j in range(len(ps)-1):
            for k in range(len(ps)-1-j):
                ps[k] = (1-r)*ps[k] + r*ps[k+1]
        result.append(ps[0])
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    