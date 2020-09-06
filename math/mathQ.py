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

def generateQuestions(num, mode:int):
    qList = []
    qStrList = []
    additionCnt = 0
    
    for i in range(num):
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        operNum = random.randint(0, 1)
        operType = 'ADD' if operNum == 1 else 'SUBTRACT'
        
        while not validate(operType, num1, num2):
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
        
        qList.append(Question(num1, num2, operType))
        
        if operType == 'ADD':
            additionCnt = additionCnt + 1
    
    print('Additon: ' + str(additionCnt))
    
    for q in qList:
        qStrList.append(q.getString())
    
    printQ(qStrList, mode)
    
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
    
generateQuestions(240, 2)