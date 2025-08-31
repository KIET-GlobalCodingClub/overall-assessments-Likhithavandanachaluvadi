from fpdf import FPDF
import os

def create_certificate(name, roll, dept, filename):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.set_font("Arial", 'B', 24)
    pdf.cell(0, 20, "Certificate of Participation", ln=True, align='C')

    pdf.ln(20)
    pdf.set_font("Arial", '', 16)
    pdf.cell(0, 10, "This is to certify that", ln=True, align='C')

    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 15, name, ln=True, align='C')

    pdf.set_font("Arial", '', 14)
    pdf.cell(0, 10, f"Roll Number: {roll}", ln=True, align='C')
    pdf.cell(0, 10, f"Department: {dept}", ln=True, align='C')

    pdf.ln(10)
    pdf.cell(0, 10, "has participated in the event.", ln=True, align='C')

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    pdf.output(filename)
