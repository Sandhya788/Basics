import turtle
   
pegasus=turtle.Turtle()
pegasus.speed(20)
pegasus.getscreen().bgcolor("green")
pegasus.penup()
pegasus.goto((-200,100))
pegasus.pendown()

def star(turtle, size):
    if size <= 10:
      return
    else:   
         for i in range(5):
           turtle.forward(size)
           star(turtle,size/3)
           turtle.left(216)
           turtle.end_fill()
star(pegasus,360)
turtle.done()