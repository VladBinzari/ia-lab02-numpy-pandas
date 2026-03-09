import pandas as pd
import seaborn as sns

# Încărcăm dataset-ul Tips
tips = sns.load_dataset('tips')

# 1. Dimensiune, tipuri de date și statistici descriptive
print("=== Informații generale ===")
print(f"Dimensiune: {tips.shape[0]} linii × {tips.shape[1]} coloane")
print(f"\nTipuri de date:\n{tips.dtypes}")
print(f"\nValori lipsă:\n{tips.isnull().sum()}")
print("\n=== Statistici descriptive ===")
print(tips.describe().round(2))

# 2. Bacșișul mediu per zi a săptămânii și per sex
print("\n=== Bacșișul mediu per zi a săptămânii ===")
bacsis_per_zi = tips.groupby('day', observed=True)['tip'].mean().round(3)
print(bacsis_per_zi)

print("\n=== Bacșișul mediu per sex ===")
bacsis_per_sex = tips.groupby('sex', observed=True)['tip'].mean().round(3)
print(bacsis_per_sex)

# 3. Coloană nouă procent_bacsis (lucrăm pe o copie)
tips_extins = tips.copy()
tips_extins['procent_bacsis'] = (tips_extins['tip'] / tips_extins['total_bill'] * 100).round(2)

print("\n=== Primele 5 rânduri cu procent_bacsis ===")
print(tips_extins[['total_bill', 'tip', 'procent_bacsis']].head())

# 4. Cele mai generoase 5 mese (cel mai mare procent_bacsis)
print("\n=== Top 5 cele mai generoase mese ===")
top5 = tips_extins.nlargest(5, 'procent_bacsis')[['total_bill', 'tip', 'procent_bacsis', 'day', 'sex']]
print(top5.to_string(index=False))

# 5. Numărul de mese per zi și per fumător
print("\n=== Numărul de mese per zi și per fumător ===")
mese_zi_fumator = tips.groupby(['day', 'smoker'], observed=True).size().reset_index(name='numar_mese')
print(mese_zi_fumator.to_string(index=False))
