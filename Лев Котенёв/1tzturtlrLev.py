import turtle

rm = turtle.Turtle()
rm.shape("turtle")

rm.color('black','brown')
rm.begin_fill()

for i in range(4):
    rm.forward(100)
    rm.right(90)
    
rm.end_fill()

rm.penup()

rm.right(90)
rm.forward(40)
rm.left(90)
rm.forward(20)

rm.pendown()

rm.color('black','blue')
rm.begin_fill()

for i in range(4):
    rm.forward(20)
    rm.right(90)

rm.penup()

rm.forward(40)

rm.pendown()

for i in range(4):
    rm.forward(20)
    rm.right(90)

rm.end_fill()

rm.penup()

rm.backward(10)
rm.left(90)
rm.forward(40)
rm.left(90)
rm.forward(50)
rm.right(135)

rm.pendown()

rm.color('black','red')
rm.begin_fill()

rm.forward(50*(2**(1/2)))
rm.right(90)
rm.forward(50*(2**(1/2)))

rm.end_fill()

rm.color('orange','yellow')
rm.begin_fill()

rm.penup()
rm.right(180)
rm.forward(200)

rm.pendown()

rm.circle(50)

rm.end_fill()