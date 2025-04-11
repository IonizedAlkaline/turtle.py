import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500,500)

side = int(input("How many sides should the shape have: "))
angle = 360 // side

polygon = turtle.Turtle()
for i in range(side):
    polygon.forward(100)
    polygon.left(angle)
turtle.done()