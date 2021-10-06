# different kind of sun in a blue sky
import turtle

kk = turtle.Turtle()

kk.color
kk.getscreen().bgcolor("skyblue")
kk.pensize(3)
kk.hideturtle()
kk.speed(105)

kk.begin_fill()

for i in range(50):

    kk.fd(350)
    kk.left(175)
    kk.fd(350)
    kk.right(150)

kk.end_fill()

turtle.done()
