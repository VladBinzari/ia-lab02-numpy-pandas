import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid', palette='Set2')

iris = sns.load_dataset('iris')

# 1. Pairplot complet cu hue='species' și diag_kind='kde'
pairplot_fig = sns.pairplot(iris, hue='species', diag_kind='kde',
                             plot_kws={'alpha': 0.6})
plt.suptitle('Pairplot — Dataset Iris (per specie)', y=1.02, fontsize=14, fontweight='bold')
plt.savefig('tema_d_pairplot_iris.png', dpi=150, bbox_inches='tight')
plt.show()
print("Pairplot salvat ca 'tema_d_pairplot_iris.png'.")

# 2. Figură separată cu 4 violinplot-uri (1×4), câte unul per variabilă numerică
variabile = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
etichete = ['Lungime sepală (cm)', 'Lățime sepală (cm)',
            'Lungime petală (cm)', 'Lățime petală (cm)']

fig, axes = plt.subplots(1, 4, figsize=(18, 6))
fig.suptitle('Violinplot per variabilă numerică — Dataset Iris',
             fontsize=14, fontweight='bold')

for ax, var, eticheta in zip(axes, variabile, etichete):
    sns.violinplot(data=iris, x='species', y=var,
                   inner='quart', split=False, ax=ax)
    ax.set_title(eticheta)
    ax.set_xlabel('Specie')
    ax.set_ylabel(eticheta)
    ax.tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.savefig('tema_d_violinplots_iris.png', dpi=150, bbox_inches='tight')
plt.show()
print("Violinplot-uri salvate ca 'tema_d_violinplots_iris.png'.")
