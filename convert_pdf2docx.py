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
    docx_path = os.path.join(downloads_dir, pdf_file.replace('.pdf', '.docx'))
    
    if os.path.exists(pdf_path):
        print(f"Converting {pdf_file}...")
        try:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
            print(f"Success: {docx_path}")
        except Exception as e:
            print(f"Failed to convert {pdf_file}: {str(e)}")
    else:
        print(f"Could not find {pdf_path}")
