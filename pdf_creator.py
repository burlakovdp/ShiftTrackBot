from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=12)
# Printing title:
#pdf.cell(30, 10, "Сводка", border=1, align="C")
# Performing a line break:

for i in range(1, 41):
    pdf.cell(50, 5, f"Printing line number {i}", border=1, new_x="LMARGIN", new_y="NEXT")
pdf.output("new-tuto2.pdf")