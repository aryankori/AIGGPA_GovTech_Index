import re

filepath = "concept_proposal_final_v3.tex"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Section Isolation (Page break per heading)
if r"\newcommand{\sectionbreak}{\clearpage}" not in text:
    text = text.replace(r"\titleformat{\section}[block]{\normalfont}{}{0em}{\techsection}", 
                        r"\newcommand{\sectionbreak}{\clearpage}" + "\n" + r"\titleformat{\section}[block]{\normalfont}{}{0em}{\techsection}")

# 2. Em-Dashes fix
text = text.replace("Week 1--2", "Week 1 to 2")
text = text.replace("Week 4--5", "Week 4 to 5")
text = text.replace("Week 6--7", "Week 6 to 7")

# 3. Graphic Bordering (PGFPlots)
if r"\begin{tikzpicture}[framed" not in text:
    text = text.replace(r"\begin{tikzpicture}" + "\n" + r"  \begin{axis}[", 
                        r"\begin{tikzpicture}[framed, background rectangle/.style={draw=midgray, rounded corners=3pt, fill=lightsec, thick}]" + "\n" + r"  \begin{axis}[")

# 4. UTAUT Router Smoothing
text = text.replace(r"arrow/.style={-{Stealth[length=4pt]},thick,color=slate}",
                    r"arrow/.style={-{Stealth[length=4pt]},thick,color=slate,rounded corners=4pt}")

# 5. Scope Fix
scope_pattern = re.compile(r"\\begin{tabularx}{\\textwidth}.*?\\end{tabularx}", re.DOTALL)
# Search specifically after the "Scope" section text
scope_header_pos = text.find(r"\section{Scope}")
if scope_header_pos != -1:
    scope_search_space = text[scope_header_pos:]
    match = scope_pattern.search(scope_search_space)
    if match:
        old_scope = match.group(0)
        new_scope = r"""\begin{graphitebox}
\vspace{0.1cm}
\begin{tabularx}{\textwidth}{@{} >{\bfseries\color{graphite}\small}p{3.2cm} >{\small}X @{}}
Departments & School Education \textbullet{} Health \textbullet{} Forest (Government of Madhya Pradesh) \\[0.1cm]
\hline \rule{0pt}{3ex}%
Respondents & Department officials (Class I, II \& III cadres) and IT cell / IT department staff \\[0.1cm]
\hline \rule{0pt}{3ex}%
Office Level & State-level Secretariat offices in Bhopal; selected district \& sub-district territorial offices \\[0.1cm]
\hline \rule{0pt}{3ex}%
Duration & April to June 2026 (approximately 10 weeks) \\[0.1cm]
\hline \rule{0pt}{3ex}%
Exclusions & Private contractors; citizen-facing front-end users \\[0.1cm]
\hline \rule{0pt}{3ex}%
Output & Gap analysis report and a set of prioritised recommendations for AIGGPA \\
\end{tabularx}
\vspace{0.1cm}
\end{graphitebox}"""
        text = text[:scope_header_pos] + scope_search_space.replace(old_scope, new_scope, 1)

# 6. Cover Page Appeal Upgrade
cover_page_pattern = re.compile(r"% ═════════════════════════════════════════════════════════════\n%  COVER PAGE\n% ═════════════════════════════════════════════════════════════.*?\\newpage", re.DOTALL)
new_cover_page = r"""% ═════════════════════════════════════════════════════════════
%  COVER PAGE
% ═════════════════════════════════════════════════════════════
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  % Subtle grid background
  \draw[step=1cm,gray!15,very thin] (current page.south west) grid (current page.north east);
  
  % Perimeter border frame
  \draw[thick, graphite] ($(current page.south west)+(1cm,1cm)$) rectangle ($(current page.north east)-(1cm,1cm)$);
  
  % Left vertical accent bar
  \fill[graphite] (current page.north west) rectangle ($(current page.south west)+(3.5cm,0)$);
  
  % Thin geometric slash lines
  \draw[indigo, line width=4pt] ($(current page.north west)+(6cm,0)$) -- ($(current page.south east)-(0,8cm)$);
  \draw[cyan, line width=1.5pt] ($(current page.north west)+(6.5cm,0)$) -- ($(current page.south east)-(0,7cm)$);
\end{tikzpicture}

\vspace*{4.5cm}
\begin{flushleft}
  \hspace{2cm}
  \begin{minipage}{0.75\textwidth}
  \fontsize{10.5}{12}\selectfont\color{indigo}\textbf{INSTITUTIONAL RESEARCH PROPOSAL}\\[1em]
  \fontsize{34}{40}\selectfont\bfseries\color{graphite}
  Assessment of IT Tool\\[0.15em]
  Utilisation Among\\[0.15em]
  Government Officials\\[1.5em]
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
      \textbf{Investigator:} & Aryan Kori \\[6pt]
      \textbf{Institution:}  & AIGGPA, Bhopal \\[6pt]
      \textbf{Departments:}  & School Education \textbullet{} Health \textbullet{} Forest, Govt.\ of MP \\[6pt]
      \textbf{Date:}         & April 2026 \\
    \end{tabular}
  \end{minipage}
\end{flushleft}

\newpage"""
text = cover_page_pattern.sub(lambda _: new_cover_page, text)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
