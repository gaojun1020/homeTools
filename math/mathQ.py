from mathGen import printQ
import random

class Question:
    def __init__(self, num1, num2, operType):
        self.num1 = num1
        self.num2 = num2
        self.operType = operType
        
    def getString(self):
        if self.operType == 'ADD':
            oper = '+'
        else:
            oper = '-'
    
        return str(self.num1) + ' ' + oper + ' ' + str(self.num2) + ' = '

def generateQuestions(num):
    qList = []
    qStrList = []
    
    for i in range(num):
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        operNum = random.randint(0, 1)
        operType = 'ADD' if operNum == 0 else 'SUBTRACT'
        
        while not validate(operType, num1, num2):
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
            operNum = random.randint(0, 1)
            operType = 'ADD' if operNum == 0 else 'SUBTRACT'

        
        qList.append(Question(num1, num2, operType))
    
    for q in qList:
        qStrList.append(q.getString())
    
    printQ(qStrList)
    
def validate(operType, num1, num2):
    if operType == 'SUBTRACT' and num1 <= num2:
        return False
        
    return True
    
generateQuestions(120)