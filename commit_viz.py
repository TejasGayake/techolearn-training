import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
import numpy as np

commits = [
    "2026-01-29", "2026-01-31",
    "2026-02-01", "2026-02-03", "2026-02-04", "2026-02-05",
    "2026-02-06", "2026-02-06", "2026-02-07", "2026-02-08", "2026-02-08",
    "2026-02-09", "2026-02-10", "2026-02-11", "2026-02-12", "2026-02-13",
    "2026-02-14", "2026-02-16", "2026-02-17", "2026-02-18", "2026-02-19",
    "2026-02-20", "2026-02-20", "2026-02-22", "2026-02-23", "2026-02-26",
    "2026-02-27", "2026-02-27", "2026-02-28",
    "2026-03-02", "2026-03-05", "2026-03-05", "2026-03-06", "2026-03-06",
    "2026-03-08", "2026-03-12", "2026-03-17", "2026-03-17", "2026-03-18",
    "2026-03-19", "2026-03-22", "2026-03-25", "2026-03-26",
    "2026-03-28", "2026-03-28", "2026-03-29", "2026-03-30",
    "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-05", "2026-04-07",
    "2026-04-08", "2026-04-08", "2026-04-08", "2026-04-10", "2026-04-15",
    "2026-04-18", "2026-04-18", "2026-04-22", "2026-04-25", "2026-04-28",
    "2026-04-29", "2026-04-29", "2026-04-29", "2026-04-29",
    "2026-05-03", "2026-05-06", "2026-05-07", "2026-05-08", "2026-05-12",
    "2026-05-15", "2026-05-18", "2026-05-19", "2026-05-20",
    "2026-05-21", "2026-05-21", "2026-05-22", "2026-05-23",
]

from collections import Counter
counts = Counter(commits)

start = datetime(2026, 1, 27)
end = datetime(2026, 5, 24)
all_days = []
d = start
while d <= end:
    all_days.append(d)
    d += timedelta(days=1)

intensity = {}
for day in all_days:
    key = day.strftime("%Y-%m-%d")
    c = counts.get(key, 0)
    intensity[key] = min(c, 4)

weeks = []
current_week = []
for day in all_days:
    current_week.append(day)
    if len(current_week) == 7:
        weeks.append(current_week)
        current_week = []
if current_week:
    weeks.append(current_week)

# Pad first week
if len(weeks[0]) < 7:
    pad_count = 7 - len(weeks[0])
    weeks[0] = [None] * pad_count + weeks[0]

fig, ax = plt.subplots(figsize=(16, 3.5))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

colors = ['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353']

month_labels = []
month_starts = []
prev_month = None
for wi, week in enumerate(weeks):
    for di, day in enumerate(week):
        if day is None:
            continue
        key = day.strftime("%Y-%m-%d")
        c = intensity.get(key, 0)
        rect = plt.Rectangle((wi * 14, di * 14), 12, 12,
                             facecolor=colors[c], edgecolor='none')
        ax.add_patch(rect)
        if prev_month != day.month:
            month_labels.append((wi, day.strftime("%b")))
            month_starts.append(wi)
            prev_month = day.month

# Month labels
for wi, label in month_labels:
    ax.text(wi * 14 + 6, -8, label, fontsize=9, color='#8b949e',
            ha='center', va='bottom', fontfamily='monospace')

# Day labels
for di, label in enumerate(['Mon', '', 'Wed', '', 'Fri', '', '']):
    ax.text(-20, di * 14 + 6, label, fontsize=8, color='#8b949e',
            ha='right', va='center', fontfamily='monospace')

# Legend
legend_x = len(weeks) * 14 - 120
legend_y = 7 * 14 + 20
ax.text(0, legend_y + 12, 'Less', fontsize=8, color='#8b949e',
        ha='left', fontfamily='monospace')
for i in range(5):
    rect = plt.Rectangle((legend_x + i * 18, legend_y), 12, 12,
                         facecolor=colors[i], edgecolor='none')
    ax.add_patch(rect)
ax.text(legend_x + 5 * 18 + 4, legend_y + 2, 'More', fontsize=8, color='#8b949e',
        ha='left', fontfamily='monospace')

# Total box
total_commits = len(commits)
total_days = len(set(commits))
ax.text(0, 7 * 14 + 20,
        f'{total_commits} commits in 5 months  •  {total_days} unique days',
        fontsize=11, color='#c9d1d9', fontfamily='monospace')

ax.set_xlim(-30, len(weeks) * 14 + 30)
ax.set_ylim(-20, 7 * 14 + 40)
ax.axis('off')

plt.savefig("G:\\technolearn_training\\TecholearnLearnTraining\\commit_calendar.png",
            dpi=200, bbox_inches='tight', facecolor='#0d1117')
plt.close()
print(f"Done. {total_commits} commits, {total_days} unique days")
