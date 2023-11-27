from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page(orientation= "portrait",format= (210,297))
pdf.set_font("Helvetica","B",50)
pdf.cell(0,60,"CS50 Shirtificate",align="C")
pdf.image("shirtificate.png",x = 0, y = 70)
pdf.set_font_size(18)
pdf.set_text_color(255,255,255)
pdf.text(x=45,y=145,txt = f"{name} took CS50")
pdf.output("shirtificate.pdf")
