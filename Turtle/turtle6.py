import turtle as tur
from random import random

tur.bgcolor('purple')
tur.color('black')
tur.width(3)
tur.speed(10)


for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    tur.right(angle)
    tur.fd(steps)

tur.screen.mainloop()