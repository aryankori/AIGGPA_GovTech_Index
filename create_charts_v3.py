"""
Premium Wall-Street quality charts for the research proposal.
Every data point is sourced from PIB, TRAI, UN DESA, or DARPG.
White background, clean serif/sans, black & gray palette.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

OUT = os.path.join(os.path.dirname(__file__), 'Proposal_Graphics')
os.makedirs(OUT, exist_ok=True)

# ── Minimalist palette (B&W / finance-grade) ─────────────────
BG      = '#FFFFFF'
BLACK   = '#1A1A1A'
DGRAY   = '#3C3C3C'
MGRAY   = '#707070'
LGRAY   = '#B0B0B0'
VLGRAY  = '#E8E8E8'
ACCENT  = '#1A1A1A'
ACCENT2 = '#5A5A5A'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Georgia', 'Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.facecolor': BG,
    'figure.facecolor': BG,
    'axes.edgecolor': LGRAY,
    'axes.labelcolor': DGRAY,
    'xtick.color': MGRAY,
    'ytick.color': MGRAY,
    'text.color': BLACK,
    'axes.grid': False,
})

def add_source(fig, text, y=0.02):
    fig.text(0.12, y, text, fontsize=7, color=LGRAY, fontstyle='italic', fontfamily='sans-serif')

def add_figure_label(fig, label, y=0.955):
    fig.text(0.12, y, label, fontsize=7.5, color=MGRAY, fontweight='bold', fontfamily='sans-serif')


# ═══════════════════════════════════════════════════════════════
#  FIGURE 1: India's UN E-Government Ranking (2014–2024)
#  Source: UN DESA E-Government Survey (biennial)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))

years = [2014, 2016, 2018, 2020, 2022, 2024]
ranks = [118,  107,  96,   100,  105,  97]

ax.plot(years, ranks, color=BLACK, linewidth=2.2, marker='o', markersize=7,
        markerfacecolor=BG, markeredgecolor=BLACK, markeredgewidth=2, zorder=5)

# Fill below
ax.fill_between(years, ranks, max(ranks)+5, alpha=0.04, color=BLACK)

for yr, rk in zip(years, ranks):
    offset = -16 if rk <= 100 else 14
    ax.annotate(f'#{rk}', (yr, rk), textcoords='offset points',
                xytext=(0, offset), ha='center', fontsize=10, fontweight='bold', color=BLACK)

ax.set_ylabel('Rank (out of 193 countries)', fontsize=10)
ax.set_xlabel('')
ax.set_xticks(years)
ax.set_xlim(2013, 2025)
ax.invert_yaxis()
ax.set_ylim(125, 88)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color(LGRAY)
ax.spines['left'].set_color(LGRAY)
ax.axhline(y=100, color=LGRAY, linewidth=0.8, linestyle='--', alpha=0.6)
ax.text(2024.3, 100, 'Top 100', fontsize=7.5, color=LGRAY, va='center')

fig.suptitle("India's UN E-Government Development Index Ranking",
             fontsize=14, fontweight='bold', x=0.12, ha='left', y=0.98)
fig.text(0.12, 0.91, 'Biennial assessment of 193 UN member states on e-governance maturity',
         fontsize=9, color=MGRAY, fontfamily='sans-serif')
add_source(fig, 'Source: United Nations Department of Economic & Social Affairs, E-Government Survey 2014–2024')
add_figure_label(fig, 'FIGURE 1')

fig.tight_layout(rect=[0.05, 0.06, 0.98, 0.88])
fig.savefig(os.path.join(OUT, 'fig1_un_egdi_ranking.png'), dpi=300, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ Figure 1: UN EGDI Ranking')


# ═══════════════════════════════════════════════════════════════
#  FIGURE 2: India Internet Subscribers (2015–2024)
#  Source: TRAI Annual Performance Indicators
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))

years2 = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
subs   = [30.2, 34.3, 39.2, 49.4, 63.7, 74.3, 82.5, 83.4, 88.1, 95.4]

# Bar chart with gradient effect
bars = ax.bar(years2, subs, width=0.65, color=DGRAY, edgecolor=BG, linewidth=0.5, zorder=3)
# highlight last bar
bars[-1].set_color(BLACK)

for yr, s in zip(years2, subs):
    ax.text(yr, s + 1.5, f'{s}', ha='center', fontsize=7.5, fontweight='bold', color=DGRAY)

# Growth annotation
ax.annotate('', xy=(2024, 95.4), xytext=(2015, 30.2),
            arrowprops=dict(arrowstyle='->', color=LGRAY, lw=1.5, linestyle='--'))
ax.text(2019.5, 70, '+216%\ngrowth', ha='center', fontsize=9, color=MGRAY, fontweight='bold')

ax.set_ylabel('Subscribers (Crores)', fontsize=10)
ax.set_xticks(years2)
ax.set_xticklabels([str(y) for y in years2], fontsize=8.5)
ax.set_ylim(0, 110)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(LGRAY)
ax.spines['bottom'].set_color(LGRAY)

fig.suptitle('India: Total Internet Subscribers',
             fontsize=14, fontweight='bold', x=0.12, ha='left', y=0.98)
fig.text(0.12, 0.91, 'As of March each year  ·  Broadband crossed 100 Cr mark in Nov 2025',
         fontsize=9, color=MGRAY, fontfamily='sans-serif')
add_source(fig, 'Source: Telecom Regulatory Authority of India (TRAI), Annual Performance Indicators')
add_figure_label(fig, 'FIGURE 2')

fig.tight_layout(rect=[0.05, 0.06, 0.98, 0.88])
fig.savefig(os.path.join(OUT, 'fig2_internet_subscribers.png'), dpi=300, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ Figure 2: Internet Subscribers')


# ═══════════════════════════════════════════════════════════════
#  FIGURE 3: iGOT Karmayogi National Enrollment Growth
#  Source: PIB releases (dates cited)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))

dates3  = ['Jan\n2023', 'May\n2025', 'Jul\n2025', 'Dec\n2025', 'Feb\n2026', 'Mar\n2026']
users3  = [3, 100, 126, 145, 148, 153]   # in lakhs

ax.plot(range(len(dates3)), users3, color=BLACK, linewidth=2.2, marker='D', markersize=6,
        markerfacecolor=BG, markeredgecolor=BLACK, markeredgewidth=2, zorder=5)
ax.fill_between(range(len(dates3)), users3, alpha=0.06, color=BLACK)

labels3 = ['3 L', '1.0 Cr', '1.26 Cr', '1.45 Cr', '1.48 Cr', '1.53 Cr']
for i, (lbl, v) in enumerate(zip(labels3, users3)):
    ax.annotate(lbl, (i, v), textcoords='offset points',
                xytext=(0, 14), ha='center', fontsize=9, fontweight='bold', color=BLACK,
                bbox=dict(boxstyle='round,pad=0.25', facecolor=VLGRAY, edgecolor=LGRAY, alpha=0.8))

# 50x annotation
ax.annotate('50x growth\nin 38 months', xy=(4.5, 130), fontsize=9, color=MGRAY,
            fontweight='bold', ha='center', fontstyle='italic')

ax.set_xticks(range(len(dates3)))
ax.set_xticklabels(dates3, fontsize=8.5)
ax.set_ylabel('Registered Users (Lakhs)', fontsize=10)
ax.set_ylim(0, 180)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(LGRAY)
ax.spines['bottom'].set_color(LGRAY)

fig.suptitle('iGOT Karmayogi: National User Registration',
             fontsize=14, fontweight='bold', x=0.12, ha='left', y=0.98)
fig.text(0.12, 0.91, 'Mission Karmayogi civil services capacity building platform',
         fontsize=9, color=MGRAY, fontfamily='sans-serif')
add_source(fig, 'Source: Press Information Bureau — Jan 2023, May 2025, Jul 2025, Dec 2025, Feb 2026, Mar 2026 releases')
add_figure_label(fig, 'FIGURE 3')

fig.tight_layout(rect=[0.05, 0.06, 0.98, 0.88])
fig.savefig(os.path.join(OUT, 'fig3_igot_national.png'), dpi=300, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ Figure 3: iGOT National')


# ═══════════════════════════════════════════════════════════════
#  FIGURE 4: e-Office — Paper vs Digital Transition
#  Source: DARPG, PIB (2024)
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))

metrics = ['e-Files', 'e-Receipts']
electronic = [94, 95]
paper      = [6, 5]

x = np.arange(len(metrics))
w = 0.45

b1 = ax.bar(x, electronic, w, color=BLACK, edgecolor=BG, linewidth=1, label='Electronic', zorder=3)
b2 = ax.bar(x, paper, w, bottom=electronic, color=VLGRAY, edgecolor=LGRAY, linewidth=0.5, label='Paper', zorder=3)

for i, (e, p) in enumerate(zip(electronic, paper)):
    ax.text(i, e/2, f'{e}%', ha='center', va='center', fontsize=18, fontweight='bold', color=BG)
    ax.text(i, e + p/2, f'{p}%', ha='center', va='center', fontsize=11, color=MGRAY)

ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=12, fontweight='bold')
ax.set_ylim(0, 105)
ax.set_ylabel('')
ax.tick_params(axis='y', which='both', left=False, labelleft=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color(LGRAY)
ax.legend(loc='upper right', fontsize=9, framealpha=0.8, edgecolor=LGRAY)

# Additional context
ax.text(1.3, 50, '37 lakh files\nprocessed\n(2019–2024)', fontsize=8.5, color=MGRAY,
        ha='left', va='center', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=VLGRAY, edgecolor=LGRAY))

fig.suptitle('Central Secretariat: Digital File Processing Rate',
             fontsize=14, fontweight='bold', x=0.12, ha='left', y=0.98)
fig.text(0.12, 0.91, 'Percentage of files and receipts handled electronically via e-Office (2024)',
         fontsize=9, color=MGRAY, fontfamily='sans-serif')
add_source(fig, 'Source: DARPG, PIB — Secretariat Reforms Report, 2024')
add_figure_label(fig, 'FIGURE 4')

fig.tight_layout(rect=[0.05, 0.06, 0.98, 0.88])
fig.savefig(os.path.join(OUT, 'fig4_eoffice_rate.png'), dpi=300, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ Figure 4: e-Office Rate')


# ═══════════════════════════════════════════════════════════════
#  FIGURE 5: Madhya Pradesh iGOT — Users vs Enrollments
#  Source: PIB, Parliament reply, Mar 6 2026
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))

cats = ['Registered Users', 'Course Enrolments']
vals = [9.37, 42.79]  # in lakhs
colors5 = [DGRAY, BLACK]

bars = ax.barh(cats, vals, height=0.45, color=colors5, edgecolor=BG, linewidth=1, zorder=3)

for bar, v in zip(bars, vals):
    ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height()/2,
            f'{v:.2f} Lakh', va='center', fontsize=12, fontweight='bold', color=BLACK)

# Ratio annotation
ratio = 42.79 / 9.37
ax.text(25, 0.8, f'Ratio: {ratio:.1f}x\ncourses per user', fontsize=9, color=MGRAY,
        ha='center', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=VLGRAY, edgecolor=LGRAY))

ax.set_xlim(0, 55)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(LGRAY)
ax.spines['bottom'].set_color(LGRAY)
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)

fig.suptitle('Madhya Pradesh: iGOT Karmayogi Performance',
             fontsize=14, fontweight='bold', x=0.12, ha='left', y=0.98)
fig.text(0.12, 0.91, 'As of March 6, 2026  ·  9.37 lakh users with 42.79 lakh course enrolments',
         fontsize=9, color=MGRAY, fontfamily='sans-serif')
add_source(fig, 'Source: PIB — Parliament Written Reply, March 2026 (pib.gov.in)')
add_figure_label(fig, 'FIGURE 5')

fig.tight_layout(rect=[0.05, 0.06, 0.98, 0.88])
fig.savefig(os.path.join(OUT, 'fig5_mp_igot.png'), dpi=300, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ Figure 5: MP iGOT')


# ═══════════════════════════════════════════════════════════════
#  FIGURE 6: e-Office Efficiency — Transaction Delayering
#  Source: DARPG e-Office Analytics
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 4.5))

periods = ['2021', 'Jan 2024', 'Jun 2024', 'Dec 2024']
levels  = [7.19, 4.58, 4.19, 4.70]

ax.plot(range(len(periods)), levels, color=BLACK, linewidth=2.2, marker='s', markersize=7,
        markerfacecolor=BG, markeredgecolor=BLACK, markeredgewidth=2, zorder=5)

# Shade improvement zone
ax.axhspan(4.0, 5.0, alpha=0.06, color=BLACK)

for i, (p, v) in enumerate(zip(periods, levels)):
    ax.annotate(f'{v:.2f}', (i, v), textcoords='offset points',
                xytext=(0, 14), ha='center', fontsize=10, fontweight='bold', color=BLACK)

# improvement arrow
ax.annotate('', xy=(3, 4.70), xytext=(0, 7.19),
            arrowprops=dict(arrowstyle='->', color=LGRAY, lw=1.5, linestyle=':'))
pct_change = (7.19 - 4.70) / 7.19 * 100
ax.text(1.5, 6.3, f'{pct_change:.0f}% reduction\nin decision layers', fontsize=9, color=MGRAY,
        ha='center', fontweight='bold', fontstyle='italic')

ax.set_xticks(range(len(periods)))
ax.set_xticklabels(periods, fontsize=10)
ax.set_ylabel('Avg. Transaction Levels per File', fontsize=10)
ax.set_ylim(3.5, 8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(LGRAY)
ax.spines['bottom'].set_color(LGRAY)

fig.suptitle('e-Office Analytics: Bureaucratic Delayering',
             fontsize=14, fontweight='bold', x=0.12, ha='left', y=0.98)
fig.text(0.12, 0.91, 'Average distinct transaction levels per active file — lower = fewer approval layers',
         fontsize=9, color=MGRAY, fontfamily='sans-serif')
add_source(fig, 'Source: DARPG — e-Office Analytics Dashboard, Secretariat Reforms Monthly Reports')
add_figure_label(fig, 'FIGURE 6')

fig.tight_layout(rect=[0.05, 0.06, 0.98, 0.88])
fig.savefig(os.path.join(OUT, 'fig6_eoffice_delayering.png'), dpi=300, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ Figure 6: e-Office Delayering')


# ═══════════════════════════════════════════════════════════════
#  FIGURE 7: UTAUT Framework — Study Design Model
# ═══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Boxes
def draw_box(ax, x, y, w, h, text, bold=False, fill='#F5F5F5'):
    rect = plt.Rectangle((x, y), w, h, facecolor=fill, edgecolor=BLACK, linewidth=1.5, zorder=3)
    ax.add_patch(rect)
    fw = 'bold' if bold else 'normal'
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=8.5, fontweight=fw, color=BLACK, zorder=4)

# Independent Variables (left)
draw_box(ax, 0.3, 4.5, 2.8, 0.7, 'Performance Expectancy\n(PE)', bold=True)
draw_box(ax, 0.3, 3.4, 2.8, 0.7, 'Effort Expectancy\n(EE)', bold=True)
draw_box(ax, 0.3, 2.3, 2.8, 0.7, 'Social Influence\n(SI)', bold=True)
draw_box(ax, 0.3, 1.2, 2.8, 0.7, 'Facilitating Conditions\n(FC)', bold=True)

# Mediating
draw_box(ax, 4.2, 3.1, 2.2, 1.0, 'Behavioural\nIntention\nto Use', bold=True, fill='#E0E0E0')

# Dependent
draw_box(ax, 7.3, 3.1, 2.2, 1.0, 'Actual\nIT Tool\nUsage', bold=True, fill=BLACK)
ax.texts[-1].set_color(BG)

# Moderators (bottom)
draw_box(ax, 3.5, 0.2, 3.5, 0.6, 'Moderators: Age · Experience · Designation', fill='#FAFAFA')

# Arrows
arrow_props = dict(arrowstyle='->', color=DGRAY, lw=1.5)
ax.annotate('', xy=(4.2, 4.85), xytext=(3.1, 4.85), arrowprops=arrow_props)
ax.annotate('', xy=(4.2, 3.75), xytext=(3.1, 3.75), arrowprops=arrow_props)
ax.annotate('', xy=(4.2, 3.6),  xytext=(3.1, 2.65), arrowprops=arrow_props)
ax.annotate('', xy=(7.3, 1.55), xytext=(3.1, 1.55), arrowprops=arrow_props)
# intention -> usage
ax.annotate('', xy=(7.3, 3.6), xytext=(6.4, 3.6), arrowprops=arrow_props)
# PE arrow goes to intention box top
# moderators arrow up
ax.annotate('', xy=(5.3, 3.1), xytext=(5.3, 0.8),
            arrowprops=dict(arrowstyle='->', color=LGRAY, lw=1, linestyle='--'))

fig.suptitle('UTAUT Framework: Study Design Model',
             fontsize=14, fontweight='bold', x=0.12, ha='left', y=0.98)
fig.text(0.12, 0.93, 'Adapted from Venkatesh, Morris, Davis & Davis (2003), MIS Quarterly 27(3), 425–478',
         fontsize=8.5, color=MGRAY, fontfamily='sans-serif')
add_figure_label(fig, 'FIGURE 7')

fig.tight_layout(rect=[0.02, 0.02, 0.98, 0.90])
fig.savefig(os.path.join(OUT, 'fig7_utaut_model.png'), dpi=300, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print('✅ Figure 7: UTAUT Model')


print(f'\n🎉 All 7 figures saved to: {OUT}')
print('\nData Sources Used:')
print('  • UN DESA E-Government Survey (2014–2024)')
print('  • TRAI Annual Performance Indicators')
print('  • PIB releases: Jan 2023, May/Jul/Dec 2025, Feb/Mar 2026')
print('  • DARPG e-Office Analytics & Secretariat Reforms Reports')
print('  • Venkatesh et al. (2003), MIS Quarterly')
