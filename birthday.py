import turtle

t = turtle.Turtle()
turtle.title("Syafri")

screen=turtle.Screen()
screen.bgcolor("black")

#Drawing heart
t.color("red")
t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)

t.end_fill()

#Writing text
t.up()
t.setpos(-100,150)
t.down()
t.color('white')
t.write("Happy Birthday!!", font=("Victor Mono", 20))

t.ht

turtle.mainloop()