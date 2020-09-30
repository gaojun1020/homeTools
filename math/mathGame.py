from vpython import *
from random import random
import string
import sys
import time
from mathLib import Question, Test

# This program is a game where the user types the letters that fall before they
# reach the blue ground. A point is awarded for correct key strokes and
# subtracted for incorrect key strokes. The users avg reaction time is displayed.

# Initialize math test
numOfQ = 200
test = Test(numOfQ)
questions = test.getPrintableQs('normal') #make list of math questions

home = canvas(width=1200, height=600)
floor = box(canvas = home, pos = vector(0,-10,0), size = vector(40,2,2), color = color.blue)
warning = text(canvas = home, pos=vector(-10,10,10), text = "Answer  before it falls!", height = 1, depth = 0.1, color=color.white)

kbInput = ''
t=0
dt=0.01

target = label(canvas = home, pos=vector(0,20,0), text='X', color=color.green, height = 20, border=2) #target text object

score = label(canvas = home, pos=vector(15,-15,0)) #display score
wrong = label(canvas = home, pos=vector(-2,-15,0)) #display # of wrong keystrokes
rTime = label(canvas = home, pos=vector(15,-17,0)) #display reaction time
AVGrtime = label(canvas = home, pos=vector(-2,-17,0)) #display average reaction time
target.pos = vector(0,20,0) #initial target position
target.velocity = vector(0, -1, 0) #initial target velocity

i = 0 #increments through alphabet
points = 0 #point counter
wrongCnt = 0 #incorrect keystrokes
rT = 0. #reaction time counter
l=[] #list of reaction time
reactionTime = 0. #reaction time
avgRT = 0.
endGame = False
answer = ''

# Initialize question
target.text = questions[0]

def keyInput(evt):
    global rT, points, target, wrongCnt, l, warning, i, endGame, kbInput, answer
    
    s = evt.key
    print(s + " is pressed")
    
    if s == '\n':
        answer = int(kbInput) if kbInput.isdigit() else None        
        print('answer = ' + answer) 
        kbInput = ''
        
        if answer == test.questions[i].answer:
            reactionTime = rT 
            target.pos = vector(-10 + 2 * 10 * random(), 20, 0) #new starting position
            target.velocity.y = target.velocity.y * 1.05 #increase veloctiy
            points = points + 1 #add one points 
            l.append(reactionTime) 
            rT = 0
            i = int(round(numOfQ * random())) #change to new letter
        else:
            points = points - 1
            wrongCnt = wrongCnt + 1
            rT = 0

    elif s != 'alt':        
        kbInput += s
    
    if s == 'backspace':
        gameover = label(canvas = home, pos=vector(0,10,0), text = "Game Over Man")
        warning.color = vector(0, 0, 0) 
        target.velocity.y = 0
        endGame = True

home.bind('keydown', keyInput)

while target.pos.y > -10 and not endGame : 
    rate(100)
    target.text = questions[i] #pick a letter
    score.text = "Score: " + str(points)
    wrong.text = "Wrong: " + str(wrongCnt)
    rTime.text = "Reaction Time: " + str(reactionTime)
    AVGrtime.text = "Average RT: " + str(avgRT)
    
    target.pos = target.pos + target.velocity * dt #make the letter fall
    t = t + dt #increment time
    rT = rT + dt

if len(l) > 0:
    m = sum(l) #add up list of reaction times 
    avg = m / len(l) 
    avgRT = round(avg, 4)

warning.color = vector(0,0,0)
gameover = label(canvas = home, pos=vector(0,10,0), text = "Game Over Man. Shutting down...")
time.sleep(3)

print('Score: ' + str(points))
print('Wrong: ' +str(wrongCnt))
print('Avg Reaction Time: ' + str(avgRT))

import os
import signal
os.kill(os.getpid(), signal.SIGINT)