import re

filepath = "concept_proposal_final_v3.tex"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Remove hard page breaks per section
text = text.replace(r"\newcommand{\sectionbreak}{\clearpage}", "")
text = text.replace(r"\newcommand{\sectionbreak}{\clearpage}" + "\n", "")

# 2. Update \techsection for richer spacing/alignment
new_techsection = r"""\newcommand{\techsection}[1]{%
  \vspace{0.8cm}\noindent
  {\fontsize{15}{18}\selectfont\bfseries\color{graphite}\MakeUppercase{#1}}%
  \\[-0.2cm]\rule{\textwidth}{1.5pt}\vspace{0.4cm}%
}"""
text = re.sub(r"\\newcommand\{\\techsection\}\[1\]\{.*?\}", lambda m: new_techsection, text, flags=re.DOTALL)

# 3. Update PGFPlots chart to be "Rich"
rich_axis_options = r"""\begin{axis}[
    xbar stacked,
    width=12cm,
    height=4cm,
    xmin=0, xmax=100,
    ytick=\empty,
    axis x line=bottom,
    axis y line=none,
    enlarge y limits=0.5,
    bar width=16pt,
    tick align=outside,
    xtick={0, 20, 40, 60, 80, 100},
    xticklabel={\pgfmathprintnumber{\tick}\%},
    grid=major,
    grid style={dashed, gray!30},
    legend style={at={(0.5,-0.35)}, anchor=north, draw=none, fill=none, font=\footnotesize, legend columns=-1},
    axis line style={graphite, very thick},
    title={\textbf{Public Sector IT Budget Allocation Estimates (GAO, 2019)}},
    title style={font=\small\bfseries\color{graphite}, yshift=0ex}
  ]"""
text = re.sub(r"\\begin\{axis\}\[.*?xbar stacked.*?\]", lambda m: rich_axis_options, text, flags=re.DOTALL)

# 4. Update UTAUT flowchart with shadows and solid fills
if "{shadows}" not in text:
    text = text.replace(r"\usetikzlibrary{calc", r"\usetikzlibrary{shadows,calc")

# Define the new styles for the flowchart
new_tikz_style = r"""\begin{tikzpicture}[
  node distance=0.8cm and 1.2cm,
  box/.style={rectangle, minimum width=3cm, minimum height=0.8cm, 
    align=center, font=\scriptsize\bfseries\color{white}, 
    fill=graphite, draw=darkgray, thick, drop shadow},
  indigo_box/.style={box, fill=indigo, draw=indigo!80!black},
  cyan_box/.style={box, fill=cyan, draw=cyan!80!black},
  arrow/.style={-{Stealth[length=5pt]}, ultra thick, color=graphite!70, rounded corners=6pt}
]
  \node[cyan_box] (pe) {PERFORMANCE (PE/EE)};
  \node[indigo_box, left=of pe] (input) {OFFICIAL};
  \node[indigo_box, below=of pe] (si) {SOCIAL INFL. (SI)};
  \node[indigo_box, below=of si] (fc) {CONDITIONS (FC)};
  \node[cyan_box, right=of si] (out) {AIGGPA\\iGOT MODULE};"""

# Replace the specific block in the UTAUT flowchart
# We look for the start of the tikzpicture that contains the UTAUT boxes
text = re.sub(r"\\begin\{tikzpicture\}\[\s*node distance=0.8cm and 1.2cm,.*?input.*?\)\s*\{OFFICIAL\};", lambda m: new_tikz_style, text, flags=re.DOTALL)

# Since the previous step might have left some old nodes or changed things, let's just make sure the rest of the flow is correct.
# The nodes were already replaced partially or I should replace them explicitly if they aren't covered by the block.

# After the block, the draw commands should stay as is.
# Ensure the nodes inside are correctly styled.
text = text.replace(r"\node[box] (pe)", r"\node[cyan_box] (pe)")
text = text.replace(r"\node[box,draw=indigo,text=indigo,left=of pe] (input) {OFFICIAL};", "") # Handled by block
text = text.replace(r"\node[box] (si)", r"\node[indigo_box] (si)")
text = text.replace(r"\node[box] (fc)", r"\node[indigo_box] (fc)")
text = text.replace(r"\node[box,draw=cyan,text=cyan,right=of si] (out) {AIGGPA\\iGOT MODULE};", r"\node[cyan_box, right=of si] (out) {AIGGPA\\iGOT MODULE};")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
