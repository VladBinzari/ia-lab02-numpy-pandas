# Laborator 02 — NumPy, Pandas, Matplotlib, Seaborn

Proiect realizat in cadrul cursului **Inteligenta Artificiala 2025-2026**.

## Descriere

Analiza exploratorie a datelor (EDA) folosind cele 4 biblioteci standard Python:
- **NumPy** — calcul numeric pe array-uri
- **Pandas** — manipularea datelor tabelare
- **Matplotlib** — grafice de baza
- **Seaborn** — vizualizari statistice

## Structura proiectului

```
lab02/
├── requirements.txt
├── cerinta_3_1_numpy.py       # Array-uri si operatii NumPy
├── cerinta_3_2_pandas.py      # Explorarea dataset-ului Iris cu Pandas
├── cerinta_3_3_matplotlib.py  # Grafice de baza cu Matplotlib
├── cerinta_3_4_seaborn.py     # Distributii cu Seaborn
├── cerinta_3_5_heatmap.py     # Heatmap de corelatie
├── cerinta_3_6_titanic.py     # Analiza dataset-ului Titanic
└── tema/
    ├── tema_a_numpy.py        # Operatii matriceale NumPy
    ├── tema_b_tips.py         # Analiza dataset Tips cu Pandas
    ├── tema_c_dashboard.py    # Dashboard vizualizare Tips
    ├── tema_d_bonus_iris.py   # Raport comparativ Iris
    └── tema_e_colab.ipynb     # Notebook Google Colab — Titanic
```

## Instalare

```bash
# Creare mediu virtual
python -m venv .venv

# Activare (Windows)
.venv\Scripts\activate

# Instalare dependente
pip install -r requirements.txt
```

## Rulare

```bash
python cerinta_3_1_numpy.py
python cerinta_3_2_pandas.py
python cerinta_3_3_matplotlib.py
python cerinta_3_4_seaborn.py
python cerinta_3_5_heatmap.py
python cerinta_3_6_titanic.py
```

Fisierul `tema_e_colab.ipynb` se ruleaza in [Google Colab](https://colab.research.google.com).

## Dataset-uri folosite

| Dataset | Sursa | Descriere |
|---------|-------|-----------|
| Iris | seaborn | 150 flori, 3 specii, 4 masuratori |
| Tips | seaborn | 244 mese restaurant, bacsis si factura |
| Titanic | seaborn | 891 pasageri, date despre supravietuire |
