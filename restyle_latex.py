import re

filepath = "concept_proposal_final_v3.tex"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Global Variable Renaming
text = text.replace("{navyblue}", "{graphite}")
text = text.replace("[navyblue]", "[graphite]")
text = text.replace("color{navyblue}", "color{graphite}")
text = text.replace("color=navyblue", "color=graphite")

text = text.replace("{gold}", "{indigo}")
text = text.replace("[gold]", "[indigo]")
text = text.replace("color{gold}", "color{indigo}")
text = text.replace("color=indigo", "color=indigo")

text = text.replace("{gold!", "{indigo!")
text = text.replace("[gold!", "[indigo!")
text = text.replace("color{gold!", "color{indigo!")
text = text.replace("color=gold!", "color=indigo!")

text = text.replace("{accentteal", "{cyan")
text = text.replace("[accentteal", "[cyan")
text = text.replace("color{accentteal", "color{cyan")
text = text.replace("color=accentteal", "color=cyan")

text = text.replace("navybox", "graphitebox")
text = text.replace("goldbox", "indigobox")

# 2. Complete Header Block Replacements
color_block_pattern = re.compile(r"% ── BRAND COLORS ─────────────────────────────────────────────.*?% ── SECTION HEADING ──────────────────────────────────────────", re.DOTALL)
new_color_block = r"""% ── BRAND COLORS ─────────────────────────────────────────────
\definecolor{graphite}{HTML}{1A1B26}
\definecolor{indigo}{HTML}{4F46E5}
\definecolor{lightgray}{HTML}{F8FAFC}
\definecolor{midgray}{HTML}{CBD5E1}
\definecolor{darkgray}{HTML}{334155}
\definecolor{cyan}{HTML}{06B6D4}
\definecolor{sectionbg}{HTML}{F1F5F9}
\definecolor{softgreen}{HTML}{F0FDF4}
\definecolor{darkgreen}{HTML}{166534}

% ── SECTION HEADING ──────────────────────────────────────────"""
text = color_block_pattern.sub(lambda _: new_color_block, text)

section_block_pattern = re.compile(r"% ── SECTION HEADING ──────────────────────────────────────────.*?% ── HEADER / FOOTER ──────────────────────────────────────────", re.DOTALL)
new_section_block = r"""% ── SECTION HEADING ──────────────────────────────────────────
\newcommand{\techsection}[1]{%
  \vspace{0.4cm}\noindent
  {\fontsize{14}{16}\selectfont\bfseries\color{graphite}\MakeUppercase{#1}}%
  \vspace{2pt}\hrule height 1.2pt width \textwidth\vspace{0.2cm}%
}

\titleformat{\section}[block]{\normalfont}{}{0em}{\techsection}
\titlespacing*{\section}{0pt}{10pt}{8pt}

\titleformat{\subsection}[block]
  {\normalfont\bfseries\fontsize{11}{13}\selectfont\color{indigo}}
  {}{0em}{}
\titlespacing*{\subsection}{0pt}{8pt}{2pt}

% ── HEADER / FOOTER ──────────────────────────────────────────"""
text = section_block_pattern.sub(lambda _: new_section_block, text)

custom_box_pattern = re.compile(r"% ── CUSTOM BOXES ─────────────────────────────────────────────.*?% ── LISTS ────────────────────────────────────────────────────", re.DOTALL)
new_custom_boxes = r"""% ── CUSTOM BOXES ─────────────────────────────────────────────
\newtcolorbox{indigobox}{
  colback=indigo!5, colframe=indigo, boxrule=0.8pt, arc=0mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable}

\newtcolorbox{graphitebox}{
  colback=sectionbg,colframe=graphite,boxrule=0.8pt,arc=0mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable}

\newtcolorbox{greenbox}{
  colback=softgreen,colframe=darkgreen,boxrule=0.8pt,arc=0mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable}

\newtcolorbox{streamboxa}{
  colback=lightgray,colframe=cyan,boxrule=1.2pt,arc=0mm,
  lefttitle=10pt,toptitle=6pt,bottomtitle=6pt,
  left=10pt,right=10pt,top=8pt,bottom=8pt,
  title={\bfseries\fontsize{9.5}{11}\selectfont\color{white}Stream A \textbullet{} Department Officials},
  colbacktitle=cyan,breakable}

\newtcolorbox{streamboxb}{
  colback=lightgray,colframe=graphite,boxrule=1.2pt,arc=0mm,
  lefttitle=10pt,toptitle=6pt,bottomtitle=6pt,
  left=10pt,right=10pt,top=8pt,bottom=8pt,
  title={\bfseries\fontsize{9.5}{11}\selectfont\color{white}Stream B \textbullet{} IT Department},
  colbacktitle=graphite,breakable}

% ── LISTS ────────────────────────────────────────────────────"""
text = custom_box_pattern.sub(lambda _: new_custom_boxes, text)

cover_page_pattern = re.compile(r"% ═════════════════════════════════════════════════════════════\n%  COVER PAGE\n% ═════════════════════════════════════════════════════════════.*?\\newpage", re.DOTALL)
new_cover_page = r"""% ═════════════════════════════════════════════════════════════
%  COVER PAGE
% ═════════════════════════════════════════════════════════════
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  % Tech minimalist background
  \fill[white] (current page.south west) rectangle (current page.north east);
  
  % Left vertical accent bar
  \fill[graphite] (current page.north west) rectangle ($(current page.south west)+(3.5cm,0)$);
  
  % Thin geometric slash lines
  \draw[indigo, line width=4pt] ($(current page.north west)+(6cm,0)$) -- ($(current page.south east)-(0,8cm)$);
  \draw[cyan, line width=1.5pt] ($(current page.north west)+(6.5cm,0)$) -- ($(current page.south east)-(0,7cm)$);
\end{tikzpicture}

\vspace*{5cm}
\begin{flushleft}
  \hspace{2cm}
  \begin{minipage}{0.75\textwidth}
  \fontsize{10.5}{12}\selectfont\color{indigo}\textbf{INSTITUTIONAL RESEARCH PROPOSAL}\\[1em]
  \fontsize{32}{38}\selectfont\bfseries\color{graphite}
  Assessment of IT Tool\\[0.15em]
  Utilisation Among\\[0.15em]
  Government Officials\\[1.2em]
  \fontsize{13}{16}\selectfont\color{darkgray}
  \hindi{सरकारी अधिकारियों द्वारा आईटी उपकरणों के उपयोग का आकलन}
  \end{minipage}
\end{flushleft}

\vspace*{7cm}
\begin{flushleft}
  \hspace{2cm}
  \begin{minipage}{10cm}
    \footnotesize\color{graphite}
    \begin{tabular}{@{}ll@{}}
      \textbf{Investigator:} & Aryan Kori \\[5pt]
      \textbf{Institution:}  & AIGGPA, Bhopal \\[5pt]
      \textbf{Departments:}  & School Education \textbullet{} Health \textbullet{} Forest, Govt.\ of MP \\[5pt]
      \textbf{Date:}         & April 2026 \\
    \end{tabular}
  \end{minipage}
\end{flushleft}

\newpage"""
text = cover_page_pattern.sub(lambda _: new_cover_page, text)

# Lastly fix the footer lines that use \color{gold}/\color{navyblue} without bracket
text = text.replace(r"\renewcommand{\headrule}{\color{graphite}\hrule width\headwidth height\headrulewidth}", r"\renewcommand{\headrule}{\color{graphite}\hrule width\headwidth height 1pt}")
text = text.replace(r"\renewcommand{\footrule}{\color{indigo}\hrule width\headwidth height 1.5pt}", r"\renewcommand{\footrule}{\color{graphite}\hrule width\headwidth height 0.5pt}")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
