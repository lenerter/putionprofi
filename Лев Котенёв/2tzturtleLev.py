import turtle
rm = turtle.Turtle()
rm.shape("turtle")
width = turtle.window_width()
height = turtle.window_height()
print(width)
print(height)
rm.penup()
rm.goto(480,405)
rm.pendown()
rm.goto(-480,405)
rm.goto(-480,-405)
rm.goto(480,-405)
rm.goto(480,405)
