import turtle

rm = turtle.Turtle()
rm.shape("turtle")

l=turtle.textinput('Цвет','В какой цвет покрасим лапки?')
g=turtle.textinput('Цвет','В какой цвет покрасим голову?')
p=turtle.textinput('Цвет','В какой цвет покрасим панцерь?')

rm.penup()
rm.forward(30)
rm.pendown()

rm.color(l,l)
rm.begin_fill()

rm.circle(10)

rm.end_fill()

rm.penup()
rm.right(180)
rm.forward(60)
rm.right(180)
rm.pendown()

rm.color(l,l)
rm.begin_fill()

rm.circle(10)

rm.end_fill()

rm.penup()
rm.left(90)
rm.forward(95)
rm.pendown()

rm.color(l,l)
rm.begin_fill()

rm.circle(10)

rm.end_fill()

rm.penup()
rm.right(90)
rm.forward(60)
rm.right(90)
rm.pendown()

rm.color(l,l)
rm.begin_fill()

rm.circle(10)

rm.end_fill()

rm.penup()
rm.right(90)
rm.forward(30)
rm.right(180)
rm.pendown()

rm.color(g,g)
rm.begin_fill()

rm.circle(20)

rm.end_fill()

#final part

rm.penup()
rm.goto(0,0)
rm.pendown()

rm.color(p,p)
rm.begin_fill()

rm.circle(52)

rm.end_fill()




