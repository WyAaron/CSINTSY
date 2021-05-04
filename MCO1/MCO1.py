import random
    
#class for Alien
class Alien():
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y 
        self.fctr =2
        self.rctr =0 
        self.mctr =0
    #default facing of the alien is east 
    
    def rotate(self): 
        ############################################
        
        self.fctr += 1
        if (self.fctr == 5):
            self.fctr = 1

       
        
        


        pass

    def move(self,grid):
        # # prevent from moving out of the border
        if self.X > sizeofN-1:
            self.X = self.X-1 
            print("prevented moving out of borrder")
        
        if self.Y > sizeofN-1:
            self.Y = self.Y-1
            print("prevented moving out of borrder")
        
        if self.X < 0: 
            self.X = self.X+1
            print("prevented moving out of borrder")
        
        if self.Y < 0: 
            self.Y = self.Y+1
            print("prevented moving out of borrder")
        # move right 
        if self.fctr == 2: 
            self.X += 1
            print("moved right")
        # move down
        elif self.fctr == 3:
            self.Y =+1
            print("moved down")
        # move up
        elif self.fctr == 1:
            self.Y =- 1
            if self.Y < 0:
                self.Y = 0 

            print("moved Up")
        #move left
        elif self.fctr == 4:
            self.X=-1
            if self.X <0: 
                self.X = 0
            print("moved Left")
        if (self.Y < 0 or self.Y >= sizeofN or self.X < 0 or self.X >= sizeofN): 
            return False
        
        
        
    def random(self): 
        rd = random.randint(1,2); 
        if rd ==1: 
            alien.move(grid)
            self.mctr+=1
        elif rd ==2: 
            alien.rotate() 
            self.rctr+=1
        return rd
        

    def scan(self):
        pass




#class creation for Pit
class Pit(): 
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    

#class creation for Gold
class Gold(): 
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        

#class creation for Nano
class Nano(): 
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

#class creation for Grid
class Grid():
    x=[[]]
    def __init__(self,size,gold,nano,pit):
        self.x = [["----" for i in range(0,size)] for j in range(0,size)]
        self.nano = nano 
        self.pit = pit
        self.x[gold.Y][gold.X] ='G'
        self.x[nano.Y][nano.X] ='N'
        self.x[pit.Y][pit.X] ='P'
        self.x[alien.Y][alien.X] ='A'




    
        

    def printGrid(self,alien):
        
        # 
        
        if alien.random() == 1: 
            if alien.fctr == 'E':
                self.x[alien.Y][alien.X-1]='----'
                self.x[alien.Y][alien.X] ='A'
            
            elif alien.fctr == 'S':
                self.x[alien.Y-1][alien.X]='----'
                self.x[alien.Y][alien.X] ='A'
            
            elif  alien.fctr == 'W':
                self.x[alien.Y][alien.X+1]='----'
                self.x[alien.Y][alien.X] ='A'

            elif  alien.fctr == 'N':
                self.x[alien.Y+1][alien.X]='----'
                self.x[alien.Y][alien.X] ='A'

            
        for i in self.x: 
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
sizechk = False
while not sizechk: 
    sizeofN = int(input("Enter size "))
    if sizeofN <8 or sizeofN>64:
        print("Please input only sizes from 8-64")
        sizechk= False
    else: 
        sizechk = True



alien = Alien(0,0) 
# X and Y positions of gold
gold = Gold(2,3) #goldX,goldY
# X and Y positions of Pit
pit = Pit(2,4) #pitX,pitY
# X and Y positions of Nano
nano =Nano(2,5) #nanoX,nanoY
# initializes the placements of the entities 
grid = Grid(sizeofN,gold,nano,pit)

ctr =0

while True: 
    print("Position X: {} Y: {}".format(alien.X,alien.Y)) 
    print("###################################")
    grid.printGrid(alien)

    
        


    if ctr == 50:
        break
    

    if grid.check() == 0:
        break
    ctr = ctr+1
    print("Move CTR: {}".format(alien.mctr))
    print("Rotate CTR: {} ".format(alien.rctr))
    print("Facing Id: {}".format(alien.fctr))
    print("###################################")
    

print("Moves made: ",ctr)
    
