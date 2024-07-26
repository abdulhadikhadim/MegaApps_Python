from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False,margin=0)
df = pd.read_csv('topics.csv',sep = ',')


'''
w is the width of the cell
h is the height of the cell
txt this is the text of the cell
border, border = 1 means it covers the whole area of the page
ln =1 means it only take one cell in a line 
align means it is either left or right
    pdf.cell(w=0,h=12,txt=f"{row}",border=1,ln = 1,align='L')

'''

for index , row in df.iterrows():
    pdf.add_page()
    #set the header
    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=f"{row['Topic']}",ln = 1,align='L')
    sep = 10
    for i in range(27):
        pdf.line(10,22+sep*i,200,22+sep*i)

    #setr the footer
    pdf.ln(265)
    pdf.set_font(family='Times',style='I',size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=f"{row['Topic']}",align='R')
    

    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(265)
        pdf.set_font(family='Times',style='I',size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=f"{row['Topic']}",align='R')
        sep1 = 10
        for i in range(27):
            pdf.line(10,22+sep1*i,200,22+sep1*i)

pdf.output("output.pdf")