from fpdf import FPDF   
from mathLib import Test, Question
import webbrowser
import sys
import datetime

OUTPUT_PATH = 'D:/data/temp/mathTests'

def printQ(qList, mode:int):  
    now = datetime.datetime.now()
    outputFilename = 'math_test_' + now.strftime('%Y%m%d%H%M%S') + '_' + now.strftime('%f') + '.pdf'
    
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
    pdf.output(OUTPUT_PATH + '\\' + outputFilename)
    webbrowser.open_new(r'file://' + OUTPUT_PATH + '\\' + outputFilename)
    
def parseInput(prompt, default):
    result = ''
    
    while(result != '$ERROR$'):
        inputStr = input(prompt)

        try:
            result = int(inputStr)
            
            break
        except ValueError:
            if inputStr == '':
                result = default
                
                break
            else:
                result = '$ERROR$'
    
    return result

####################################################   

try:
    numOfQ = int(sys.argv[1])
    numOfCol = int(sys.argv[2])
    numScope = int(sys.argv[3])
    mode = int(sys.argv[4])
except:   
    numOfQ = parseInput("Number of questions:(120)", 120)
    numOfCol = parseInput("Number of columns:(4)", 4)
    numScope = parseInput("No larger than number:(40)", 40)
    mode = parseInput("Question Mode: (1:normal(default); 2:fillBlank)", 1)

if mode == 1:
    mode = 'normal'
else:
    mode = 'fillBlank'


print("Generating a paper with [%s] questions in [%s] columns, no larger than [%s], with mode:[%s]..."%(numOfQ, numOfCol, numScope, mode))
    
test = Test(numOfQ, numScope)    
printQ(test.getPrintableQs(mode), numOfCol)
