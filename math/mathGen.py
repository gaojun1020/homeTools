from fpdf import FPDF   

# mode: number of colums
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