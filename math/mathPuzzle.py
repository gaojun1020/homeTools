# -*- coding: UTF-8 -*-
from playsound import playsound
from mathGen import printQ
from prettyTime import pretty_time_delta
from printUtil import printMe
from termcolor import colored

import random
import os
import sys
import time
import winsound

class Question:
    def __init__(self, num1, num2, operType):
        self.num1 = num1
        self.num2 = num2
        self.operType = operType
        
        if self.operType == 'ADD':
            self.answer = num1 + num2
        else:
            self.answer = num1 - num2
        
    def getString(self, mode):
        if self.operType == 'ADD':
            oper = '+'
        else:
            oper = '-'
            
        if mode == 'normal':
            qStr = str(self.num1) + ' ' + oper + ' ' + str(self.num2) + ' = '
        elif mode == 'fillBlank':
            if random.randint(0, 1) == 0:
                qStr = '(   ) ' + oper + ' ' + str(self.num2) + ' = ' + str(self.answer)
            else:
                qStr = str(self.num1) + ' ' + oper + ' (   )' + ' = ' + str(self.answer)
    
        return qStr
        
    def __eq__(self, other): 
        if not isinstance(other, Question):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.num1 == other.num1 and self.num2 == other.num2 and self.operType == other.operType

class Test:
    questions = []
    correctQs = []
    incorrectQs = []
    
    def __init__(self, numOfQ):
        self.startTime = time.time()
        self.numOfQ = numOfQ
        
        for i in range(numOfQ):
            q = generateSingleQ()
            
            while q in self.questions:
                q = generateSingleQ()
                
            self.addQ(q)
    
    def addQ(self, q):
        self.questions.append(q)

    def addCorrectQ(self, q):
        self.correctQs.append(q)
        
    def addIncorrectQ(self, q):
        self.incorrectQs.append(q)
        
    def getSize(self):
        return self.numOfQ
        
    def start(self):
        self.startTime = time.time()

    def end(self):
        self.endTime = time.time()
    
    def getResult(self):
        correctNum = len(self.correctQs)
        incorrectNum = len(self.incorrectQs)
        score = int(100 * correctNum / (correctNum + incorrectNum))
        elapsedTime = round(self.endTime - self.startTime, 0)

        return (score, correctNum, incorrectNum, elapsedTime)
        
    def getReport(self):
        correctNum = len(self.correctQs)
        incorrectNum = len(self.incorrectQs)
        score = int(100 * correctNum / (correctNum + incorrectNum))
        elapsedTime = round(self.endTime - self.startTime, 0)
    
        return 'Correct:' + str(correctNum) \
               + ', ' + 'Incorrect:' + str(incorrectNum) \
               + '. Final score is ' + str(score) + '. ' \
               + 'Elapsed Time is ' + pretty_time_delta(elapsedTime) + '.'


def generateSingleQ():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operNum = random.randint(0, 2)
    operType = 'ADD' if operNum == 1 else 'SUBTRACT'
    
    while not validate(operType, num1, num2):
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        
    return Question(num1, num2, operType)
    
def validate(operType, num1, num2):
    if operType == 'SUBTRACT' and num1 <= num2:
        return False
    elif num1 > 20 or num2 > 20:
        return False
    elif num1 < 10 and num2 < 10:
        return False
    elif num1 < 6 or num2 < 6:
        return False
    elif operType == 'ADD' and (num1 % 10 == 0 or num2 % 10 == 0):
        return False
        
    return True

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
for i in range(test.numOfQ):
    q = generateSingleQ()
    
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

if test.getResult()[0] == 100:
    playsound('resource/cheer.mp3')
elif test.getResult()[0] < 80:
    playsound('resource/boo.mp3')
else:
    playsound('resource/Whistling.mp3')