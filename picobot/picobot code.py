from graphics import *
import tkinter as tk
from tkinter.filedialog import askopenfilename


def dialogueBox():
    tk.Tk().withdraw()
    filename= askopenfilename(initialdir="C:\\Users\\graci\\AppData\\Local\\Programs\\Python\\Python39\\Python projects\\Python Projects\\picobot",
                              title = "upload your picobot instructions")
    return filename
    
def readFile(x):
    file=open(x,'r')
    #readFile= file.readlines()
#print(readFile)
    instructions = []
    for line in file:
        line = line.split()
        line.pop(2)

        # converts state to integer
        line[0]=int(line[0])

        # converts new state to integer
        line[3] = int(line[3])
        instructions.append(line)
    

    return instructions
    
def asterics(instructions,index,character): #index = position of astrics, character= N,E,S or W

    newLst = []


    for line in instructions:

        if line[1][index] == "*":
            
            #newLine= list(line[1])
            newLine=line[1]
            newLineX = newLine[:index]+"X"+newLine[index + 1:]
            newLineChar = newLine[:index]+ character + newLine[index + 1:]
            
            newLineX=[line[0]] + [newLineX] + line[2:]
            newLineChar = [line[0]] + [newLineChar] + line[2:]

            newLst.append(newLineX)
            newLst.append(newLineChar)

        else:
            newLst.append(line)

    return newLst

def drawPixel(x,y,window, colour):
    rect = Rectangle(Point(x,y), Point(x+20,y+20))
    rect.setOutline(colour)
    rect.setFill(colour)

    rect.draw(window)

    return
            


grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
        [1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,1],\
        [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1],\
        [1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1],\
        [1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1],\
        [1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1],\
        [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1],\
        [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1],\
        [1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,1,1],\
        [1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1],\
        [1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1],\
        [1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1],\
        [1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1],\
        [1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,1],\
        [1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1],\
        [1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,1],\
        [1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1],\
        [1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1],\
        [1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1],\
        [1,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1],\
        [1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1],\
        [1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1],\
        [1,0,1,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1],\
        [1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1],\
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
            

window = GraphWin("picobot",500,600)

def drawGrid(grid):
    x=0
    y=0
    trailsquares=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                drawPixel(x,y,window,"blue")
            else:
                drawPixel(x,y,window,"white")
            x=x+20
        x= 0
        y=y+20
    for row in grid:
        for item in row:
            if item ==0:
                trailsquares+=1


                
    return trailsquares


def inside(point, rectangle):
    """ Is point inside rectangle? """

    ul = rectangle.getP1()  # assume p1 is ul (upper left)
    lr = rectangle.getP2()  # assume p2 is lr (lower right)

    return ul.getX() < point.getX() < lr.getX() and lr.getY() < point.getY() < ul.getY()


# 1 draw picobot
# move picobot
# 


class Button:


    def __init__(self,window,left,right, colour, text):
        self.win = window
        self.left = left
        self.right = right
        self.button = Rectangle(self.left, self.right)
        self.colour = colour
        self.text= Text(Point((left.x+right.x)/2, (left.y+right.y)/2), text )

    def drawButton(self):
        self.button.draw(self.win)
        self.button.setFill(self.colour)
        self.text.draw(self.win)

    def checkClick(self, clickpoint):

        if clickpoint != None:

            if clickpoint.x in range(self.left.x, self.right.x) and \
            clickpoint.y in range(self.left.y,self.right.y):

                return True

        return False 

class Picobot:

    def __init__(self,window,grid,colour="red"):

        self.colour = colour
        self.state = 0
        self.startPointX = 20
        self.startPointY = 20
        self.win = window
        self.trailsquares = 0
        self.trail=grid
        self.grid = grid
        self.x = 1
        self.y= 1
        
        



        trail = []
        rows = []

    
        '''for j in range(25):

            rows = []


            for i in range(25):
            
            
                rows.append(0)

            trail.append(rows)

        self.trail = trail'''
        
        

    def drawBot(self):
       
        picobot = Rectangle(Point(self.startPointX,self.startPointY), Point(self.startPointX+20,self.startPointY+20))
        picobot.setOutline(self.colour)
        picobot.setFill(self.colour)

        picobot.draw(self.win)

        self.picobot = picobot

    def surroundings(self):  #problem 1: startPointX and startPointY don't update, so it returns the same surroundings each time the bot moves

        surroundings = ""

        

        picoX = self.startPointX
        picoY= self.startPointY

        gridpositionX = picoX//20
        gridpositionY = picoY//20

        if grid[gridpositionY-1][gridpositionX] == 1:
            surroundings = "N"
            #self.startPointY = self.startPointY - 20


        else:
            surroundings = "X"

        if grid[gridpositionY][gridpositionX+1] == 1:
            surroundings = surroundings + "E"
            #self.startPointX = self.startPointX + 20

        else:
            surroundings = surroundings + "X"

        if grid[gridpositionY][gridpositionX-1] == 1:
            surroundings = surroundings + "W"
            #self.startPointX = self.startPointX - 20

        else:
            surroundings = surroundings + "X"

        
        if grid[gridpositionY+1][gridpositionX] == 1:
            surroundings = surroundings + "S"
            #self.startPointY = self.startPointY + 20

        else:
            surroundings = surroundings + "X"

        
            

        return surroundings



    def makeTrail(self, changeVar, temp):

        if changeVar ==1:
            trail = Rectangle(Point(self.startPointX,temp), Point(self.startPointX+20,temp+20))

        elif changeVar == 0:
            trail = Rectangle(Point(temp,self.startPointY), Point(temp+20,self.startPointY+20))
        
        trail.setOutline("gray")
        trail.setFill("gray")

        trail.draw(self.win)

        

    def movePicobot(self, surroundings, groupedInstructions):

        

        changeVar = 0
        #change variable to 1 if y variable changes

        for currentRule in groupedInstructions[self.state]:       

            print("surroundings:  ",surroundings)
            print("currentrule:    ",currentRule[1])
            if surroundings == currentRule[1]:
                if currentRule[2] == "N":
                    self.picobot.move(0,-20)
                    temp=self.startPointY
                    self.startPointY = self.startPointY - 20
                    changeVar = 1
                    
                elif currentRule[2] == "E":
                    self.picobot.move(20,0)
                    temp=self.startPointX
                    self.startPointX = self.startPointX + 20
                    
                elif currentRule[2] == "S":
                    self.picobot.move(0,20)
                    temp=self.startPointY
                    self.startPointY = self.startPointY + 20
                    changeVar = 1
                    
                elif currentRule[2] == "W":
                    self.picobot.move(-20,0)
                    temp=self.startPointX
                    self.startPointX = self.startPointX - 20

                
                    
                self.state = currentRule[3]

                self.makeTrail(changeVar,temp)

                self.refresh()

                gridpositionX = self.startPointX//20
                gridpositionY = self.startPointY//20


                '''if self.trail[gridpositionX][gridpositionY]==0:
                    self.trail[gridpositionX][gridpositionY] = 3 # 3 means that this position has been traversed previously by picobot
                    self.trailsquares = self.trailsquares+1'''

                

               
                

                    

                
    def refresh(self):

        self.picobot.undraw()
        self.picobot.draw(self.win)



        
  #when picobot is on square, colour square grey
        
    '"picobot movement: can move through white squares, cannot pass through "' 
        




trailsquares=drawGrid(grid)

startLeft = Point(20,550)
startRight = Point(65,570)

exitLeft = Point(220, 550)
exitRight = Point(265, 570)

uploadLeft = Point(420, 550)
uploadRight = Point(465, 570)

btnStart = Button(window, startLeft, startRight, "green", "start")
btnExit = Button(window, exitLeft, exitRight, "red", "exit")
btnUpload = Button(window, uploadLeft, uploadRight, "cyan", "upload")


btnStart.drawButton()
btnExit.drawButton()



btnUpload.drawButton()



print(grid[0])

bot = Picobot(window, "red")
bot.drawBot()
bot.surroundings()

while True: 
    clickpoint = window.checkMouse()

           

            

    if btnExit.checkClick(clickpoint):
        window.close()

    if btnUpload.checkClick(clickpoint):
        rawInstructions = dialogueBox()
        instructions=readFile(rawInstructions)

        NInstructions=asterics(instructions, 0, "N")
        EInstructions=asterics(NInstructions, 1, "E")
        WInstructions=asterics(EInstructions, 2, "W")
        SInstructions=asterics(WInstructions, 3, "S")

        useableInstructions = SInstructions

                    

        groupedInstructions = {}

    #''' current state = i[0]'''
    #''' i = each line of instructions'''
        for i in useableInstructions:
            if i[0] in groupedInstructions:
                groupedInstructions[i[0]].append(i)
            else:
                    groupedInstructions[i[0]] = [i]

            print(groupedInstructions)

    if btnStart.checkClick(clickpoint):
            while True: #bot.trailsquares <trailsquares:                                   #checking to see if the problem is in the while loop
                bot.movePicobot(bot.surroundings(), groupedInstructions)
                    
                    
                    
                    #make the maze less glitchy:
                    #1.  write start point x and start point y as separate functions, call them after making the trail
                    #2.

                '''possible reason why the array isn't working: [first element is [0][0] not [1][1]]'''
              





        
        

    
