from fpdf import FPDF
import pandas as pd
import os
import yagmail

# --- Your email credentials ---
SENDER_EMAIL = "likhithavandana06@gmail.com"
SENDER_PASSWORD = "mejxeswpxhfsqmbm"  # App Password (16 chars)

# --- Files ---
EXCEL_FILE = "student_details.xlsx"     # Excel file: Name, Roll, Dept, Email
OUTPUT_FOLDER = "certificates"          
BACKGROUND_IMAGE = "certificate_template.png"  # Background template image

# Create folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Read participant details
df = pd.read_excel(EXCEL_FILE)
print("Columns in Excel:", df.columns.tolist())

# Email client
yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)

# --- Certificate Generator Class ---
class Certificate(FPDF):
    def header(self):
        if BACKGROUND_IMAGE:
            self.image(BACKGROUND_IMAGE, 0, 0, 210, 297)

    def footer(self):
        pass

# --- Loop through participants ---
for index, row in df.iterrows():
    # Only these 3 columns are used for the certificate
    name = row['Name']
    roll = row['Roll']
    dept = row['Department']
    email = row['Email']  # only used to send email, not on certificate

    pdf = Certificate("P", "mm", "A4")
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 28)
    pdf.set_text_color(0, 51, 102)
    pdf.ln(60)
    pdf.cell(0, 20, "Certificate of Participation", ln=True, align='C')

    # Body text
    pdf.set_font("Arial", '', 16)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    pdf.cell(0, 10, "This is to certify that", ln=True, align='C')

    # Name
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(0, 15, name, ln=True, align='C')

    # Roll Number & Department
    pdf.set_font("Arial", '', 14)
    pdf.cell(0, 10, f"Roll Number: {roll}", ln=True, align='C')
    pdf.cell(0, 10, f"Department: {dept}", ln=True, align='C')

    pdf.ln(10)
    pdf.cell(0, 10, "has actively participated in the Hackathon event.", ln=True, align='C')

    # Save certificate
    filename = os.path.join(OUTPUT_FOLDER, f"{name}_certificate.pdf")
    pdf.output(filename)

    # Send email (certificate attached, but email not printed on certificate)
    subject = "Your Hackathon Certificate"
    body = f"Dear {name},\n\nCongratulations on participating in the Hackathon! Please find your certificate attached.\n\nBest regards,\nTeam GCC"
    try:
        yag.send(to=email, subject=subject, contents=body, attachments=filename)
        print(f"✅ Sent certificate to {name} at {email}")
    except Exception as e:
        print(f"❌ Failed to send email to {name}: {e}")

print("🎉 All certificates created & sent successfully!")
