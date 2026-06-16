import re
import os

filepath = "concept_proposal_final_v3.tex"
hero_image_path = r"C:\Users\aryan\.gemini\antigravity\brain\6e8468d5-c3e1-4169-b1a5-53e231bbc6a3\high_tech_governance_abstract_art_1776336447651.png"

# Ensure the image path is relative or escaped for LaTeX
hero_image_tex = hero_image_path.replace("\\", "/")

artistic_content = r"""\documentclass[11pt,a4paper]{article}

% ── FONTS ────────────────────────────────────────────────────
\usepackage{fontspec}
\setmainfont{Calibri}
\setsansfont{Calibri}
\newfontfamily{\hindifont}{Nirmala UI}[Script=Devanagari]
\newcommand{\hindi}[1]{{\hindifont #1}}

% ── LAYOUT ───────────────────────────────────────────────────
\usepackage[top=2cm,bottom=2.5cm,left=2.5cm,right=2cm]{geometry} % Asymmetric
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{shadows,calc,shapes.geometric,arrows.meta,positioning,fit,backgrounds,patterns}
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

% ── ARTISTIC TECH PALETTE ─────────────────────────────────────
\definecolor{deepink}{HTML}{0D0E12}
\definecolor{cyberpurple}{HTML}{7C3AED}
\definecolor{cybercyan}{HTML}{06B6D4}
\definecolor{cyberpink}{HTML}{EC4899}
\definecolor{cyberviolet}{HTML}{4F46E5}
\definecolor{glassy}{HTML}{1F2937}
\definecolor{lightgray}{HTML}{E2E8F0}
\definecolor{dimtext}{HTML}{94A3B8}

% ── CUSTOM BACKGROUND ON EVERY PAGE ──────────────────────────────
\usepackage{background}
\backgroundsetup{
  scale=1,
  color=black,
  opacity=1,
  angle=0,
  contents={%
    \begin{tikzpicture}[remember picture,overlay]
      \fill[deepink] (current page.south west) rectangle (current page.north east);
      % Subtle grid
      \draw[step=1cm,white!3,very thin] (current page.south west) grid (current page.north east);
      % Decorative telemetry line
      \draw[cybercyan!20, line width=0.5pt] ($(current page.north west)+(1.2cm,-1cm)$) -- ($(current page.north west)+(1.2cm,-28cm)$);
      \draw[cyberpink!20, line width=0.5pt] ($(current page.north west)+(1cm,-5cm)$) -- ($(current page.north west)+(1.4cm,-5cm)$);
    \end{tikzpicture}
  }
}

% ── ARTISTIC HEADERS ──────────────────────────────────────────
\newcommand{\techsection}[1]{%
  \vspace{1cm}\noindent
  \begin{tikzpicture}[remember picture, overlay]
    \node[anchor=west, opacity=0.15, scale=6, font=\bfseries\color{cyberviolet}] at (0,0.5) {\thesection};
  \end{tikzpicture}%
  {\fontsize{18}{22}\selectfont\bfseries\color{cybercyan}\MakeUppercase{#1}}%
  \\[-0.2cm]{\color{cyberpink}\rule{\textwidth}{2pt}}\vspace{0.6cm}%
}

\titleformat{\section}[block]{\normalfont}{}{0em}{\techsection}
\titlespacing*{\section}{0pt}{20pt}{12pt}

\titleformat{\subsection}[block]
  {\normalfont\bfseries\fontsize{13}{15}\selectfont\color{cyberpink}}
  {}{0em}{}
\titlespacing*{\subsection}{0pt}{12pt}{6pt}

% ── HEADER / FOOTER ──────────────────────────────────────────
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\footnotesize\color{dimtext}\textbf{AIGGPA MISSION} \quad\textbar\quad ID: 2026-IT-SEC}
\fancyhead[R]{\footnotesize\color{cybercyan}\thepage}
\fancyfoot[L]{\tiny\color{dimtext} CONFIDENTIAL // INSTITUTIONAL RESEARCH PROPOSAL // MP\_GOV\_DPT}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% ── GLASS BOXES ─────────────────────────────────────────────
\newtcolorbox{glassbox}[1]{
  colback=glassy!80, colframe=cyberviolet, boxrule=1pt, arc=2mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable,
  fonttitle=\bfseries\color{cybercyan}, title=#1}

\newtcolorbox{pinkglassbox}{
  colback=glassy!80, colframe=cyberpink, boxrule=1pt, arc=2mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable}

\newtcolorbox{cyanglassbox}{
  colback=glassy!80, colframe=cybercyan, boxrule=1pt, arc=2mm,
  left=12pt,right=12pt,top=10pt,bottom=10pt,breakable}

% ── GLOBAL TEXT COLOR ─────────────────────────────────────────
\color{lightgray}

\begin{document}
\onehalfspacing

% ═════════════════════════════════════════════════════════════
%  COVER PAGE (ARTISTIC)
% ═════════════════════════════════════════════════════════════
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  % Full bleed hero
  \node[anchor=center] at (current page.center) {\includegraphics[width=\paperwidth,height=\paperheight]{""" + hero_image_tex + r"""}};
  
  % Dark overlay gradient for text legibility
  \fill[deepink, opacity=0.4] (current page.south west) rectangle (current page.north east);
  
  % Aesthetic bars
  \fill[cybercyan] ($(current page.north west)+(0.5\paperwidth,-2cm)$) rectangle ($(current page.north west)+(0.5\paperwidth+4cm,-2.2cm)$);
  \fill[cyberpink] ($(current page.north west)+(0.5\paperwidth+4.5cm,-2cm)$) rectangle ($(current page.north west)+(0.5\paperwidth+5cm,-2.2cm)$);
\end{tikzpicture}

\vspace*{3cm}
\begin{flushright}
  \begin{minipage}{0.8\textwidth}
    \begin{flushright}
      \fontsize{12}{14}\selectfont\color{cybercyan}\textbf{AIGGPA INSTITUTIONAL PROPOSAL}\\[1em]
      \fontsize{42}{48}\selectfont\bfseries\color{white}
      ASSESSMENT OF\\
      IT TOOL\\
      UTILISATION\\[0.5em]
      \fontsize{16}{20}\selectfont\color{cyberpink}
      \hindi{सरकारी अधिकारियों द्वारा आईटी उपकरणों के उपयोग का आकलन}
    \end{flushright}
  \end{minipage}
\end{flushright}

\vfill

\begin{flushleft}
  \hspace{1cm}
  \begin{minipage}{10cm}
    \small\color{lightgray}
    \begin{tabular}{@{}ll@{}}
      \textbf{\color{cybercyan}INVESTIGATOR:} & ARYAN KORI \\
      \textbf{\color{cybercyan}INSTITUTION:}  & AIGGPA BHOPAL \\
      \textbf{\color{cybercyan}TARGETS:}      & MP GOV DEPARTMENTS \\
      \textbf{\color{cybercyan}VERSION:}       & 3.0 ARTISTIC \\
    \end{tabular}
  \end{minipage}
\end{flushleft}
\vspace{1cm}

\newpage
\pagenumbering{arabic}

% ═════════════════════════════════════════════════════════════
%  CONTENT START
% ═════════════════════════════════════════════════════════════

\section{Background}

\vspace{0.2cm}
The Government of Madhya Pradesh, architected primarily by technical agencies such as MAP-IT and NIC, has built an impressive portfolio of digital platforms across its key departments:

\begin{itemize}[leftmargin=1.4em, label=\textcolor{cybercyan}{\textbullet}]
  \item \textbf{\color{white}School Education:} Education Portal 3.0 is designed to manage
    approximately 350,000 permanent teachers across 92,000+ schools.\footnote{Government
    of Madhya Pradesh, School Education Department (2025). \textit{Education Portal
    3.0}. \url{https://sederp.educationportal3.in}.}
  \item \textbf{\color{white}Health:} The department operates HRMIS, NHM CHETNA, and an AI chatbot ``Ayushman Sakhi.''
  \item \textbf{\color{white}Forest:} Real-time encroachment alerts and wildlife tourism permitting via MPOnline.
\end{itemize}

Despite these platforms, day-to-day workflows still run on physical registers and informal digital tools. The lack of 
institutionalised usage norms and inadequate front-line computing training are common 
barriers to IT tools in public administration (Bhatnagar, 2004). Often, failures originate from a \textit{design-reality gap} (Heeks, 2003). 

% ═════════════════════════════════════════════════════════════
\section{Rationale}

\vspace{0.2cm}

Maximizing adoption translates to structural resilience. As reported by the GAO (2019), up to 80\% of IT budgets are consumed entirely by maintenance of legacy systems.

\vspace{0.4cm}
\begin{center}
\begin{tikzpicture}[framed, background rectangle/.style={draw=cyberpurple, rounded corners=5pt, fill=glassy, thick, drop shadow}]
  \begin{axis}[
    xbar stacked,
    width=12cm, height=4.5cm, xmin=0, xmax=100,
    ytick=\empty, axis x line=bottom, axis y line=none,
    enlarge y limits=0.5, bar width=18pt,
    xtick={0, 20, 40, 60, 80, 100},
    xticklabel={\color{dimtext}\pgfmathprintnumber{\tick}\%},
    grid=major, grid style={dashed, white!10},
    legend style={at={(0.5,-0.38)}, anchor=north, draw=none, fill=none, font=\footnotesize, legend columns=-1, text=lightgray},
    axis line style={white!30, very thick},
    title={\textbf{\color{white}IT BUDGET ALLOCATION ESTIMATES (GAO 2019)}},
    title style={font=\small\bfseries, yshift=1ex}
  ]
  \addplot [fill=cyberpurple, draw=none] coordinates {(80,0)};
  \addplot [fill=cybercyan, draw=none] coordinates {(20,0)};
  \legend{Legacy Maintenance (80\%), Modernisation (20\%)}
  \end{axis}
\end{tikzpicture}
\end{center}

% ═════════════════════════════════════════════════════════════
\section{Theoretical Framework}

To bridge individual psychological constraints with bureaucratic realities, this study employs the \textbf{Unified Theory of Acceptance and Use of Technology (UTAUT)} (Venkatesh et al., 2003).

\vspace{0.5cm}

\begin{center}
\begin{tikzpicture}[
  node distance=1cm and 1.5cm,
  box/.style={rectangle, minimum width=3.2cm, minimum height=1cm, 
    align=center, font=\scriptsize\bfseries\color{white}, 
    fill=cyberviolet, draw=cybercyan, thick, drop shadow, rounded corners=6pt,
    top color=cyberviolet, bottom color=cyberpurple!80},
  input_box/.style={box, top color=cyberpink, bottom color=cyberpink!60, draw=white},
  glow_box/.style={box, top color=cybercyan, bottom color=cybercyan!60, draw=white, text=deepink},
  arrow/.style={-{Stealth[length=6pt]}, ultra thick, color=cybercyan!80, rounded corners=8pt, drop shadow}
]
  \node[glow_box] (pe) {PERFORMANCE (PE/EE)};
  \node[input_box, left=of pe] (input) {OFFICIAL};
  \node[box, below=of pe] (si) {SOCIAL INFL. (SI)};
  \node[box, below=of si] (fc) {CONDITIONS (FC)};
  \node[glow_box, right=of si] (out) {AIGGPA\\iGOT MODULE};

  \draw[arrow] (input) |- (pe);
  \draw[arrow] (input) -- (si);
  \draw[arrow] (input) |- (fc);
  \draw[arrow] (pe) -| (out);
  \draw[arrow] (si) -- (out);
  \draw[arrow] (fc) -| (out);
\end{tikzpicture}
\end{center}

% ═════════════════════════════════════════════════════════════
\section{Research Objectives}

\begin{glassbox}{CORE TARGETS}
\begin{enumerate}[label={\color{cybercyan}\bfseries\arabic*.},itemsep=6pt]
  \item \textbf{Map tool usage} across official categories.
  \item \textbf{Assess workflows} for correspondce and records.
  \item \textbf{Capture IT perspectives} via usage stats.
  \item \textbf{Classify barriers} using UTAUT nodes.
\end{enumerate}
\end{glassbox}

% ═════════════════════════════════════════════════════════════
\section{Scope}

\begin{cyanglassbox}
\vspace{0.1cm}
\begin{tabularx}{\textwidth}{@{} >{\bfseries\color{cybercyan}\small}p{3.2cm} >{\small}X @{}}
Departments & School Education \textbullet{} Health \textbullet{} Forest (MP Govt) \\[0.1cm]
Respondents & Officials (Class I, II \& III) and IT staff \\[0.1cm]
Duration & April to June 2026 \\[0.1cm]
Output & Gap analysis report and prioritised recommendations \\
\end{tabularx}
\end{cyanglassbox}

% ═════════════════════════════════════════════════════════════
\section{Methodology}

Parallel collection streams ensure data triangulation:

\vspace{0.4cm}
\begin{multicols}{2}
\begin{glassbox}{STREAM A: OFFICIALS}
\tiny
\begin{itemize}[label=\textcolor{cybercyan}{\tiny\textbullet}]
  \item Daily task mapping
  \item Tool inventory
  \item Barrier identification
\end{itemize}
\end{glassbox}

\columnbreak

\begin{glassbox}{STREAM B: IT SYSTEMS}
\tiny
\begin{itemize}[label=\textcolor{cyberpink}{\tiny\textbullet}]
  \item Deployed platforms
  \item \textbf{Usage Statistics}
  \item Technical support audit
\end{itemize}
\end{glassbox}
\end{multicols}

\subsection{Sampling Strategy}

\vspace{0.4cm}
\begin{tabularx}{\textwidth}{L{3.5cm} C C C C}
\rowcolor{cyberpurple}
\textbf{\color{white}Profile} & \textbf{\color{white}Edu.} & \textbf{\color{white}Health} & \textbf{\color{white}Forest} & \textbf{\color{white}Total} \\
\rowcolor{glassy}
Approvers & 4 & 4 & 4 & \textbf{12} \\
\rowcolor{deepink}
Data Creators & 5 & 5 & 5 & \textbf{15} \\
\rowcolor{glassy}
Field Users & 6 & 6 & 6 & \textbf{18} \\
\rowcolor{deepink}
IT Support & 3 & 3 & 3 & \textbf{9} \\
\rowcolor{cyberpink}
\textbf{SUBTOTAL} & \textbf{18} & \textbf{18} & \textbf{18} & \textbf{54} \\
\end{tabularx}

% ═════════════════════════════════════════════════════════════
\section{Data Analysis \& Matrix}

\begin{tikzpicture}[remember picture, overlay]
  \draw[cybercyan, line width=10pt, opacity=0.05] (current page.center) circle (5cm);
\end{tikzpicture}

Findings are mapped to \textbf{UTAUT Matrices} using ATLAS.ti coding.

\vspace{0.4cm}
\noindent\small\textbf{Matrix A (Secretariat Workflow)}
\begin{tabularx}{\textwidth}{l C C C C}
\rowcolor{cybercyan}
\textbf{\color{deepink}Dpt} & \textbf{\color{deepink}PE} & \textbf{\color{deepink}EE} & \textbf{\color{deepink}SI} & \textbf{\color{deepink}FC} \\
\rowcolor{glassy}
Edu. & & & & \\
\rowcolor{deepink}
Health & & & & \\
\end{tabularx}

% ═════════════════════════════════════════════════════════════
\section{Work Plan}

\vspace{0.2cm}
\renewcommand{\arraystretch}{1.8}
\begin{tabularx}{\textwidth}{L{2.2cm} L{4.5cm} X}
\rowcolor{cyberpurple}
\textbf{\color{white}Phase} & \textbf{\color{white}Activity} & \textbf{\color{white}Milestone} \\
\rowcolor{glassy}
Week 1-2 & Literature & Signed Proposal \\
\rowcolor{deepink}
Week 3 & Design & Pilot Test \\
\rowcolor{glassy}
Week 4-8 & Field Ops & Case Studies \\
\rowcolor{deepink}
Week 9-10 & Synthesis & Final Report \\
\end{tabularx}

% ═════════════════════════════════════════════════════════════
\section{References}

\small
Alrawabdeh, W. (2014). \textit{Int J Bus Soc Sci}, 5(8). \\
Braun, V., \& Clarke, V. (2006). \textit{Qual Res Psychol}, 3(2). \\
Venkatesh, V. et al. (2003). \textit{MIS Quarterly}, 425--478.

\end{document}
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(artistic_content)
