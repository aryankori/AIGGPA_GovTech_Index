import re
import os

filepath = "concept_proposal_final_v3.tex"

academic_content = r"""\documentclass[11pt,a4paper]{article}

% ── FONTS (Academic Rigor) ──────────────────────────────────
\usepackage{fontspec}
\setmainfont{Times New Roman}
\newfontfamily{\hindifont}{Nirmala UI}[Script=Devanagari]
\newcommand{\hindi}[1]{{\hindifont #1}}

% ── LAYOUT ───────────────────────────────────────────────────
\usepackage[top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm]{geometry}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{shadows,calc,shapes.geometric,arrows.meta,positioning,fit,backgrounds,patterns,decorations.pathmorphing}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{colortbl}
\usepackage{booktabs}
\usepackage{tabularx}
\newcolumntype{C}{>{\centering\arraybackslash}X}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\usepackage{enumitem}
\usepackage{setspace}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{hanging}
\usepackage{multicol}
\usepackage{hyperref}
\usepackage{microtype}
\usepackage{array}
\usepackage{caption}

\hypersetup{colorlinks=false,hidelinks}

% ── AIGGPA + EARTHEN PALETTE ─────────────────────────────────
\definecolor{aiggpablue}{HTML}{002E5D}
\definecolor{aiggpagold}{HTML}{D4AF37}
\definecolor{slate}{HTML}{2E3133}
\definecolor{sage}{HTML}{76933C}
\definecolor{sand}{HTML}{FDFCF8}
\definecolor{stone}{HTML}{E5E7EB}

% ── ACADEMIC HEADERS ──────────────────────────────────────────
\newcommand{\techsection}[1]{%
  \vspace{0.8cm}\noindent
  {\fontsize{14}{17}\selectfont\bfseries\color{aiggpablue}\MakeUppercase{#1}}%
  \\[-0.15cm]{\color{aiggpagold}\rule{\textwidth}{1.5pt}}\vspace{0.4cm}%
}

\titleformat{\section}[block]{\normalfont}{}{0em}{\techsection}
\titlespacing*{\section}{0pt}{15pt}{10pt}

\titleformat{\subsection}[block]
  {\normalfont\bfseries\fontsize{12}{14}\selectfont\color{slate}}
  {}{0em}{}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}

% ── HEADER / FOOTER ──────────────────────────────────────────
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\footnotesize\color{slate}\textbf{AIGGPA Bhopal} \quad\textbar\quad IT Assessment Proposal}
\fancyhead[R]{\footnotesize\color{slate}\thepage}
\fancyfoot[C]{\tiny\color{slate} INSTITUTIONAL RESEARCH PROPOSAL // APRIL 2026 // MP GOV}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\headrule}{\color{aiggpagold}\hrule width\headwidth height 0.5pt}

% ── INSTITUTIONAL BOXES ──────────────────────────────────────
\newtcolorbox{academicbox}[1]{
  colback=white, colframe=aiggpablue, boxrule=0.8pt, arc=0mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable,
  fonttitle=\bfseries\color{white}, title=#1, colbacktitle=aiggpablue}

\newtcolorbox{sagebox}{
  colback=sage!5, colframe=sage, boxrule=0.8pt, arc=0mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable}

\newtcolorbox{goldbox}{
  colback=aiggpagold!5, colframe=aiggpagold, boxrule=0.8pt, arc=0mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable}

% ── GLOBAL STYLING ───────────────────────────────────────────
\color{slate}
\pagecolor{sand}

\begin{document}
\onehalfspacing

% ═════════════════════════════════════════════════════════════
%  COVER PAGE (NATIVE TOPOGRAPHIC TIKZ)
% ═════════════════════════════════════════════════════════════
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  \fill[sand] (current page.south west) rectangle (current page.north east);
  
  % Native Topographic Pattern
  \begin{scope}[opacity=0.15]
    \foreach \i in {1,...,12} {
      \draw[aiggpablue, ultra thick, decoration={random steps, segment length=10mm, amplitude=15mm}, decorate] 
        ($(current page.south west)+(-5cm,\i*2cm)$) -- ($(current page.north east)+(5cm,\i*2cm-5cm)$);
    }
    \foreach \j in {1,...,8} {
      \draw[aiggpagold, thick, decoration={random steps, segment length=15mm, amplitude=25mm}, decorate] 
        ($(current page.south east)+(5cm,\j*3cm)$) -- ($(current page.north west)+(-5cm,\j*3cm-8cm)$);
    }
  \end{scope}
  
  % Framing
  \draw[aiggpablue, line width=2pt] ($(current page.south west)+(1.5cm,1.5cm)$) rectangle ($(current page.north east)-(1.5cm,1.5cm)$);
  \draw[aiggpagold, line width=0.5pt] ($(current page.south west)+(1.35cm,1.35cm)$) rectangle ($(current page.north east)-(1.35cm,1.35cm)$);
\end{tikzpicture}

\vspace*{3.5cm}
\begin{center}
  \begin{minipage}{0.85\textwidth}
    \centering
    \fontsize{10}{12}\selectfont\color{slate}\textbf{INSTITUTIONAL RESEARCH PROPOSAL}\\[1.5em]
    \fontsize{28}{34}\selectfont\bfseries\color{aiggpablue}
    Assessment of IT Tool Utilisation\\
    Among Government Officials\\[0.8em]
    \fontsize{14}{18}\selectfont\color{slate}
    \hindi{सरकारी अधिकारियों द्वारा आईटी उपकरणों के उपयोग का आकलन}
  \end{minipage}
\end{center}

\vfill

\begin{center}
  \begin{minipage}{12cm}
    \centering\small\color{slate}
    \begin{tabular}{c}
      \textbf{Investigator:} Aryan Kori \\[4pt]
      \textbf{Institutional Body:} AIGGPA, Bhopal \\[4pt]
      \textbf{Departments:} School Education \textbullet{} Health \textbullet{} Forest \\[4pt]
      \textbf{Date:} April 2026 \\
    \end{tabular}
  \end{minipage}
\end{center}
\vspace{1.5cm}

\newpage
\pagenumbering{arabic}

% ═════════════════════════════════════════════════════════════
%  CONTENT
% ═════════════════════════════════════════════════════════════

\section{Background}

\vspace{0.2cm}
The Government of Madhya Pradesh, architected primarily by technical agencies such as MAP-IT and NIC, has built an impressive portfolio of digital platforms across its key departments. These include Education Portal 3.0, NHM CHETNA, and AI-enabled forest monitoring systems.

Despite the sophistication of these platforms, institutional observation reveals that day-to-day workflows at the district and block level still run on physical registers and informal digital tools. The lack of institutionalised usage norms and inadequate front-line computing training are common barriers to IT tools in public administration (Bhatnagar, 2004). Often, failures in IT adoption originate from a \textit{design-reality gap} (Heeks, 2003). 

% ═════════════════════════════════════════════════════════════
\section{Rationale}

\vspace{0.2cm}
Maximizing the adoption of IT tools translates directly to productivity gains and structural resilience. Current public sector agencies globally face significant hurdles due to aging infrastructure. As reported by the GAO (2019), up to 80\% of IT budgets are consumed entirely by maintenance of legacy systems.

\vspace{0.4cm}
\begin{center}
\begin{tikzpicture}[background rectangle/.style={draw=stone, fill=white, thick}, framed]
  \begin{axis}[
    xbar stacked,
    width=10.5cm, height=4cm, xmin=0, xmax=100,
    ytick=\empty, axis x line=bottom, axis y line=none,
    enlarge y limits=0.5, bar width=16pt,
    xtick={0, 20, 40, 60, 80, 100},
    xticklabel={\pgfmathprintnumber{\tick}\%},
    grid=major, grid style={dotted, slate!40},
    legend style={at={(0.5,-0.38)}, anchor=north, draw=none, fill=none, font=\footnotesize, legend columns=-1},
    axis line style={aiggpablue, thick},
    title={\textbf{IT Budget Allocation: Maintenance vs. Modernisation}},
    title style={font=\small\bfseries, yshift=1ex}
  ]
  \addplot [fill=aiggpablue, draw=none] coordinates {(80,0)};
  \addplot [fill=aiggpagold, draw=none] coordinates {(20,0)};
  \legend{Maintenance (80\%), Modernisation (20\%)}
  \end{axis}
\end{tikzpicture}
\end{center}

% ═════════════════════════════════════════════════════════════
\section{Theoretical Framework}

This study employs the \textbf{Unified Theory of Acceptance and Use of Technology (UTAUT)} (Venkatesh et al., 2003) to map bureaucratic and individual barriers. Every data point collected will be coded against UTAUT dimensions to inform training designs.

\vspace{0.5cm}

\begin{center}
\begin{tikzpicture}[
  node distance=0.8cm and 1.2cm,
  box/.style={rectangle, minimum width=3.1cm, minimum height=1cm, 
    align=center, font=\footnotesize\bfseries\color{white}, 
    fill=aiggpablue, draw=aiggpablue!80!black, thick, drop shadow},
  gold_box/.style={box, fill=aiggpagold, draw=aiggpagold!80!black},
  arrow/.style={-{Stealth[length=5pt]}, ultra thick, color=aiggpablue!60, rounded corners=6pt}
]
  \node[box] (pe) {PERFORMANCE (PE/EE)};
  \node[gold_box, left=of pe] (input) {OFFICIAL};
  \node[box, below=of pe] (si) {SOCIAL INFLU. (SI)};
  \node[box, below=of si] (fc) {CONDITIONS (FC)};
  \node[gold_box, right=of si] (out) {AIGGPA\\MODULE};

  \draw[arrow] (input) |- (pe);
  \draw[arrow] (input) -- (si);
  \draw[arrow] (input) |- (fc);
  \draw[arrow] (pe) -| (out);
  \draw[arrow] (si) -- (out);
  \draw[arrow] (fc) -| (out);
\end{tikzpicture}
\end{center}

% ═════════════════════════════════════════════════════════════
\section{Scope}

\begin{academicbox}{PROPOSAL SCOPE}
\renewcommand{\arraystretch}{1.5}
\noindent\begin{tabularx}{\linewidth}{@{} >{\bfseries\color{aiggpablue}\small}p{3.2cm} >{\small}X @{}}
Departments & School Education \textbullet{} Health \textbullet{} Forest \\[0.1cm]
Respondents & Class I, II \& III Officials; IT nodal staff \\[0.1cm]
Office Level & State Secretariat (Bhopal) and Territorial Units \\[0.1cm]
Duration & April to June 2026 (10 Weeks) \\
\end{tabularx}
\end{academicbox}

% ═════════════════════════════════════════════════════════════
\section{Methodology}

The study uses a mixed-methods design. Quantitative statistical counts are triangulated with qualitative thematic coding (Stream A/B methodology).

\vspace{0.3cm}
\begin{multicols}{2}
\begin{sagebox}
\small\textbf{Stream A: Officials}
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
  \item Daily task mapping
  \item Barrier identification
  \item Training history
\end{itemize}
\end{sagebox}

\columnbreak

\begin{goldbox}
\small\textbf{Stream B: IT Systems}
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
  \item Platform inventory
  \item Usage statistics audit
  \item Support structure
\end{itemize}
\end{goldbox}
\end{multicols}

\subsection{Sampling Strategy}

\vspace{0.4cm}
\begin{academicbox}{Sampling Strategy}
\noindent\begin{tabularx}{\linewidth}{L{3.5cm} C C C C}
\rowcolor{aiggpablue}
\textbf{\color{white}Profile} & \textbf{\color{white}Edu.} & \textbf{\color{white}Health} & \textbf{\color{white}Forest} & \textbf{\color{white}Total} \\
\rowcolor{white}
Approvers & 4 & 4 & 4 & \textbf{12} \\
\rowcolor{stone!30}
Data Creators & 5 & 5 & 5 & \textbf{15} \\
\rowcolor{white}
Field Users & 6 & 6 & 6 & \textbf{18} \\
\rowcolor{stone!30}
IT Support & 3 & 3 & 3 & \textbf{9} \\
\rowcolor{aiggpagold!20}
\textbf{SUBTOTAL} & \textbf{18} & \textbf{18} & \textbf{18} & \textbf{54} \\
\end{tabularx}
\end{academicbox}

% ═════════════════════════════════════════════════════════════
\section{Data Analysis \& Matrix}

Transcripts will be coded in ATLAS.ti to construct the \textbf{UTAUT Gap Analysis Matrices}.

\vspace{0.6cm}
\begin{academicbox}{Matrix A: Secretariat Workflow Analysis}
\noindent\begin{tabularx}{\linewidth}{l C C C C}
\rowcolor{aiggpablue}
\textbf{\color{white}Department} & \textbf{\color{white}PE} & \textbf{\color{white}EE} & \textbf{\color{white}SI} & \textbf{\color{white}FC} \\
\rowcolor{white}
School Education & & & & \\
\rowcolor{stone!30}
Health & & & & \\
\rowcolor{white}
Forest & & & & \\
\end{tabularx}
\end{academicbox}

% ═════════════════════════════════════════════════════════════
\section{Work Plan}

\vspace{0.2cm}
\renewcommand{\arraystretch}{1.8}
\begin{academicbox}{Phased Work Plan}
\noindent\begin{tabularx}{\linewidth}{L{2.2cm} L{4cm} X}
\rowcolor{aiggpablue}
\textbf{\color{white}Phase} & \textbf{\color{white}Activity} & \textbf{\color{white}Milestone} \\
\rowcolor{white}
Week 1-3 & Literature \& Design & Signed Proposal \\
\rowcolor{stone!30}
Week 4-8 & Field Operations & 54 Case Studies \\
\rowcolor{white}
Week 9-10 & Synthesis \& Writing & Final Report \\
\end{tabularx}
\end{academicbox}

% ═════════════════════════════════════════════════════════════
\section{References}

\small
Alrawabdeh, W. (2014). \textit{International Journal of Business and Social Science}, 5(8). \\
Bhatnagar, S. (2004). \textit{E-Government: From Vision to Implementation}. Sage. \\
Heeks, R. (2003). \textit{Most eGovernment-for-Development Projects Fail}. Manchester. \\
Venkatesh, V., et al. (2003). \textit{User Acceptance of IT: Toward a Unified View}. MIS Quarterly.

\end{document}
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(academic_content)
