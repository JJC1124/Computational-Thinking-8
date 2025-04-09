import turtle
turtle.Screen().bgcolor("black")
t = turtle.Turtle()

t.goto(100, 0)
t.color("turquoise")
        

for i in range( 100 ) :
    t.forward( 120 )
    t.left(45 + 1)

for i in range( 75 ) :
    t.forward( 72 )
    t.left(50 + 1)

t.goto(0, 100)
t.color("purple")
for i in range( 100) :
    t.forward( 120)
    t.left(45 + 1)

t.goto(-100, 0)
t.color("red")
for i in range( 75) :
    t.forward( 60 )
    t.left(75 + 1)

t.goto(0, -100)
t.color("green")
for i in range( 100) :
    t.forward( 120)
    t.left(45 + 1)



turtle.exitonclick()