from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set Title font
pdf.set_font("Arial", style='B', size=32)

# Add a cell
pdf.cell(200, 10, txt="Welcome to FPDF!", ln=True, align='C')

# Set paragraph font
pdf.set_font("Arial", size=12)

# Add another 2 cells with different content
pdf.cell(200, 10, txt="Text Line 1", ln=True, align='C')
pdf.cell(200, 10, txt="Text Line 2", ln=True, align='C')

# Add an image
pdf.image("./TestXImage.png", x=10, y=30, w=50)

# Move the cursor to a new line to add bullet points
pdf.ln(60)

# Bullet points
bullet_points = [
    "Bullet point 1",
    "Bullet point 2",
    "Bullet point 3"
]

# Add bullet points to the PDF
for point in bullet_points:
    pdf.cell(10, 10, txt="-", ln=False)
    pdf.cell(190, 10, txt=point, ln=True)

# Save the PDF with name .pdf
pdf.output("example.pdf")
