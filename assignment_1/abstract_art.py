from turtle import *
import time

setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)
colormode(255)

#background_color = input("Choose a background color: ")
#drawing_color = input("Choose a drawing color: ")
#bgcolor(background_color)
#color(drawing_color)

background_color = int(input("Enter a number between 0-16777215 representing the background color: "))
drawing_color = int(input("Enter a number between 0-16777215 representing the drawing color: "))

Bb = background_color %
background_color -= Bb
background_color /= 256
Bg = background_color % 256
background_color -= Bg
background_color /= 256
Br = background_color % 256


print("R:", Br, "\tG:", Bg, "\tB:", Bb)

Rb = drawing_color % 256
drawing_color -= Rb
drawing_color /= 256
Rg = drawing_color % 256
drawing_color -= Rg
drawing_color /= 256
Rr = drawing_color % 256



bgcolor(int(Br), int(Bg), int(Bb))
color(int(Rr), int(Rg), int(Rb))
begin_fill()
right(10)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()

time.sleep(10)