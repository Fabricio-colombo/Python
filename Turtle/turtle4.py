import turtle as tur

tur.bgcolor('black')
tur.width(3)
tur.speed(50)
for steps in range(200):
    for c in ('blue', 'red', 'green'):
        tur.color(c)
        tur.forward(steps)
        tur.right(30)