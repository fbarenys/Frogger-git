from Cars import *

class Lane:
    width=800
    height=40
    def __init__(self,x,y,type,numOfVehicles,vehicleSpeed,height):
        self.x = x
        self.y = y
        self.height=height
        self.cars=[]
        self.carsSpeed=vehicleSpeed
        if type==1: #lane of cars
            for i in range(numOfVehicles):
                if vehicleSpeed>=0:
                    c=Car(x+i*50,y+height/4,vehicleSpeed)
                    self.startX = x
                    #self.startY = y+10
                else:
                    c = Car(x+self.width-i*50, y + height/4, vehicleSpeed)
                    self.startX = x+self.width
                    #self.startY = y + 10
                self.cars.append(c)

        if type==2: #lane of lorries
            for i in range(numOfVehicles):
                if vehicleSpeed>=0:
                    c=Lorry(x+i*70,y+height/4,vehicleSpeed)
                    self.startX = x
                else:
                    c = Lorry(x+self.width-i*70, y + height/4, vehicleSpeed)
                    self.startX = x+self.width
                self.cars.append(c)

    def isOutsideLimits(self,car):
        if car.x<self.x or car.x>self.x+self.width:
            return True
        return False

    def moveCars(self):
        for c in self.cars:
            c.move()
            if self.isOutsideLimits(c):
                c.x = self.startX

    def draw(self,w):
        w.create_rectangle(self.x,self.y,self.x + self.width, self.y + self.height,fill="gray")
        for c in self.cars:
            c.draw(w)
