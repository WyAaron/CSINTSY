import random

class Alien: 
    pastlocs = [ ] 
    def __init__(self):
        # since starting point 
        self.x = 0
        self.y = 0
        #East-2 South-3 West-4 North-1 
        self.front = 2
        self.mctr = 0
        self.rctr = 0
        self.sctr = 0 
        

    def move(self,grid): 
        
        
        
        self.mctr +=1 
        #move north
        if self.front == 1: 
            if (self.y != 0):
                self.y -= 1
                grid.xy[self.y+1][self.x] = '----'
                if (self.y != 0):
                    grid.xy[self.y+1][self.x] = '----'
                
            print("-----------------------------------------")
            print("Moving to(X: {}, Y:{})".format(self.x,self.y))
            print("-----------------------------------------")
            

        #MOVE EAST
        elif self.front == 2: 
            
            if (self.x != (grid.sizeN)):
                self.x += 1
                ## prevent if it will go out of bounds
                if self.x == grid.sizeN:
                    self.rotate(grid)
                    
                    self.x -= 1
                
                grid.xy[self.y][self.x-1] = '----'
                if (self.x != (grid.sizeN)):
                    grid.xy[self.y][self.x-1] = '----'
            print("-----------------------------------------")
            print("Moving to(X: {}, Y:{})".format(self.x,self.y))
            print("-----------------------------------------")

        #MOVE SOUTH
        elif self.front == 3:
            if (self.y != grid.sizeN):
                self.y += 1
                ## prevent if alien would go out of bounds 
                if self.y == grid.sizeN:
                    self.rotate(grid)
                    
                    self.y-=1
                
                grid.xy[self.y-1][self.x] = '----'
                if (self.y != grid.sizeN):
                    grid.xy[self.y-1][self.x] = '----'
            print("-----------------------------------------")
            print("Moving to(X: {}, Y:{})".format(self.x,self.y))
            print("-----------------------------------------")

        #MOVE WEST
        elif self.front == 4: 
            if (self.x != 0):
                self.x -= 1 
                
                grid.xy[self.y][self.x+1] = '----'
                if (self.y != grid.sizeN):
                    grid.xy[self.y][self.x+1] = '----'
            print("-----------------------------------------")
            print("Moving to(X: {}, Y:{})".format(self.x,self.y))
            print("-----------------------------------------")
        
        
    

    def rotate(self,grid):
        self.rctr +=1 
        self.front += 1

        if(self.front == 5):
            self.front = 1
        print("-----------------------------------------")
        print("Rotated: {} (1-north2-east,3-south,4-west)".format(self.front))
        print("-----------------------------------------")
        
    def scan(self,grid):
        self.sctr +=1
        #scan right 
        if self.front == 2:
            if self.x+1 >= grid.sizeN:
                self.rotate(grid)
                return None
            print("-----------------------------------------")
            print("Infront: {}".format(grid.xy[self.y][self.x+1]))
            print("-----------------------------------------")
            return grid.xy[self.y][self.x+1]
        
        #scan south
        elif self.front == 3:
            if self.y+1 >= grid.sizeN:
                self.rotate(grid)
                return None
            print("-----------------------------------------")
            print("Infront: {}".format(grid.xy[self.y+1][self.x]))
            print("-----------------------------------------")
            return grid.xy[self.y+1][self.x]
        #scan west 
        
        elif self.front == 4:
            if self.x-1 < 0 :
                self.rotate(grid)
                return None
            print("-----------------------------------------")
            print("Infront: {}".format(grid.xy[self.y][self.x-1]))
            print("-----------------------------------------")
            return grid.xy[self.y][self.x-1]
        #scan north 
    
        elif self.front  ==1: 
            if self.y-1 < 0:
                self.rotate(grid)
                return None
            print("-----------------------------------------")
            print("Infront: {}".format(grid.xy[self.y-1][self.x]))
            print("-----------------------------------------")
            return grid.xy[self.y-1][self.x]



            

    def random(self,grid):
        move = random.randint(1,3)
        if (move == 1):
            self.move(grid)

        elif (move == 2): 
            self.rotate(grid)
        elif move == 3:
            self.scan(grid)
            

    def smart(self,grid):

        scanval = '----'
        
        if (self.scan(grid) == scanval):
            # check if the front location is a past location
            for i in self.pastlocs: 
                if ([self.x,self.y]) == i:
                    self.rotate(grid)
            self.pastlocs.append([self.x,self.y])
            self.move(grid)

        elif (self.scan(grid) == None):
            self.rotate(grid)
        elif ((self.scan(grid) == 'GOLD')):            
            self.move(grid)
        elif ((self.scan(grid) == 'NANO')):
            self.rotate(grid)
            self.move(grid)
        elif ((self.scan(grid) == 'PITS')):
            self.rotate(grid)
            self.move(grid)
    
        





class Grid(): 

    def __init__(self,sizeN,pits,gold,nano):
        self.sizeN = sizeN
        self.xy = [['----' for x in range(0,sizeN)] for x in range(0,sizeN)]
        self.xy[goldy-1][goldx-1] ='GOLD'
        self.xy[nanoy-1][nanox-1] ='NANO'
        self.pits=pits

        for pit in pits:
            self.xy[pit[1]-1][pit[0]-1] = 'PITS'


        
        
    def update(self,alien): 
        grid.xy[alien.y][alien.x] ='MINE'
        for i in grid.xy:
            print(i)
    
    def check(self,alien): 
        if grid.xy[alien.y][alien.x] == 'GOLD':
            print("win win win win")
            return 1
        elif grid.xy[alien.y][alien.x] == 'NANO':
            print("KILLED BY NANO")
            return 1
        elif grid.xy[alien.y][alien.x] == 'PITS':
            print("ALIEN: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
            return 1

sizeN = int(input("Enter the size of board: "))

goldx = int(input("Enter the X location of gold: "))
goldy = int(input("Enter the y location of gold: ")) 
goldLoc = (goldy,goldx)

nanox = int(input("Enter the X location of nano: "))
nanoy = int(input("Enter the y location of nano: "))
nanoLoc = (nanoy,nanox)

pN  = int(input("Please enter how many pits to put: "))

pitArr = []
for i in range(pN): 
    pitx = int(input("Enter the X location of pit: "))
    pity = int(input("Enter the y location of pit: ")) 
    pitArr.append(tuple((pity,pitx)))

smart = int(input('1-Smart/2-random:'))

alien = Alien()
grid = Grid(sizeN,pitArr,goldLoc,nanoLoc)

ctr =1
while True: 
    
    
    grid.update(alien)
    if(smart ==1): 
        alien.smart(grid)
    elif(smart ==2):
        alien.random(grid)
    
    # if ctr == 10:
    #     break
    
    # ctr+=1
    if(grid.check(alien)==1):
        break
    


print("Move:{} Rotate: {} Scan: {}".format(alien.mctr,alien.rctr,alien.sctr))














