import openpyxl
wb = openpyxl.load_workbook(r"c:\Users\aryan\Downloads\Framework for Interns.xlsx")
ws = wb["Sheet1"]

for r in range(8, 14):
    cell = ws.cell(row=r, column=2)  # column B which always had fill
    f = cell.fill
    print(f"Row {r} B: rgb={getattr(f.fgColor, 'rgb', 'N')}, theme={getattr(f.fgColor, 'theme', 'N')}, tint={getattr(f.fgColor, 'tint', 'N')}, type={getattr(f.fgColor, 'type', 'N')}, pattern={f.patternType}")
