import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Variables
a_score = 0
b_score = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Player A: 0 Player B: 0", align="center", font = ("Courier", 24, "normal"))

#Function
def paddle_a_up():
  if paddle_a.ycor() < 260:
    ay = paddle_a.ycor()
    ay += 20
    paddle_a.sety(ay)
  
def paddle_a_down():
  if paddle_a.ycor() > -260:
    ay = paddle_a.ycor()
    ay -= 20
    paddle_a.sety(ay)
  
def paddle_b_up():
  if paddle_b.ycor() < 260:
    by = paddle_b.ycor()
    by += 20
    paddle_b.sety(by)
  
def paddle_b_down():
  if paddle_b.ycor() > -260:
    by = paddle_b.ycor()
    by -= 20
    paddle_b.sety(by)

#Key binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
while True:
   wn.update()


   #Move the ball
   ball.setx(ball.xcor() + ball.dx)
   ball.sety(ball.ycor() + ball.dy)

   #Border check
   if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
      
   if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
      
   if ball.xcor() > 390:
      ball.goto(0 , 0)
      ball.dx *= -1
      b_score += 1
      
   if ball.xcor() < -390:
      ball.goto(0 , 0)
      ball.dx *= -1
      a_score += 1

   #Paddle and ball collision
   if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60:
      ball.dx *= -1
      ball.setx(340)
   if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60:
      ball.dx *= -1
      ball.setx(-340)

   #Score
