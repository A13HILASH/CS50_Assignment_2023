from fpdf import FPDF

class ShirtificatePDF():

    def __init__(self,name):
        self._pdf = FPDF()
        self._pdf.add_page(orientation= "portrait", format=(210,297))
        self._pdf.set_font("Helvetica","B",50)
        self._pdf.cell(0,60,"CS50 Shirtificate",align="C")
        self._pdf.image("shirtificate.png",x = 0, y = 70)
        self._pdf.set_font_size(18)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=45,y=145,txt = f"{name} took CS50")

    def addShirtificate(self,filename):
        self._pdf.output(filename) 


name = input("Name: ")
pdf = ShirtificatePDF(name)
pdf.addShirtificate("shirtificate.pdf")