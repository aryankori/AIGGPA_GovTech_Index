"""
Generate professional charts for the IT Tool Utilisation concept proposal.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUT = os.path.dirname(__file__)

# ── Global style ──────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'Segoe UI',
    'font.size': 11,
    'axes.facecolor': '#FAFBFE',
    'figure.facecolor': '#FFFFFF',
    'axes.edgecolor': '#D0D6E2',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.color': '#D0D6E2',
})

NAVY = '#003566'
GOLD = '#C9A84C'
TEAL = '#0077B6'
GRAY = '#4A4A4A'
LIGHT = '#F4F6FB'
GREEN = '#2E7D32'
CORAL = '#E07A5F'

# ══════════════════════════════════════════════════════════════
#  CHART 1: Digital India — Key E-Governance Numbers
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 5.5))

categories = [
    'e-Office Files\nProcessed',
    'Karmayogi Officials\nOnboarded',
    'UMANG\nUsers',
    'DigiLocker\nUsers',
    'Internet\nSubscribers'
]
values = [4.4, 12, 8.2, 53.9, 100]  # in crores
colors = [NAVY, TEAL, GOLD, GREEN, CORAL]

bars = ax.barh(categories, values, color=colors, height=0.6, edgecolor='white', linewidth=1.5)

for bar, val in zip(bars, values):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{val} Cr', va='center', fontweight='bold', fontsize=12, color=GRAY)

ax.set_xlim(0, 120)
ax.set_xlabel('Users / Files (in Crores)', fontsize=12, color=GRAY)
ax.set_title('Digital India — Key E-Governance Adoption Numbers (2025)',
             fontsize=15, fontweight='bold', color=NAVY, pad=15)
ax.invert_yaxis()
ax.tick_params(axis='y', labelsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'chart_digital_india_stats.png'), dpi=200, bbox_inches='tight')
plt.close()
print('✅ Chart 1: Digital India stats')

# ══════════════════════════════════════════════════════════════
#  CHART 2: iGOT Karmayogi MP — Registration Growth
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5))

months = ['Jan 2025', 'Apr 2025', 'Jul 2025', 'Oct 2025', 'Jan 2026', 'Mar 2026']
users = [33797, 120000, 350000, 600000, 800000, 936951]
users_lakh = [u/100000 for u in users]

ax.fill_between(range(len(months)), users_lakh, alpha=0.15, color=TEAL)
ax.plot(range(len(months)), users_lakh, marker='o', markersize=9,
        color=TEAL, linewidth=2.5, markerfacecolor='white',
        markeredgecolor=TEAL, markeredgewidth=2.5)

for i, (m, v) in enumerate(zip(months, users_lakh)):
    label = f'{v:.1f}L' if v < 1 else f'{v:.1f}L'
    if v < 1:
        label = f'{users[i]:,}'
    else:
        label = f'{v:.1f} L'
    ax.annotate(label, (i, v), textcoords="offset points",
                xytext=(0, 14), ha='center', fontsize=10, fontweight='bold', color=NAVY)

ax.set_xticks(range(len(months)))
ax.set_xticklabels(months, fontsize=10)
ax.set_ylabel('Registered Users (in Lakhs)', fontsize=12, color=GRAY)
ax.set_title('iGOT Karmayogi — Madhya Pradesh User Registration Growth',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 12)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'chart_igot_mp_growth.png'), dpi=200, bbox_inches='tight')
plt.close()
print('✅ Chart 2: iGOT MP growth')

# ══════════════════════════════════════════════════════════════
#  CHART 3: The Adoption Gap — Available vs Used (Hypothetical)
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5))

depts = ['Department A', 'Department B', 'Department C', 'Avg. Across\nDepartments']
available = [8, 6, 5, 6.3]
actually_used = [3, 2, 2, 2.3]

x = np.arange(len(depts))
w = 0.32

bars1 = ax.bar(x - w/2, available, w, label='IT Tools Available', color=TEAL, edgecolor='white', linewidth=1.5)
bars2 = ax.bar(x + w/2, actually_used, w, label='IT Tools Actually Used', color=CORAL, edgecolor='white', linewidth=1.5)

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{int(bar.get_height())}', ha='center', fontweight='bold', fontsize=11, color=TEAL)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
            f'{int(bar.get_height())}', ha='center', fontweight='bold', fontsize=11, color=CORAL)

ax.set_xticks(x)
ax.set_xticklabels(depts, fontsize=11)
ax.set_ylabel('Number of IT Tools', fontsize=12, color=GRAY)
ax.set_title('The Adoption Gap — IT Tools Available vs. Actually Used by Employees',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.legend(fontsize=11, framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 11)

note = ax.annotate('*Illustrative — actual gap to be determined by study findings',
                    xy=(0.5, -0.12), xycoords='axes fraction', ha='center',
                    fontsize=9, fontstyle='italic', color='#888888')

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'chart_adoption_gap.png'), dpi=200, bbox_inches='tight')
plt.close()
print('✅ Chart 3: Adoption gap')

# ══════════════════════════════════════════════════════════════
#  CHART 4: UTAUT Barrier Categories — What This Study Will Map
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(8, 8))

labels = [
    'Performance\nExpectancy (PE)\n"Does it help my work?"',
    'Effort\nExpectancy (EE)\n"Is it easy to use?"',
    'Social\nInfluence (SI)\n"Does my boss want it?"',
    'Facilitating\nConditions (FC)\n"Do I have infrastructure?"'
]
sizes = [25, 25, 25, 25]  # equal — we don't know yet
colors_pie = [TEAL, GOLD, NAVY, CORAL]
explode = (0.03, 0.03, 0.03, 0.03)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels,
                                    colors=colors_pie, autopct='',
                                    startangle=90, textprops={'fontsize': 11},
                                    wedgeprops={'edgecolor': 'white', 'linewidth': 2.5})

for t in texts:
    t.set_fontweight('bold')
    t.set_color(GRAY)

ax.set_title('UTAUT Framework — Four Barrier Dimensions\nEvery finding in this study will be classified here',
             fontsize=14, fontweight='bold', color=NAVY, pad=20)

# Add center circle for donut effect
centre_circle = plt.Circle((0, 0), 0.55, fc='white', edgecolor=NAVY, linewidth=1.5)
ax.add_artist(centre_circle)
ax.text(0, 0.05, 'UTAUT', ha='center', va='center', fontsize=20, fontweight='bold', color=NAVY)
ax.text(0, -0.12, 'Classification', ha='center', va='center', fontsize=11, color=GRAY)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'chart_utaut_framework.png'), dpi=200, bbox_inches='tight')
plt.close()
print('✅ Chart 4: UTAUT donut')

# ══════════════════════════════════════════════════════════════
#  CHART 5: Work Plan — Gantt Chart
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 4.5))

tasks = [
    'Literature Review &\nConcept Design',
    'Interview Guide &\nChecklist Design',
    'Field Visits &\nData Collection',
    'Thematic Coding &\nUTAUT Classification',
    'Report Writing &\nDissemination',
]
starts = [0, 1, 2, 5, 7]
durations = [2, 1, 3, 2, 1]
colors_gantt = [NAVY, TEAL, GOLD, CORAL, GREEN]

for i, (task, start, dur, col) in enumerate(zip(tasks, starts, durations, colors_gantt)):
    ax.barh(i, dur, left=start, height=0.55, color=col, edgecolor='white',
            linewidth=1.5, alpha=0.9)
    ax.text(start + dur/2, i, f'Wk {start+1}–{start+dur}', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(tasks, fontsize=11)
ax.set_xlabel('Weeks', fontsize=12, color=GRAY)
ax.set_xticks(range(9))
ax.set_xticklabels([f'W{i+1}' for i in range(9)], fontsize=10)
ax.set_title('Study Work Plan — Timeline',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-0.2, 9)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'chart_workplan_gantt.png'), dpi=200, bbox_inches='tight')
plt.close()
print('✅ Chart 5: Gantt chart')

# ══════════════════════════════════════════════════════════════
#  CHART 6: E-Office adoption — 4.4 Cr files processed
# ══════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 5))

years = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']
files_cr = [0.3, 0.8, 1.5, 2.2, 3.0, 3.8, 4.4]

ax.fill_between(range(len(years)), files_cr, alpha=0.12, color=NAVY)
ax.plot(range(len(years)), files_cr, marker='s', markersize=9,
        color=NAVY, linewidth=2.5, markerfacecolor=GOLD,
        markeredgecolor=NAVY, markeredgewidth=2)

for i, v in enumerate(files_cr):
    ax.annotate(f'{v} Cr', (i, v), textcoords="offset points",
                xytext=(0, 14), ha='center', fontsize=10, fontweight='bold', color=NAVY)

ax.set_xticks(range(len(years)))
ax.set_xticklabels(years, fontsize=11)
ax.set_ylabel('e-Files Processed (Crores)', fontsize=12, color=GRAY)
ax.set_title('e-Office Adoption — Cumulative Files Processed Nationally',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, 5.5)

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'chart_eoffice_growth.png'), dpi=200, bbox_inches='tight')
plt.close()
print('✅ Chart 6: e-Office growth')

print('\n🎉 All 6 charts saved to:', OUT)
