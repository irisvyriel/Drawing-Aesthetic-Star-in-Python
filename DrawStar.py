import turtle
import colorsys

def draw_square():
    brad = turtle.Turtle()
    brad.pencolor("white")
    h = 0
    n = 50
    brad.speed(0)
    for i in range(380):
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h = h + 1/n
        brad.color(c)
        brad.forward(i * 2)
        brad.left(145)

window = turtle.Screen()
window.bgcolor("black")

draw_square()

window.exitonclick()