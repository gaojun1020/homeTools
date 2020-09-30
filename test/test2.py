from vpython import *

floor = box (pos=vector(0,0,0), length=4, height=0.5, width=4, color=color.blue)
#ball = sphere (pos=vector(0,4,0), radius=1, color=color.red)
ball = text(pos=vector(5,20,0), text='X', depth=-0.3, color=color.green, height = 3)
ball.velocity = vector(0,-1,0)
dt = 0.01

while 1:
    rate (100)
    ball.pos = ball.pos + ball.velocity * dt
    if ball.pos.y < ball.height:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt