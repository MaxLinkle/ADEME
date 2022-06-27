import turtle as tu

slices = 4


def separator():
    for _ in range(10):
        tu.pendown()
        tu.forward(15)
        tu.penup()
        tu.forward(15)


tu.screensize(200, 200)
tu.pencolor("gray")
tu.pensize(3)

tu.penup()
tu.goto(0, -300)
tu.pendown()

tu.left(30)
for _ in range(6):
    tu.forward(300)
    tu.left(60)

tu.left(60)
tu.pensize(2)
tu.penup()
tu.goto(0, 0)

if slices != 0 or slices != 1:
    angle = 360 // slices
    for _ in range(slices):
        separator()
        tu.penup()
        tu.goto(0, 0)
        tu.right(angle)

tu.done()
