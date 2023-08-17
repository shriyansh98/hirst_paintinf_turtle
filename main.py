from turtle import Turtle , Screen ,colormode
from random import choice
colormode(255)

squirtal  = Turtle()
squirtal.speed("fastest")
squirtal.penup()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
pallate = [(202, 110, 164), (240, 241, 245), (236, 243, 239), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), 
 (138, 20, 31), (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), (232, 165, 176), 
 (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), (147, 19, 17),
 (27, 102, 68), (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99)]



turn_angle = 90
space_size = 50
dot_size = 20
rows = 0
no_of_dots =10
def line_func(no_dots):
    squirtal.dot(dot_size,choice(pallate))
    if (no_of_dots-1)>no_dots:
        
        squirtal.forward(space_size)
        
        


def next_row_left():
    squirtal.left(turn_angle)
    
    squirtal.forward(space_size)
    
    squirtal.left(turn_angle)
    
def next_row_right():
    squirtal.right(turn_angle)
    
    squirtal.forward(space_size)
    
    squirtal.right(turn_angle)

squirtal.setheading(225)
squirtal.forward(300)
squirtal.setheading(0)
squirtal.forward(50)

while rows != 10:
    for i in range(0,no_of_dots):
        
        
        
        
        
        
        
        line_func(i)
    if rows%2 == 0: 
        next_row_left()
    else:
        next_row_right()

    rows += 1 
    

    
    
screen = Screen()
screen.exitonclick()