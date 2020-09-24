# -*- coding: UTF-8 -*-
from mathGen import printQ
from termcolor import colored

import random
import io
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

class Test:
    correctQs = []
    incorrectQs = []
    
    def addCorrectQ(self, q):
        self.correctQs.append(q)
        
    def addIncorrectQ(self, q):
        self.incorrectQs.append(q)
        
    def getReport(self):
        correctNum = len(self.correctQs)
        incorrectNum = len(self.incorrectQs)
        score = 100 * correctNum / (correctNum + incorrectNum)
    
        return 'Correct:' + str(correctNum) + ', ' + 'Incorrect:' + str(incorrectNum) + '. Final score is ' + str(score) + '.'


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

test = Test()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')    
os.system('color')

print('Test starting... 3')
time.sleep(1)
print('Test starting... 2')
time.sleep(1)
print('Test starting... 1')
time.sleep(1)
print('GO!')
print()
print('---')
print()

for i in range(10):
    q = generateSingleQ()
    answer = int(input(' ' + q.getString('normal') + ': '))

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

print()
print(test.getReport())