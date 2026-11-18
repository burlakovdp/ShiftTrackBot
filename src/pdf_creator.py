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
        self.set_font("PageFont", size=15)
        self.cell(80)
        self.cell(30, 10, self.doc_title, border=1, align="C")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font("PageFont", size=8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def set_doc_title(self, title):
        self.doc_title = title

def pdf_creator(user_id, title, data):
    pdf = PDF()
    pdf.set_doc_title(title)
    pdf.add_page()
    pdf.set_font("PageFont", size=12)
    with pdf.table() as table:
        for data_row in data:
            row = table.row()
            for datum in data_row:
                row.cell(str(datum))
    pdf.output(f"output/{user_id}_summary.pdf")
    return f"output/{user_id}_summary.pdf"