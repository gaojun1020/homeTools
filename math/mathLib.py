import random
import time

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
    
    #decide num of + vs -
    operNum = random.randint(0, 1)
    operType = 'ADD' if operNum == 1 else 'SUBTRACT'
    
    while not validate(operType, num1, num2):
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        
    return Question(num1, num2, operType)
    
def validate(operType, num1, num2):
    if operType == 'SUBTRACT' and num1 <= num2:
        return False
    elif num1 > 30 or num2 > 30:
        return False
    elif num1 < 10 and num2 < 10:
        return False
    elif num1 < 6 or num2 < 6:
        return False
    elif operType == 'ADD' and (num1 % 10 == 0 or num2 % 10 == 0):
        return False
        
    return True