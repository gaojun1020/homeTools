from fpdf import FPDF   

from mathLib import Test, Question
from mathLib import generateSingleQ

import sys

def printQ(qList, mode:int):  
    if mode <= 2:
        mode = 2
    elif mode >= 4:
        mode = 4

    # save FPDF() class into a  
    # variable pdf 
    pdf = FPDF() 
      
    # Add a page 
    pdf.add_page() 
      
    # set style and size of font  
    # that you want in the pdf 
    pdf.set_font("Arial", size = 11) 
    
    lnValue = 1
    index = 0
    
    # mode - 2: 0, 1
    # mode - 3: 0, 0, 1
    # mode - 4: 0, 0, 0, 1
    for q in qList:
        # Control whether to start from a new line
        if (index + 1) % mode == 0:
            lnValue = 1
        else:
            lnValue = 0
        
        # add quesiton cell 
        pdf.cell(200 / mode, 8, q, 
                 ln = lnValue, align = 'L') 
				 
        index = index + 1
		
        if index % (5 * mode) == 0:
            pdf.cell(100, 4, '-----------------------------------------------------------------------------', 
                 ln = 0, align = 'L') 
            pdf.cell(100, 4, '-----------------------------------------------------------', 
                 ln = 1, align = 'L') 
			
      
    # save the pdf with name .pdf 
    pdf.output("math-001.pdf")
    
def generateQuestions(num, numCol:int, mode):
    qStrList = []
    
    test = Test(num)
    
    for q in test.questions:
        qStrList.append(q.getString(mode))
    
    printQ(qStrList, numCol)

####################################################    
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