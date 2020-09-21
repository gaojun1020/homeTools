from mathGen import printQ

import random
import sys

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

def generateQuestions(num, numCol:int, mode):
    qList = []
    qStrList = []
    additionCnt = 0
    
    for i in range(num):
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        operNum = random.randint(0, 2)
        operType = 'ADD' if operNum == 1 else 'SUBTRACT'
        
        while not validate(operType, num1, num2):
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
        
        qList.append(Question(num1, num2, operType))
        
        if operType == 'ADD':
            additionCnt = additionCnt + 1
    
    print('Additon: ' + str(additionCnt))
    
    for q in qList:
        qStrList.append(q.getString(mode))
    
    printQ(qStrList, numCol)
    
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

if len(sys.argv) != 4:
    numOfQ = int(input("Number of questions:"))
    numOfCol = int(input("Number of columns:"))
    mode = input("Question Mode (1:normal/2:fillBlank):")
else:
    numOfQ = int(sys.argv[1])
    numOfCol = int(sys.argv[2])
    mode = sys.argv[3]

if mode == '1':
    mode = 'normal'
else:
    mode = 'fillBlank'


print("Generating a paper with [%s] questions in [%s] columns with mode:[%s]..."%(numOfQ, numOfCol, mode))
    
generateQuestions(numOfQ, numOfCol, mode)