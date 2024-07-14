from turtle import *
speed('slowest')
s = 5
d = 100
for i in range (6):
    fd(100)
    lt(360/6)
    write(i, font =('Arial', 12, 'normal'))
    dot(360/s)

mainloop()