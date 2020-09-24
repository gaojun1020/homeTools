from fpdf import FPDF   

pdf = FPDF(orientation = 'L', unit = 'mm', format='A4')

# imagelist is the list with all image filenames
image = 'D:\\data\lab\\homeTools\\image\\usa.png'
#pdf = FPDF(unit = "pt", format = [width, height])
pdf.add_page()
pdf.image(image,x=8,y=25,w=280,h=150)
pdf.output("usa.pdf", "F")