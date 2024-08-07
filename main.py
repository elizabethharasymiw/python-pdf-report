from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=18)

# Add a cell
pdf.cell(200, 10, txt="Welcome to FPDF!", ln=True, align='C')

# Add another cell with different content
pdf.cell(200, 10, txt="Text Line 1", ln=True, align='C')
pdf.cell(200, 10, txt="Text Line 2", ln=True, align='C')

# Save the PDF with name .pdf
pdf.output("example.pdf")
