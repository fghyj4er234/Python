from turtle import *
from colorsys import hsv_to_rgb

speed(0)
bgcolor("black")
hue = 0
name = "UMAIR"

for i in range(75):
    rgb = hsv_to_rgb(hue, 1, 1)
    color(rgb)
    hue += 0.014

    left(1)
    forward(1)

    for _ in range(2):
        left(2)
        circle(140)

penup()
goto(0, -20)
for i, char in enumerate(name):
    rgb = hsv_to_rgb(hue + i * 0.1, 1, 1)
    color(rgb)
    write(char, align="center", font=("Arial", 24, "bold"))
    forward(24)

hideturtle()
done()