import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500,500)

side = 5
angle = 144
star = turtle.Turtle()
for i in range (5):
    star.forward(100)
    star.left(angle)
turtle.done()