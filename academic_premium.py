import re
import os

filepath = "concept_proposal_final_v3.tex"

academic_content = r"""\documentclass[11pt,a4paper]{article}

% ── FONTS (Academic Rigor) ──────────────────────────────────
\usepackage{fontspec}
\setmainfont{Times New Roman}
\newfontfamily{\hindifont}{Nirmala UI}[Script=Devanagari]
\newcommand{\hindi}[1]{{\hindifont #1}}

% ── LAYOUT (Premium Density with Margin) ────────────────────
\usepackage[top=2.5cm,bottom=2.5cm,left=2cm,right=5.5cm, marginparwidth=4.5cm, marginparsep=0.5cm]{geometry}
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
\usepackage{marginnote}
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
\definecolor{keygold}{HTML}{FFF9E6}

% ── ACADEMIC HEADERS ──────────────────────────────────────────
\newcommand{\techsection}[1]{%
  \vspace{0.8cm}\noindent
  {\fontsize{14}{17}\selectfont\bfseries\color{aiggpablue}\MakeUppercase{#1}}%
  \\[-0.15cm]{\color{aiggpagold}\rule{\textwidth}{1.5pt}}\vspace{0.4cm}%
}

\titleformat{\section}[block]{\normalfont}{}{0em}{\techsection}
\titlespacing*{\section}{0pt}{15pt}{10pt}

\titleformat{\subsection}[block]
  {\normalfont\bfseries\fontsize{11}{13}\selectfont\color{aiggpablue}}
  {}{0em}{}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}

% ── CUSTOM MARGIN CALLOUTS ───────────────────────────────────
\newcommand{\sideref}[2]{%
  \marginnote{%
    \begin{tcolorbox}[colback=keygold, colframe=aiggpagold, arc=0mm, left=4pt, right=4pt, top=4pt, bottom=4pt, boxrule=0.5pt]
      \tiny\textbf{\color{aiggpablue}#1}\\[2pt]\color{slate}#2
    \end{tcolorbox}
  }%
}

\newcommand{\marginstat}[2]{%
  \marginnote{%
    \vspace{0.2cm}
    {\fontsize{20}{22}\selectfont\bfseries\color{aiggpagold}#1}\\[-2pt]
    {\tiny\color{slate}\uppercase{#2}}
  }%
}

% ── HEADER / FOOTER ──────────────────────────────────────────
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\footnotesize\color{slate}\textbf{AIGGPA MISSION} \textbar\quad Assessing IT Utilisation}
\fancyhead[R]{\footnotesize\color{aiggpablue}\thepage}
\fancyfoot[L]{\tiny\color{slate} CONFIDENTIAL // INSTITUTIONAL RESEARCH PROPOSAL // MP\_GOV}
\fancyfoot[R]{%
  \begin{tikzpicture}[baseline=(o.base)]
    \node[circle, draw=aiggpagold, inner sep=1pt, font=\tiny\bfseries\color{aiggpablue}] (o) {A};
  \end{tikzpicture}
}
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

\newtcolorbox{sidebox}[1]{
  colback=sand, colframe=stone, boxrule=0.5pt, arc=0mm,
  left=8pt,right=8pt,top=6pt,bottom=6pt,breakable,
  title={\tiny\bfseries\color{slate}#1}, colbacktitle=stone!30}

% ── GLOBAL STYLING ───────────────────────────────────────────
\color{slate}
\pagecolor{sand}

\begin{document}
\onehalfspacing

% ═════════════════════════════════════════════════════════════
%  COVER PAGE (PREMIUM TOPOGRAPHIC TIKZ)
% ═════════════════════════════════════════════════════════════
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  \fill[sand] (current page.south west) rectangle (current page.north east);
  
  % Layer 1: Dense Topo lines
  \begin{scope}[opacity=0.1]
    \foreach \i in {1,...,25} {
      \draw[aiggpablue, thin, decoration={random steps, segment length=8mm, amplitude=12mm}, decorate] 
        ($(current page.south west)+(-5cm,\i*1.2cm)$) -- ($(current page.north east)+(10cm,\i*1.2cm-8cm)$);
    }
  \end{scope}

  % Layer 2: Institutional Grid
  \draw[step=2cm, aiggpagold, opacity=0.08, very thin] (current page.south west) grid (current page.north east);
  
  % Framing
  \draw[aiggpablue, line width=3pt] ($(current page.south west)+(1.2cm,1.2cm)$) rectangle ($(current page.north east)-(1.2cm,1.2cm)$);
  \draw[aiggpagold, line width=0.8pt] ($(current page.south west)+(1.05cm,1.05cm)$) rectangle ($(current page.north east)-(1.05cm,1.05cm)$);

  % Manual AIGGPA Seal in TikZ
  \begin{scope}[shift={($(current page.center)+(0,8cm)$)}, scale=0.8]
    \draw[aiggpablue, line width=1.5pt] (0,0) circle (1.5cm);
    \draw[aiggpagold, line width=1pt] (0,0) circle (1.35cm);
    \node[font=\tiny\bfseries\color{aiggpablue}, text width=2.5cm, align=center] at (0,0) {AIGGPA\\BHOPAL};
    \foreach \a in {0,45,...,315} \draw[aiggpagold, line width=1pt] (\a:1.35cm) -- (\a:1.5cm);
  \end{scope}
\end{tikzpicture}

\vspace*{7cm}
\begin{center}
  \begin{minipage}{0.85\textwidth}
    \centering
    \fontsize{10}{12}\selectfont\color{slate}\textbf{INSTITUTIONAL RESEARCH PROPOSAL}\\[1.5em]
    \fontsize{32}{38}\selectfont\bfseries\color{aiggpablue}
    ASSESSMENT OF IT\\TOOL UTILISATION\\
    \fontsize{18}{22}\selectfont\color{aiggpagold}Among Government Officials\\[1.5em]
    \fontsize{14}{18}\selectfont\color{slate}
    \hindi{सरकारी अधिकारियों द्वारा आईटी उपकरणों के उपयोग का आकलन}
  \end{minipage}
\end{center}

\vfill

\begin{flushright}
  \begin{minipage}{8cm}
    \small\color{slate}
    \begin{tabular}{rl}
      \textbf{Investigator:} & Aryan Kori \\
      \textbf{Body:} & AIGGPA, Bhopal \\
      \textbf{Scope:} & MP Gov Ecosystem \\
      \textbf{Ref:} & AIG-2026-IT-003 \\
    \end{tabular}
  \end{minipage}
\end{flushright}
\vspace{1.5cm}

\newpage
\pagenumbering{arabic}

% ═════════════════════════════════════════════════════════════
%  CONTENT
% ═════════════════════════════════════════════════════════════

\section{Background}

\marginstat{92k+}{Schools in MP}
\sideref{Tech Debt}{GAO reports that legacy systems consume up to 80\% of modern IT budgets.}

\vspace{0.2cm}
The Government of Madhya Pradesh, architected by agencies such as MAP-IT and NIC, handles approximately 350,000 permanent teachers and 92,000 schools through platforms like Education Portal 3.0. Despite this, baseline IT utilization remains a critical bottleneck.

\vspace{0.4cm}
\begin{center}
\begin{tikzpicture}[background rectangle/.style={draw=stone, fill=white, thick}, framed]
  \begin{axis}[
    xbar stacked,
    width=0.8\textwidth, height=4cm, xmin=0, xmax=100,
    ytick=\empty, axis x line=bottom, axis y line=none,
    enlarge y limits=0.5, bar width=18pt,
    xtick={0, 20, 40, 60, 80, 100},
    xticklabel={\pgfmathprintnumber{\tick}\%},
    grid=major, grid style={dotted, slate!40},
    legend style={at={(0.5,-0.4)}, anchor=north, draw=none, fill=none, font=\tiny, legend columns=-1},
    axis line style={aiggpablue, thick},
    title={\textbf{IT Expenditure Trend (Institutional Maintenance vs Growth)}},
    title style={font=\footnotesize\bfseries, yshift=1ex}
  ]
  \addplot [fill=aiggpablue, draw=none] coordinates {(80,0)};
  \addplot [fill=aiggpagold, draw=none] coordinates {(20,0)};
  \legend{Legacy O\&M (80\%), Modernisation (20\%)}
  \end{axis}
\end{tikzpicture}
\end{center}

% ═════════════════════════════════════════════════════════════
\section{Theoretical Framework}

\sideref{UTAUT}{Unified Theory of Acceptance and Use of Technology (Venkatesh et al., 2003)}
\marginstat{4}{Determinants}

This study employs the **UTAUT** framework to bridge individual psychological constraints with bureaucratic realities.

\vspace{0.5cm}
\begin{center}
\begin{tikzpicture}[
  node distance=0.8cm and 1cm,
  box/.style={rectangle, minimum width=2.8cm, minimum height=0.8cm, 
    align=center, font=\tiny\bfseries\color{white}, 
    fill=aiggpablue, draw=aiggpablue!80!black, thick, drop shadow},
  gold_box/.style={box, fill=aiggpagold, draw=aiggpagold!80!black},
  arrow/.style={-{Stealth[length=4pt]}, thick, color=aiggpablue!60, rounded corners=6pt}
]
  \node[box] (pe) {PERFORMANCE (PE/EE)};
  \node[gold_box, left=of pe] (input) {OFFICIAL};
  \node[box, below=of pe] (si) {SOCIAL INFLU. (SI)};
  \node[box, below=of si] (fc) {CONDITIONS (FC)};
  \node[gold_box, right=of si] (out) {AIGGPA\\STRATEGY};

  \draw[arrow] (input) |- (pe);
  \draw[arrow] (input) -- (si);
  \draw[arrow] (input) |- (fc);
  \draw[arrow] (pe) -| (out);
  \draw[arrow] (si) -- (out);
  \draw[arrow] (fc) -| (out);
\end{tikzpicture}
\end{center}

% ═════════════════════════════════════════════════════════════
\section{Institutional Scope}

\marginstat{54}{Respondents}

\begin{academicbox}{PROPOSAL BOUNDARIES}
\renewcommand{\arraystretch}{1.8}
\noindent\begin{tabularx}{\linewidth}{@{} >{\bfseries\color{aiggpablue}\small}p{3.2cm} >{\small}X @{}}
Departments & Education \textbullet{} Health \textbullet{} Forest \\[0.1cm]
Respondents & Class I, II \& IIICadres \\[0.1cm]
Timeline & 10-Week Field Intensive \\
Target Units & State Secretariat \& DTOs \\
\end{tabularx}
\end{academicbox}

% ═════════════════════════════════════════════════════════════
\section{Methodology}

\sideref{Manual Coding}{Rigorous thematic analysis via Braun \& Clarke (2006) coding pipeline.}

\vspace{0.3cm}
\begin{multicols}{2}
\begin{sagebox}
\tiny\textbf{Stream A: Qualitative Path}
\begin{itemize}[leftmargin=1.2em]
  \item Semi-structured sessions
  \item Barrier coding
  \item Skill inventories
\end{itemize}
\end{sagebox}

\columnbreak

\begin{goldbox}
\tiny\textbf{Stream B: Quant. Audit}
\begin{itemize}[leftmargin=1.2em]
  \item System usage logs
  \item Support ticket counts
  \item Infrastructure audit
\end{itemize}
\end{goldbox}
\end{multicols}

\subsection{Sampling Strategy}

\begin{academicbox}{Participant Matrix}
\noindent\begin{tabularx}{\linewidth}{L{3cm} C C C C}
\rowcolor{aiggpablue}
\textbf{\color{white}Profile} & \textbf{\color{white}Edu.} & \textbf{\color{white}Health} & \textbf{\color{white}Forest} & \textbf{\color{white}Total} \\
\rowcolor{white}
Approvers & 4 & 4 & 4 & \textbf{12} \\
\rowcolor{stone!15}
Data Creators & 5 & 5 & 5 & \textbf{15} \\
\rowcolor{white}
Field Users & 6 & 6 & 6 & \textbf{18} \\
\rowcolor{stone!15}
Support Staff & 3 & 3 & 3 & \textbf{9} \\
\rowcolor{aiggpagold!15}
\textbf{TOTAL} & \textbf{18} & \textbf{18} & \textbf{18} & \textbf{54} \\
\end{tabularx}
\end{academicbox}

% ═════════════════════════════════════════════════════════════
\section{Data Synthesis}

\begin{academicbox}{UTAUT Gap Matrix (Draft)}
\noindent\begin{tabularx}{\linewidth}{p{2.5cm} C C C C}
\rowcolor{aiggpablue}
\textbf{\color{white}Segment} & \textbf{\color{white}PE} & \textbf{\color{white}EE} & \textbf{\color{white}SI} & \textbf{\color{white}FC} \\
\rowcolor{white}
Secretariat & \cellcolor{sage!10}Low & \cellcolor{aiggpagold!10}High & \cellcolor{sage!10}Med & \cellcolor{aiggpagold!10}High \\
\rowcolor{stone!10}
Territorial & \cellcolor{aiggpagold!10}High & \cellcolor{sage!10}Low & \cellcolor{aiggpagold!10}High & \cellcolor{sage!10}Med \\
\end{tabularx}
\end{academicbox}

% ═════════════════════════════════════════════════════════════
\section{Projected Work Plan}

\vspace{0.2cm}
\begin{center}
\begin{tikzpicture}[node distance=0cm, outer sep=0pt]
  \node[draw=aiggpablue, fill=aiggpablue, text=white, font=\tiny\bfseries, minimum width=3cm, minimum height=0.6cm] (w1) {Weeks 1-3};
  \node[draw=aiggpagold, fill=aiggpagold, text=white, font=\tiny\bfseries, minimum width=4cm, minimum height=0.6cm, right=of w1] (w4) {Weeks 4-8};
  \node[draw=sage, fill=sage, text=white, font=\tiny\bfseries, minimum width=2cm, minimum height=0.6cm, right=of w4] (w9) {Weeks 9-10};
  
  \node[below=0.2cm of w1, font=\tiny\color{slate}, text width=3cm, align=center] {Literature Review \\ \& Design Pilot};
  \node[below=0.2cm of w4, font=\tiny\color{slate}, text width=4cm, align=center] {Field Intensive \\ (Interviews \& Audit)};
  \node[below=0.2cm of w9, font=\tiny\color{slate}, text width=2cm, align=center] {Synthesis \\ \& Reporting};
\end{tikzpicture}
\end{center}

\vspace{0.4cm}
\renewcommand{\arraystretch}{1.6}
\begin{academicbox}{Deliverable Roadmap}
\noindent\begin{tabularx}{\linewidth}{L{2cm} X X}
\rowcolor{aiggpablue}
\textbf{\color{white}Goal} & \textbf{\color{white}Objective} & \textbf{\color{white}Institutional Output} \\
\rowcolor{white}
\textbf{Milestone 1} & Pilot validated & Site permissions granted \\
\rowcolor{stone!15}
\textbf{Milestone 2} & Data saturation & Coding nodes construction \\
\rowcolor{white}
\textbf{Milestone 3} & Gap analysis & Final training modules \\
\end{tabularx}
\end{academicbox}

% ═════════════════════════════════════════════════════════════
\section{References}

\small
Alrawabdeh, W. (2014). \textit{Int. J. Bus. Soc. Sci.}, 5(8). \\
Bhatnagar, S. (2004). \textit{E-Government Implementation}. Sage. \\
Heeks, R. (2003). \textit{Failure in eGovernment Projects}. Manchester. \\
Venkatesh, V., et al. (2003). \textit{User Acceptance of IT}. MIS Quarterly.

\end{document}
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(academic_content)
