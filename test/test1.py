from vpython import *
from random import random
import string

# This program is a game where the user types the letters that fall before they
# reach the blue ground. A point is awarded for correct key strokes and
# subtracted for incorrect key strokes. The users avg reaction time is displayed.
floor = box(pos=vector(0,-10,0), size = vector(40,2,2), color=color.blue)
warning = text(pos=vector(-10,10,10), text = "Type the letter before it falls!", height = 1, depth = 0.1, color=color.white)
t=0
dt=0.01
letters = [] #make list to store letters

for i in string.ascii_letters: 
    letters.append(i) #fill list with alphabet
    
target = label(pos=vector(0,20,0), text='X', color=color.green, height = 20, border=2) #target text object
score = label(pos=vector(15,-15,0)) #display score
wrong = label(pos=vector(-2,-15,0)) #display # of wrong keystrokes
rTime = label(pos=vector(15,-19,0)) #display reaction time
AVGrtime = label(pos=vector(-2,-19,0)) #display average reaction time
#target.pos = vector(0,20,0) #initial target position
target.velocity = vector(0, -3, 0) #initial target velocity

i = 0 #increments through alphabet
points = 0 #point counter
wrongCnt = 0 #incorrect keystrokes
rT = 0. #reaction time counter
l=[] #list of reaction time
reactionTime = 0. #reaction time
avgRT = 0.

target.text = letters[0]

def keyInput(evt):
    global rT, points, target, wrongCnt, l, warning, i
    
    s = evt.key
    
    if s == 'backspace':
        gameover = label(pos=vector(0,10,0), text = "Game Over Man")
        warning.color = vector(0, 0, 0) 
        target.velocity.y = 0

    if s == target.text:
        reactionTime = rT 
        target.pos = vector(-10 + 2 * 10 * random(),20,0) #new starting position
        target.velocity.y = target.velocity.y * 1.1 #increase veloctiy
        points = points + 1 #add one points 
        l.append(reactionTime) 
        rT = 0
        i = int(round(25 * random())) #change to new letter
    else:
        points = points - 1
        wrongCnt = wrongCnt + 1
        rT = 0
        
    print("key is " + s)

scene.bind('keydown', keyInput)


while target.pos.y > -10: 
    rate(100)
    target.text = letters[i] #pick a letter
    score.text = "Score: " + str(points)
    wrong.text = "Wrong: " + str(wrongCnt)
    rTime.text = "Reaction Time: " + str(reactionTime)
    AVGrtime.text = "Average RT: " + str(avgRT)
    
    target.pos = target.pos + target.velocity * dt #make the letter fall
    t = t + dt #increment time
    rT = rT + dt

m = sum(l) #add up list of reaction times 
avg = m / len(l) 
avgRT = round(avg, 4)

warning.color = vector(0,0,0)
gameover = label(pos=vector(0,10,0), text = "Game Over Man")

print('Score: ' + str(points))
print('Wrong: ' +str(wrongCnt))
print('Avg Reaction Time: ' + str(avgRT))