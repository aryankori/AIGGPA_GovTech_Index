from pdf2docx import Converter
import os

files = [
    "AIGGPA_Printable_Schedule.pdf",
    "Schedule_Revenue.pdf",
    "Schedule_Rural_Development.pdf",
    "Schedule_Forest.pdf",
    "Schedule_Health.pdf"
]

downloads_dir = r"c:\Users\aryan\Downloads"

for pdf_file in files:
    pdf_path = os.path.join(downloads_dir, pdf_file)
    # Write to _v2 first, then we can rename
    docx_name = pdf_file.replace('.pdf', '_v2.docx')
    docx_path = os.path.join(downloads_dir, docx_name)
    
    if os.path.exists(pdf_path):
        print(f"Converting {pdf_file}...")
        try:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
            print(f"  Success: {docx_name}")
        except Exception as e:
            print(f"  Failed: {str(e)}")
    else:
        print(f"  Not found: {pdf_path}")

print("\nDone! Close the old .docx files in Word, then rename _v2 files to replace them.")
