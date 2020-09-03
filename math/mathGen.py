from fpdf import FPDF   

def printQ(qList):  
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

    for q in qList:
        # Control whether to start from a new line
        lnValue = 1 - lnValue
        
        # add quesiton cell 
        pdf.cell(100, 8, q, 
                 ln = lnValue, align = 'L') 
				 
        index = index + 1
		
        if index % 10 == 0:
            pdf.cell(100, 4, ' ', 
                 ln = 1, align = 'L') 
			
      
    # save the pdf with name .pdf 
    pdf.output("math-001.pdf")