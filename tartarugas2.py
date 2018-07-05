import turtle

toto = turtle.Turtle()
toto.goto(-100, -100)
toto.write("toto inicio", font=("Arial", 11, "bold"))
toto.forward(100)
toto.write("toto fim", font=("Arial", 11, "bold"))

titi = turtle.Turtle()
titi.goto(100, 100)
toto.write("titi inicio", font=("Arial", 11, "bold"))
titi.forward(150)
titi.write("titi fim", font=("Arial", 11, "bold"))

titi.penup()
titi.forward(10000000000)