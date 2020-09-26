from mathGen import printQ
from mathLib import Question
from mathLib import generateSingleQ

import sys

def generateQuestions(num, numCol:int, mode):
    qList = []
    qStrList = []
    additionCnt = 0
    
    for i in range(num):
        q = generateSingleQ()
        qList.append(q)
        
        if q.operType == 'ADD':
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