import fitz

BAD_WORDS = ['staff', 'workers', 'worker']
EM = chr(8212)
EN = chr(8211)

issues = []

for label, path in [
    ('PROPOSAL', r'c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\Final_Proposal_Formatted.pdf'),
    ('CHARTS', r'c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\Charts_Data_Appendix.pdf'),
    ('PITCH', r'c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\Pitch_Guide.pdf'),
    ('METHODOLOGY', r'c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\Methodology_Scope_Options.pdf'),
]:
    doc = fitz.open(path)
    for i, page in enumerate(doc, 1):
        text = page.get_text()
        words = text.lower().split()
        for bw in BAD_WORDS:
            if bw in words:
                for line in text.split('\n'):
                    if bw in line.lower().split():
                        snippet = line.strip()
                        if len(snippet) > 90:
                            snippet = snippet[:90] + '...'
                        issues.append(f'  {label} p{i}: "{snippet}"')
        if EM in text:
            issues.append(f'  {label} p{i}: EM DASH FOUND')
        if EN in text:
            issues.append(f'  {label} p{i}: EN DASH FOUND')
    doc.close()

if issues:
    print('ISSUES FOUND:')
    for iss in issues:
        print(iss)
else:
    print('ALL CLEAR - No staff/workers/em-dashes/en-dashes in either PDF')
