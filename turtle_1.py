import turtle

ws = turtle.Turtle()
ws.speed(0)

def checkColor(number):
   if number % 2 == 0:
      ws.color("red")
   else:
      ws.color("orange")

for j in range (1,300):
  checkColor(j)
  for i in range (1,6):
      ws.left(144)
      ws.forward(j*3)
  ws.left(5)
turtle.done()