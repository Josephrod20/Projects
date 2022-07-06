#-------------------------------------------------------------------------------
# Joseph Rodriguez
# jrodr273@ucsc.edu
# programming assignment 2
# I will use the turtle module to draw an n pointed star, where
# n is any odd integer greater than or equal to 3 and is obtained from user input.
#-------------------------------------------------------------------------------

import turtle

def draw_triangle(t, sz):
    tess.setpos(-150,0)
    for i in range (x):
        t.forward(300)
        t.right(180 - 180 / x)
        t.dot(10,"red")
        
 
 


#-- main program --------------------------------------------------------------
wn = turtle.Screen()        
wn.bgcolor("white")

x=int(input("Enter an odd integer greater than or equal to 3:"))

tess = turtle.Turtle()     
tess.pensize(3)

tess.color("blue","green")
tess.speed(4)             


tess.begin_fill()

draw_triangle(tess, 2)
             



tess.end_fill()

wn.mainloop()
