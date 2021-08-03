import turtle
t =turtle.Turtle()
#window.bgcolor("black")
#t.turtle.Turtle()
turtle.shape(turtle)
turtle.color(green)
turtle.width(11)
turtle.speed(0)
colors=["black","red"]
def heart():
  for blood in range(43):
      
     turtle.right(5)
     turtle.forward(5)
     turtle.forward(150)
     turtle.penup()
     turtle.right(140)
     turtle.forward(147)
     turtle.pendown()
     turtle.penup()
     turtle.right(110)
     turtle.forward()
     turtle.penup()
     turtle.left(90)
     turtle.forward(400) 
     turtle.pendown()
     heart()
window.exitonclick()