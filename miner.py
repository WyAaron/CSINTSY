import random
#class Object Position
class Entity:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
#class for Alien
class Alien(Entity): 
    pass
    #default facing of the alien is east 
    front[self.X+1][self.Y] =  
    fctr = 0; 
    def rotate(self): 
        
        # face south
        if fctr ==0: 
            front[self.X][self.Y+1]
            print("the alien is facing south: ({},{})".format(self.X,self.Y))
            return fctr == 1
        # face west 
        elif fctr ==1:
            front[self.X-1][self.Y]
            return fctr == 2
        # face north
        elif fctr == 2:
            front[self][self.Y-1]
            return fctr == 3
        # face east 
        elif fctr ==3: 
            front[self.X][self.Y-1]
            return fctr ==0

        pass

    def move_random(self):
        value = random.randint(1,2)
        #print("Before Self-X: " , self.X,"Before Self-Y: " , self.Y)
        if self.X == (sizeofN-1) and self.Y == (sizeofN-1):
            self.X = 0 
            self.Y = 0
            return self.X, self.Y
        if value  == 1: 
            self.X = self.X +1
            print("Self-X: " , self.X,"Self-Y: " , self.Y)
            # THIS IS TO MAKE SURE THAT X AXIS WOULD NOT OVERLAP WITH NOT GO OVERBOARD
            if self.X == sizeofN:
                self.X = self.X -1
                print("Self-X: " , self.X,"Self-Y: " , self.Y)
                return self.X
            return self.X
        elif value == 2: 
            self.Y = self.Y +1 
            print("Self-X: " , self.X,"Self-Y: " , self.Y)
            # THIS IS TO MAKE SURE THAT Y AXIS WOULD NOT OVERLAP WITH NOT GO OVERBOARD
            if self.Y == sizeofN:
                self.Y = self.Y - 1
                print("Self-X: " , self.X,"Self-Y: " , self.Y)
                return self.Y
            return self.Y

    def scan(self):
        pass



 
#class creation for Pit
class Pit(Entity): 
    def __init__(self,X,Y):
        super().__init__(X,Y)
    
    
    def ShowPit(self):
        print("P")

#class creation for Gold
class Gold(Entity): 
    def __init__(self,X,Y): 
        super().__init__(X,Y)
        

    def ShowGold(self):
        print("G")

#class creation for Nano
class Nano(Entity): 
    def __init__(self,X,Y): 
        super().__init__(X,Y)

    def ShowNano(self):
        print("N")
#class creation for Grid
class Grid():
    
    def __init__(self,size,alien,gold,nano,pit):
        self.size = size
        self.alien =alien
        self.gold = gold
        self.nano = nano
        self.pit = pit

    def printGrid(self):
        x = [["0" for i in range(self.size)] for j in range(self.size)]
        x[alien.X][alien.Y] ='Alien'
        x[gold.X][gold.Y] ='G'
        x[nano.X][nano.Y] ='N'
        x[pit.X][pit.Y] ='P'
        for i in x: 
            print(i)
    def check(self):
        if alien.X == gold.X and alien.Y == gold.Y: 
            print("Alien had found the gold")
            return 0
        elif alien.X == nano.X and alien.Y == nano.Y:
            print("Alien was killed by nano")
            return 0
        elif alien.X == pit.X and alien.Y == pit.Y:
            print("Alien has fallen into the Pit") 
            return 0
        
    






# size input for the NxN grid
sizeofN = int(input("Enter size "))
# X,Y position for Gold
# goldX, goldY = int(input("Enter X position of Gold: ")),int(input("Enter Y position of Gold: "))
# print("Gold placed at[{},{}]".format(goldX,goldY))
# # X,Y position for Trap
# nanoX, nanoY = int(input("Enter X position of Nano: ")),int(input("Enter Y position of Nano: "))
# print("Nano placed at[{},{}]".format(nanoX,nanoY))
# # X,Y position for Pit
# pitX, pitY = int(input("Enter X position of Pit: ")),int(input("Enter Y position of Pit: "))
# print("pit place at[{},{}]".format(nanoX,nanoY))


alien = Alien(0,0) 
# X and Y positions of gold
gold = Gold(6,6) #goldX,goldY
# X and Y positions of Pit
pit = Pit(3,3) #pitX,pitY
# X and Y positions of Nano
nano =Nano(4,4) #nanoX,nanoY
# initializes the placements of the entities 
grid = Grid(sizeofN,alien,gold,nano,pit)

ctr =0

while True: 
    grid.printGrid()

    # AX,AY = int(input("X: ")),int(input("Y: "))

    # if grid.alien[alien.X][alien.Y] == 'A':
    #     alien[alien.X][alien.y] = 0
        
        # alien.X, alien.Y = AX,AY
    alien.move_random(); 
    alien.rotate(); 

    print(grid.check())
    if grid.check() == 0:
        break
    ctr = ctr+1
    

print("Moves made: ",ctr)
    
