from graphics import *
from math import *
#these are all the functions that are used to actually allow the whole patch work to actually function
def drawSquare(topLeft, dimension,win,colour):
    tlx1 = topLeft.getX()
    tly1 = topLeft.getY()
    tlx2 = tlx1 + dimension
    tly2 = tly1 + dimension
    bottomRight = Point(tlx2,tly2)
    r = Rectangle(topLeft, bottomRight)
    r.draw(win)
    r.setOutline(colour)
    r.setFill(colour)
     
def drawTriangle(point1, point2, point3, win, colour):
    t = Polygon(point1, point2, point3)
    t.draw(win)
    t.setFill(colour)
    t.setOutline(colour)
    
def drawCirlce(p, dimension, colour, win):
    c = Circle(p, dimension)
    c.draw(win)
    c.setFill(colour)
    c.setOutline(colour)

def gSize():#this is a get size function
    while True: # this is while statement is used for the user to input one of the 3 numbers for the size, this also give validation since it will only accept 5, 7 and 9
        size = int(input("pick a size 5, 7, 9: "))
        if size not in [5, 7, 9]:
            print("invalide choose either 5, 7, 9")
            continue
        else:
            return size
            break
        
def cDV():# this is a colour digit verification
 # this list is here to let the While/if statement underneath know what colours are allowed and what are not, -
 # this give validation to the system

    while True:  
        colour =  input("please choose either Red|Blue|Green|Orange|Magenta|Cyan, by using its first letter: ")       
        if colour == "r": #or colour == "red":
            return "red"
        elif colour == "b":
            return  "blue"
        elif colour == "g":
           return   "green"
        elif colour == "o":
            return "orange" 
        elif colour == "m":
            return "magenta"
        elif colour == "c":
            return "cyan"
        else:
            print("we do not support that colour, please choose either Red | Blue | Green | Orange | Magenta| Cyan, now please try again! ")
#------------------------------------------------------------------------------
def p2(basePoint, win, colour):
    #win = GraphWin("red stairs", 200,200)
    #colour = "red"
    #step = 11
    
    xBase = basePoint.getX()
    yBase = basePoint.getY()

    for i in range(0,100, 10):
        topLeft = Point(xBase + 0+i, yBase + 90-i)
        dimension = 10
        drawSquare(topLeft, dimension, win, colour)
            
#------------------------------------------------------------------------------for the patchWindow
#my second patch
def p6(basePoint, win, colour):
    
    xBase = basePoint.getX()
    yBase = basePoint.getY()

    
    for x in range(0, 100, 40):
        for y in range(0, 100, 40):
            for c in range(0,80,40):
                point1 = Point(xBase + 0 + x,yBase + 0 + y)
                point2 = Point(xBase + 10 + x,yBase + 10 + y)
                point3 = Point(xBase + 20 + x,yBase + 0 + y)
                drawTriangle(point1, point2, point3, win, colour)
                
                point1 = Point(xBase + 0 + x, yBase + 10 + y)
                point2 = Point(xBase + 10 + x ,yBase + 20 + y)
                point3 = Point(xBase + 20 + x , yBase + 10 + y)
                drawTriangle(point1, point2, point3, win, colour)
                
                p = Point(xBase + 10 + x ,yBase + 30 + c)
                dimension = 10
                drawCirlce(p, dimension, colour, win)
                
    for x in range(0, 80, 40):
        for y in range(0, 80, 40):
            for c in range(0, 100,40):             
                point1 = Point(xBase + 20+ x, yBase + 20 + y)
                point2 = Point(xBase + 30+ x, yBase + 30 + y)
                point3 = Point(xBase + 20+ x, yBase + 40 + y)
                drawTriangle(point1, point2, point3, win, colour)
                
                point1 = Point(xBase + 30+ x, yBase + 20 + y)
                point2 = Point(xBase + 40+ x, yBase + 30 + y)
                point3 = Point(xBase + 30+ x, yBase + 40 + y)
                drawTriangle(point1, point2, point3, win, colour)
                
                p = Point(xBase + 30 + x , yBase + 10 + c)
                dimension = 10
                drawCirlce(p, dimension, colour, win)

#-----------------------------------------------------------------------------
#this is the design of the patch for 5, 7, and 9, with the ability to chose the colour 
def fPD(): #the fial patch design
    size = gSize()      
    colour1 = cDV()
    colour2 = cDV()
    colour3 = cDV()
        
    win = GraphWin("ex9", size*100, size*100)
    edge = size*100  - 100 
    eM = edge - 100 
    eM2 = edge - 200#everything under when it reaches a certain length and width you need to use these to accompany the take away because -
    eM3 = edge - 300 #when it gets really long not using these will make the smaller version (like 5) be wring due a colur being in the wrong -
    eM4 = edge - 400 #place, edge applies to all
    eM5 = edge - 500 
    eM6 = edge - 600
    
    for y in range (0,size*100,100):
        for x in range (0,size*100,100):
            
            basePoint = Point(x,y)
            
            if (x, y) == (edge, 0) or (x,y) == (200,eM2) or (x,y) == (0,edge) or (x,y) == (400, eM4) or (x,y) == (600,eM6):
                p2(basePoint, win, colour2)
            elif(x,y) == (eM,100) or (x,y) == (100,eM) or (x,y) == (300, eM3) or (x,y) == (500, eM5):
                p6(basePoint, win, colour2)
            elif x == 200 and y >= eM2 or x == edge or x == 400 and y >= eM4 or x == 600 and y >= 300:
                p2(basePoint, win, colour3)
            elif x == eM and y >= 100 or x == 100 and y >= edge or x == 300 and y >= eM2 or x == 500 and y >= 300:
                p6(basePoint, win, colour3)
            else:
                p6(basePoint, win, colour1)

    win.getMouse()
    win.close()
#------------------------------------------------------------------------------------------------------------------------
# this under here is for tessing the movement of my patches, this is irellevent to the course work
