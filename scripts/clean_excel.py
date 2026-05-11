import openpyxl
import re

def clean_text(text):
    if not isinstance(text, str):
        return text
    
    # Remove em dash and replace with regular hyphen
    text = text.replace('—', '-')
    text = text.replace('–', '-') # also en dash
    
    # Simple humanizer replacements for common AI words
    replacements = {
        "delve into": "explore",
        "leverage": "use",
        "facilitate": "help",
        "Moreover": "",
        "Furthermore": "",
        "In conclusion": "",
        "tapestry": "structure",
        "testament": "proof",
        "pivotal": "important",
        "seamless": "smooth",
        "robust": "strong",
        "dynamic": "active",
        "comprehensive": "full",
        "multifaceted": "varied",
        "transformative": "big",
        "not only": "not just",
        "but also": "but"
    }
    
    for key, value in replacements.items():
        # Case insensitive replacement for words
        text = re.sub(r'\b' + re.escape(key) + r'\b', value, text, flags=re.IGNORECASE)
        
    return text

def clean_excel():
    path = r"C:\Users\aryan\Downloads\Framework_for_Interns_updated.xlsx"
    try:
        wb = openpyxl.load_workbook(path)
        for sheet in wb.worksheets:
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value:
                        cell.value = clean_text(cell.value)
        wb.save(path)
        print("Successfully cleaned the excel file.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_excel()
