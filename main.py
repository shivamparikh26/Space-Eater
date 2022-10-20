import turtle
import random
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(1000)
t.color("red")
t.penup()
t.goto(-200,200)
t.pendown()
t.speed(10)
for i in range(4):
  t.forward(400)
  t.right(90)

Score = 0
s = turtle.Turtle()
s.speed(1000)
s.color("white")
s.penup()
s.goto(-200,210)
s.pendown()
s.write("Score: "+ str(Score))

dots = []
for i in range(10):
  d = turtle.Turtle()
  d.color("red")
  d.speed(1000)
  d.shape("circle")
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  d.right(random.randint(0,360))
  d.penup()
  d.goto(x,y)
  dots.append(d)

t2 = turtle.Turtle()
t2.speed(1000)
t2.penup()
t2.color("blue")
t2.shape("turtle")
def turnright():
  t2.right(10)
def turnleft():
  t2.left(10)
screen.onkey(turnright,"right")
screen.onkey(turnleft,"left")
screen.listen()

def collision():
  if t2.xcor()>199 or t2.xcor()<-199 or t2.ycor()>199 or t2.ycor()<-199:
    t2.right(180)
    
while True:
  collision()
  t2.forward(7)
  for dot in dots:
    dot.forward(3)
    if dot.xcor()>199 or dot.xcor()<-199 or dot.ycor()>199 or dot.ycor()<-199:
      dot.right(180)
    if abs(t2.xcor()-dot.xcor())<10 and abs(t2.ycor()-dot.ycor())<10:
      x = random.randint(-200,200)
      y = random.randint(-200,200)
      dot.goto(x,y)
      Score+=1
      s.clear()
      s.write("Score: "+str(Score))
