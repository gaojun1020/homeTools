# -*- coding: UTF-8 -*-
from playsound import playsound
from prettyTime import pretty_time_delta
from printUtil import printMe
from termcolor import colored
from mathGen import printQ
from mathLib import Question, Test

import random
import os
import sys
import time
import winsound

###############################
os. system('CLS')     
numQ = int(sys.argv[1])
test = Test(numQ)
os.system('color')

winsound.Beep(2500, 200)
print('Test starting... 3')
time.sleep(1)

winsound.Beep(2500, 200)
print('Test starting... 2')
time.sleep(1)

winsound.Beep(2500, 200)
print('Test starting... 1')
time.sleep(1)

print('GO!')
winsound.Beep(2500, 1000)
print()
print('---')
print()

test.start()
for q in test.questions:
    try:
        answer = int(input(' ' + q.getString('normal') + ': '))
    except ValueError:
        answer = 8888888

    if answer == q.answer:
        test.addCorrectQ(q)
        
        print(colored('-----------------V', 'green'))
        
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 100  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        
        print()
    else:
        test.addIncorrectQ(q)
        
        print(colored('-----------------X', 'red'))
        
        frequency = 1500  # Set Frequency To 2500 Hertz
        duration = 600  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        print()

test.end()
print()
printMe(test.getResult()[0])
print('Completed in ' + pretty_time_delta(test.getResult()[3]) + '.')

"""
if test.getResult()[0] == 100:
    playsound('resource/cheer.mp3')
elif test.getResult()[0] < 80:
    playsound('resource/boo.mp3')
else:
    playsound('resource/Whistling.mp3')
"""