from turtle import *
import random
shape("turtle")
col=["orange","limegreen","gold","plum","tomato"]
for i in range(15):
    color(random.choice(col))
    circle(100)
    left(30)
done()