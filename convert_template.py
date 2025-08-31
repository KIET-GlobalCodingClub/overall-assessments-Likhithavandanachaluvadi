from pdf2image import convert_from_path

# Path to your PDF template
pdf_path = "certificate_template.pdf"

# Convert first page to image
pages = convert_from_path(pdf_path, dpi=300)

# Save the first page as a JPG
pages[0].save("certificate_template.jpg", "JPEG")

print("Template converted and saved as certificate_template.jpg")
