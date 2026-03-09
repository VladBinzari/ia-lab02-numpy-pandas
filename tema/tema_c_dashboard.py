import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid', palette='muted')

tips = sns.load_dataset('tips')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Dashboard Vizualizare — Dataset Tips', fontsize=16, fontweight='bold')

# --- Subplot 1: Scatter (Matplotlib) — total_bill vs. tip, colorat după sex ---
culori = {'Male': '#3498db', 'Female': '#e74c3c'}
for sex, culoare in culori.items():
    subset = tips[tips['sex'] == sex]
    axes[0, 0].scatter(subset['total_bill'], subset['tip'],
                       label=sex, color=culoare, alpha=0.6, s=60)
axes[0, 0].set_title('Total factură vs. Bacșiș (per sex)')
axes[0, 0].set_xlabel('Total factură ($)')
axes[0, 0].set_ylabel('Bacșiș ($)')
axes[0, 0].legend(title='Sex')
axes[0, 0].grid(True, alpha=0.3)

# --- Subplot 2: Boxplot (Seaborn) — total_bill per day, ordinea Thur→Sun ---
ordinea_zile = ['Thur', 'Fri', 'Sat', 'Sun']
sns.boxplot(data=tips, x='day', y='total_bill',
            order=ordinea_zile, ax=axes[0, 1])
axes[0, 1].set_title('Distribuția facturii totale per zi')
axes[0, 1].set_xlabel('Zi')
axes[0, 1].set_ylabel('Total factură ($)')

# --- Subplot 3: Histogramă (Seaborn histplot) — distribuția tip, hue=time + KDE ---
sns.histplot(data=tips, x='tip', hue='time',
             kde=True, bins=15, ax=axes[1, 0])
axes[1, 0].set_title('Distribuția bacșișului (Lunch vs. Dinner)')
axes[1, 0].set_xlabel('Bacșiș ($)')
axes[1, 0].set_ylabel('Frecvență')

# --- Subplot 4: Barplot (Seaborn) — bacșișul mediu per day, Thur→Sun ---
sns.barplot(data=tips, x='day', y='tip',
            order=ordinea_zile, errorbar='ci',
            palette='Blues_d', ax=axes[1, 1])
axes[1, 1].set_title('Bacșiș mediu per zi (cu interval de încredere)')
axes[1, 1].set_xlabel('Zi')
axes[1, 1].set_ylabel('Bacșiș mediu ($)')

plt.tight_layout()
plt.savefig('tema_c_dashboard_tips.png', dpi=150, bbox_inches='tight')
plt.show()
print("Dashboard salvat ca 'tema_c_dashboard_tips.png'.")
