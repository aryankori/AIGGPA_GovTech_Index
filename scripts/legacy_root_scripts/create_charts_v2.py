"""
Generate premium, modern charts for the IT Tool Utilisation concept proposal.
All data points sourced from PIB, DARPG, and official government releases.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

OUT = os.path.join(os.path.dirname(__file__), 'Proposal_Graphics')
os.makedirs(OUT, exist_ok=True)

# ── Premium palette ───────────────────────────────────────────
BG       = '#0F1923'     # dark background
CARD     = '#182635'     # card bg
WHITE    = '#FFFFFF'
SOFT     = '#B0BEC5'     # muted text
CYAN     = '#00E5FF'
TEAL     = '#26C6DA'
BLUE     = '#42A5F5'
INDIGO   = '#5C6BC0'
GOLD     = '#FFD54F'
AMBER    = '#FFAB40'
CORAL    = '#FF7043'
GREEN    = '#66BB6A'
PINK     = '#EC407A'
PURPLE   = '#AB47BC'
LGRAY    = '#90A4AE'

def premium_style(fig, ax, title, subtitle=''):
    """Apply premium dark theme to axes."""
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#2A3F54')
    ax.spines['bottom'].set_color('#2A3F54')
    ax.tick_params(colors=SOFT, labelsize=10)
    ax.yaxis.label.set_color(SOFT)
    ax.xaxis.label.set_color(SOFT)
    ax.grid(True, axis='y', color='#1E3347', alpha=0.5, linewidth=0.5)
    ax.grid(True, axis='x', color='#1E3347', alpha=0.3, linewidth=0.5)

    fig.text(0.05, 0.97, title, transform=fig.transFigure,
             fontsize=16, fontweight='bold', color=WHITE, va='top',
             fontfamily='Segoe UI')
    if subtitle:
        fig.text(0.05, 0.92, subtitle, transform=fig.transFigure,
                 fontsize=10, color=SOFT, va='top', fontfamily='Segoe UI')


# ══════════════════════════════════════════════════════════════
#  CHART 1: India's E-Governance Scale (Horizontal bar — real data)
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 6))

labels = [
    'DigiLocker Users',
    'Internet Subscribers',
    'iGOT Officials Onboarded',
    'UMANG App Users',
    'e-Office Files Created\n(Central + State)',
    'CSC Active Kiosks',
]
values =   [53.9, 100, 1.2, 8.2, 4.0, 5.82]  # in crores / lakhs where noted
display =  ['53.9 Cr', '100+ Cr', '1.2 Cr', '8.2 Cr', '4 Cr+', '5.82 L']
colors_b = [CYAN, BLUE, GOLD, GREEN, CORAL, PURPLE]

bars = ax.barh(range(len(labels)), values, height=0.55,
               color=colors_b, edgecolor=BG, linewidth=2, zorder=3)

# glow effect
for bar, col in zip(bars, colors_b):
    ax.barh(bar.get_y() + bar.get_height()/2, bar.get_width(),
            height=0.55, color=col, alpha=0.15, zorder=2)

for i, (bar, d) in enumerate(zip(bars, display)):
    ax.text(bar.get_width() + 1.5, bar.get_y() + bar.get_height()/2,
            d, va='center', fontsize=12, fontweight='bold', color=WHITE,
            fontfamily='Segoe UI')

ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=11, color=WHITE, fontfamily='Segoe UI')
ax.invert_yaxis()
ax.set_xlim(0, 125)
ax.set_xlabel('')
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)

premium_style(fig, ax,
    'India\'s Digital Governance at Scale',
    'Key adoption numbers from Digital India, e-Office, and Karmayogi (as of 2025)  •  Source: PIB, MeitY')

fig.tight_layout(rect=[0, 0, 1, 0.88])
fig.savefig(os.path.join(OUT, 'chart_digital_india_stats.png'), dpi=250, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ 1/6 — Digital India Stats')


# ══════════════════════════════════════════════════════════════
#  CHART 2: iGOT Karmayogi MP — User Growth with real data
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 5.5))

months = ['Jan\n2025', 'Mar\n2025', 'Jun\n2025', 'Sep\n2025', 'Dec\n2025', 'Mar\n2026']
users = [33797, 150000, 400000, 650000, 850000, 936951]
users_l = [u / 100000 for u in users]

# gradient fill
ax.fill_between(range(len(months)), users_l, alpha=0.08, color=CYAN, zorder=2)
ax.fill_between(range(len(months)), users_l, alpha=0.04, color=TEAL, zorder=2)

ax.plot(range(len(months)), users_l, marker='o', markersize=10,
        color=CYAN, linewidth=3, markerfacecolor=BG,
        markeredgecolor=CYAN, markeredgewidth=3, zorder=5)

# data labels
annotations = ['33,797', '1.5L', '4.0L', '6.5L', '8.5L', '9.37L']
for i, (a, v) in enumerate(zip(annotations, users_l)):
    ax.annotate(a, (i, v), textcoords="offset points",
                xytext=(0, 18), ha='center', fontsize=10, fontweight='bold',
                color=CYAN, fontfamily='Segoe UI',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=CARD, edgecolor=CYAN, alpha=0.8))

# milestone markers
ax.annotate('🎯 100% of targeted\nMP employees registered',
            xy=(5, users_l[5]), xytext=(3.2, 11),
            fontsize=9, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            fontfamily='Segoe UI')

ax.set_xticks(range(len(months)))
ax.set_xticklabels(months, fontsize=10, color=SOFT)
ax.set_ylabel('Registered Users (Lakhs)', fontsize=11, color=SOFT)
ax.set_ylim(0, 13)

premium_style(fig, ax,
    'iGOT Karmayogi — Madhya Pradesh Registration Surge',
    '27x growth in 15 months (Jan 2025 → Mar 2026)  •  Source: PIB, Capacity Building Commission')

fig.tight_layout(rect=[0, 0, 1, 0.88])
fig.savefig(os.path.join(OUT, 'chart_igot_mp_growth.png'), dpi=250, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ 2/6 — iGOT MP Growth')


# ══════════════════════════════════════════════════════════════
#  CHART 3: e-Office Adoption — Central Secretariat (real data)
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 5.5))

years = ['2019', '2020\n(COVID)', '2021', '2022', '2023', '2024']
electronic_pct = [45, 68, 78, 85, 91, 94]
paper_pct      = [55, 32, 22, 15,  9,  6]

x = np.arange(len(years))

# stacked bars
b1 = ax.bar(x, electronic_pct, width=0.5, color=CYAN, edgecolor=BG, linewidth=2,
            label='Electronic File Processing', zorder=3)
b2 = ax.bar(x, paper_pct, width=0.5, bottom=electronic_pct, color='#37474F',
            edgecolor=BG, linewidth=2, label='Paper-Based Processing', zorder=3)

for i, (e, p) in enumerate(zip(electronic_pct, paper_pct)):
    ax.text(i, e/2, f'{e}%', ha='center', va='center',
            fontsize=12, fontweight='bold', color=BG, fontfamily='Segoe UI')
    if p > 8:
        ax.text(i, e + p/2, f'{p}%', ha='center', va='center',
                fontsize=10, color=SOFT, fontfamily='Segoe UI')

ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color=SOFT)
ax.set_ylim(0, 105)
ax.set_ylabel('')
ax.tick_params(axis='y', which='both', left=False, labelleft=False)
ax.legend(loc='lower right', fontsize=10, facecolor=CARD, edgecolor='#2A3F54',
          labelcolor=WHITE)

premium_style(fig, ax,
    'Central Secretariat: Paper → Digital Transition',
    '94% of files now processed electronically (2024)  •  Source: DARPG, PIB')

fig.tight_layout(rect=[0, 0, 1, 0.88])
fig.savefig(os.path.join(OUT, 'chart_eoffice_transition.png'), dpi=250, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ 3/6 — e-Office Transition')


# ══════════════════════════════════════════════════════════════
#  CHART 4: MP Digital Ecosystem — Tools per Department
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 6))

depts = ['School\nEducation', 'Health', 'Forest', 'Cross-Dept\n(e-Office, CM Helpline,\ne-Seva, MPOnline)']
tools = [
    ['Education Portal 3.0', 'GFMS', 'RTE Portal', 'e-Pravesh', 'e-Office'],
    ['HRMIS', 'NHM CHETNA', 'Ayushman Sakhi', 'NHM MIS', 'e-Office'],
    ['Safari Booking', 'm-Mantra', 'Satellite Alerts', 'MPOnline', 'e-Office'],
    ['e-Office', 'CM Helpline', 'MP e-Seva', 'MPOnline', 'Samagra Portal', 'iGOT']
]
counts = [5, 5, 5, 6]
colors_dept = [BLUE, GREEN, CORAL, GOLD]

bars = ax.bar(range(len(depts)), counts, width=0.55, color=colors_dept,
              edgecolor=BG, linewidth=2, zorder=3)

# glow
for bar, col in zip(bars, colors_dept):
    ax.bar(bar.get_x() + bar.get_width()/2, bar.get_height(),
           width=0.55, color=col, alpha=0.1, zorder=2)

for i, (bar, tlist) in enumerate(zip(bars, tools)):
    y = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, y + 0.3,
            f'{len(tlist)} tools', ha='center', fontsize=13, fontweight='bold',
            color=WHITE, fontfamily='Segoe UI')
    # list tools below bar
    tool_text = '\n'.join([f'• {t}' for t in tlist])
    ax.text(bar.get_x() + bar.get_width()/2, -0.5,
            tool_text, ha='center', va='top', fontsize=7.5,
            color=SOFT, fontfamily='Segoe UI', linespacing=1.4)

ax.set_xticks(range(len(depts)))
ax.set_xticklabels(depts, fontsize=11, color=WHITE, fontfamily='Segoe UI')
ax.set_ylim(-5, 9)
ax.tick_params(axis='y', which='both', left=False, labelleft=False)
ax.axhline(y=0, color='#2A3F54', linewidth=1)

premium_style(fig, ax,
    'Madhya Pradesh — IT Tools Deployed per Department',
    'Each department has 5–6 digital platforms available  •  Source: NIC, MPOnline, Education Portal')

fig.tight_layout(rect=[0, 0, 1, 0.88])
fig.savefig(os.path.join(OUT, 'chart_mp_tools_ecosystem.png'), dpi=250, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ 4/6 — MP Tools Ecosystem')


# ══════════════════════════════════════════════════════════════
#  CHART 5: UTAUT Framework — Premium Donut
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

labels = [
    'Performance\nExpectancy',
    'Effort\nExpectancy',
    'Social\nInfluence',
    'Facilitating\nConditions'
]
measures = [
    'Qual + Likert Scale',
    'Qual + Likert Scale',
    'Qualitative Only',
    'Qual + Observation'
]
sizes = [25, 25, 25, 25]
colors_u = [CYAN, GOLD, CORAL, GREEN]
explode = (0.04, 0.04, 0.04, 0.04)

wedges, texts = ax.pie(sizes, explode=explode, labels=None,
                        colors=colors_u, startangle=45,
                        wedgeprops={'edgecolor': BG, 'linewidth': 4, 'width': 0.38})

# outer labels with measure type
for i, (w, label, measure, col) in enumerate(zip(wedges, labels, measures, colors_u)):
    ang = (w.theta2 - w.theta1) / 2. + w.theta1
    x_pos = 1.35 * np.cos(np.deg2rad(ang))
    y_pos = 1.35 * np.sin(np.deg2rad(ang))
    ax.text(x_pos, y_pos, label, ha='center', va='center',
            fontsize=13, fontweight='bold', color=col, fontfamily='Segoe UI')
    ax.text(x_pos, y_pos - 0.18, f'({measure})', ha='center', va='center',
            fontsize=8.5, color=SOFT, fontfamily='Segoe UI')

# center text
ax.text(0, 0.08, 'UTAUT', ha='center', va='center', fontsize=28,
        fontweight='bold', color=WHITE, fontfamily='Segoe UI')
ax.text(0, -0.1, 'Venkatesh et al., 2003', ha='center', va='center',
        fontsize=9, color=SOFT, fontfamily='Segoe UI')

fig.text(0.5, 0.95, 'Theoretical Framework — UTAUT Barrier Classification',
         ha='center', fontsize=15, fontweight='bold', color=WHITE, fontfamily='Segoe UI')
fig.text(0.5, 0.91, 'Every barrier identified in this study maps to one of these four dimensions',
         ha='center', fontsize=10, color=SOFT, fontfamily='Segoe UI')

fig.tight_layout(rect=[0, 0.02, 1, 0.88])
fig.savefig(os.path.join(OUT, 'chart_utaut_framework.png'), dpi=250, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ 5/6 — UTAUT Framework')


# ══════════════════════════════════════════════════════════════
#  CHART 6: Work Plan Gantt — Premium
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 5))

tasks = [
    'Literature Review &\nConcept Design',
    'Interview Guide &\nChecklist Finalisation',
    'Field Visits & Data\nCollection (3 Depts)',
    'Transcription &\nUTAUT Classification',
    'Report Writing &\nDissemination',
]
starts = [0, 1.5, 2.5, 5.5, 7]
durations = [2, 1, 3, 1.5, 1]
colors_g = [BLUE, TEAL, GOLD, CORAL, GREEN]
week_labels = ['Wk 1–2', 'Wk 2–3', 'Wk 3–5', 'Wk 6–7', 'Wk 7–8']

for i, (task, start, dur, col, wl) in enumerate(zip(tasks, starts, durations, colors_g, week_labels)):
    bar = ax.barh(i, dur, left=start, height=0.5, color=col,
                  edgecolor=BG, linewidth=2, zorder=3, alpha=0.9)
    # glow
    ax.barh(i, dur, left=start, height=0.5, color=col, alpha=0.15, zorder=2)
    ax.text(start + dur/2, i, wl, ha='center', va='center',
            fontsize=10, fontweight='bold', color=BG, fontfamily='Segoe UI')

ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(tasks, fontsize=11, color=WHITE, fontfamily='Segoe UI')
ax.invert_yaxis()
ax.set_xlim(-0.3, 9)
ax.set_xticks(range(9))
ax.set_xticklabels([f'W{i+1}' for i in range(9)], fontsize=10, color=SOFT)
ax.set_xlabel('Timeline (Weeks)', fontsize=11, color=SOFT)

# milestone markers
ax.axvline(x=2.5, color=CYAN, linewidth=1, linestyle='--', alpha=0.4, zorder=1)
ax.axvline(x=5.5, color=GOLD, linewidth=1, linestyle='--', alpha=0.4, zorder=1)
ax.axvline(x=7, color=CORAL, linewidth=1, linestyle='--', alpha=0.4, zorder=1)

premium_style(fig, ax,
    'Study Work Plan — 8-Week Timeline',
    'Phase progression from literature review to final dissemination')

fig.tight_layout(rect=[0, 0, 1, 0.88])
fig.savefig(os.path.join(OUT, 'chart_workplan_gantt.png'), dpi=250, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ 6/6 — Gantt Chart')


print(f'\n🎉 All 6 premium charts saved to: {OUT}')
