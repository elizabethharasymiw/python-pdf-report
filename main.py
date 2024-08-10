from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set Title font
pdf.set_font("Arial", size=32)

# Add a cell
pdf.cell(200, 10, txt="Welcome to FPDF!", ln=True, align='C')

# Set paragraph font
pdf.set_font("Arial", size=12)

# Add another 2 cells with different content
pdf.cell(200, 10, txt="Text Line 1", ln=True, align='C')
pdf.cell(200, 10, txt="Text Line 2", ln=True, align='C')

# Add an image
pdf.image("./TestXImage.png", x=10, y=30, w=50)

# Save the PDF with name .pdf
pdf.output("example.pdf")
