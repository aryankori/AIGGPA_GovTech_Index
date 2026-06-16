from pdf2docx import Converter
import os

pdf_files = [
    r"C:\Users\aryan\Downloads\Schedule_Revenue.pdf",
    r"C:\Users\aryan\Downloads\Schedule_Rural_Development.pdf",
    r"C:\Users\aryan\Downloads\Schedule_Forest.pdf",
    r"C:\Users\aryan\Downloads\Schedule_Health.pdf",
    r"C:\Users\aryan\Downloads\AIGGPA_Printable_Schedule.pdf"
]

print("Starting PDF to DOCX conversion...")

for pdf in pdf_files:
    if os.path.exists(pdf):
        docx_path = pdf.replace(".pdf", ".docx")
        print(f"Converting {pdf} -> {docx_path}")
        cv = Converter(pdf)
        cv.convert(docx_path)
        cv.close()
        print(f"Done: {docx_path}")
    else:
        print(f"File not found: {pdf}")

print("\nAll conversions finished!")
