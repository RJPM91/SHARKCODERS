import turtle

demo = turtle.Pen()

demo.shape("turtle")

# START DRAWING A SQUARE
demo.forward(100)
demo.left(90)
demo.forward(100)
demo.left(90)
demo.forward(100)
demo.left(90)
demo.forward(100)

demo.color('blue')
demo.forward(200)
demo.right(90)
demo.forward(200)
demo.right(90)
demo.forward(200)
demo.right(90)
demo.forward(200)

dummy_var = input('Terminar?')