from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("PageFont", style="", fname="assets/fonts/Inter_Regular.ttf")
        self.add_font("PageFont", style="I", fname="assets/fonts/Inter_Italic.ttf")
        self.add_font("PageFont", style="B", fname="assets/fonts/Inter_Bold.ttf")
        self.add_font("PageFont", style="BI", fname="assets/fonts/Inter_BoldItalic.ttf")
        self.doc_title = "No Name"

    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("PageFont", size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, self.doc_title, border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("PageFont", size=8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def set_doc_title(self, title):
        self.doc_title = title

def pdf_creator(user_id, title, data):
    head = [('Date', 'Shift', 'Amo', 'Tg')]
    data.reverse()
    data = head + data
    pdf = PDF()
    pdf.set_doc_title(title)
    pdf.add_page()
    pdf.set_font("PageFont", size=12)
    print(data)
    with pdf.table() as table:
        for data_row in data:
            row = table.row()
            for datum in data_row:
                row.cell(str(datum))
    pdf.output(f"output/{user_id}_summery.pdf")
    return f"output/{user_id}_summery.pdf"