import zipfile
import xml.etree.ElementTree as ET

def extract_docx(path):
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = ET.XML(xml_content)
    
    paragraphs = []
    for paragraph in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        texts = [node.text
                 for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))
            
    return paragraphs

paras = extract_docx(r"c:\Users\aryan\Downloads\AIGGPA_Fieldwork_Questionnaire_Bilingual.docx")
with open("temp_docx_dump.txt", "w", encoding="utf-8") as f:
    for p in paras:
        f.write(p + "\n")
print("Dump created.")
