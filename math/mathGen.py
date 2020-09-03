from fpdf import FPDF   

def printQ(qList):  
    # save FPDF() class into a  
    # variable pdf 
    pdf = FPDF() 
      
    # Add a page 
    pdf.add_page() 
      
    # set style and size of font  
    # that you want in the pdf 
    pdf.set_font("Arial", size = 15) 
    
    # create a cell 
    pdf.cell(200, 10, txt = "GeeksforGeeks",  
             ln = 2, align = 'C') 
             
    lnValue = 1;
      
    for q in qList:
        # Control whether to start from a new line
        lnValue = 1 - lnValue
        
        # add quesiton cell 
        pdf.cell(100, 10, q, 
                 ln = lnValue, align = 'L') 
      
    # save the pdf with name .pdf 
    pdf.output("GFG.pdf")

list = ['1 + 1 = ', '2 + 2 = ', '3 + 3 = ', '4 + 4 = ']

printQ(list)    