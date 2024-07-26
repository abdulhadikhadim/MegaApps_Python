import pandas as pd 
import glob
from pathlib import Path
from fpdf import FPDF

filepaths = glob.glob('text/*.txt')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem.title()
    df = pd.read_table(filepath)
    # print(df)
    pdf.set_font(family='Times', style='B',size=16)
    pdf.cell(w=50,h=8,txt=filename,ln=1)

    with open(filepath,'r') as file:
        content = file.read()
    pdf.set_font(family='Times', style='B',size=16)
    pdf.multi_cell(w=0,h=6,txt = content)
    

pdf.output("Output.pdf")

