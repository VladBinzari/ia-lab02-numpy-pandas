import numpy as np

# Setăm seed-ul pentru reproductibilitate
np.random.seed(42)

# 1. Generarea matricelor A (4x3) și B (3x5) cu valori întregi între 1 și 10
A = np.random.randint(1, 11, size=(4, 3))
B = np.random.randint(1, 11, size=(3, 5))

print("=== Matricea A (4×3) ===")
print(A)

print("\n=== Matricea B (3×5) ===")
print(B)

# 2. Produsul matriceal C = A @ B
C = A @ B

print("\n=== Produsul matriceal C = A @ B (4×5) ===")
print(C)

# 3. Statistici pe matricea C
print("\n=== Statistici pe C ===")
print(f"Suma tuturor elementelor din C: {np.sum(C)}")
print(f"Media pe fiecare coloană (axis=0): {np.mean(C, axis=0).round(2)}")
print(f"Valoarea maximă globală: {np.max(C)}")

# 4. (Bonus) Matrice pătratică M (3×3) — inversă și determinant
print("\n=== (Bonus) Matrice pătratică M (3×3) ===")
# Generăm o matrice cu determinant nenul (invertibilă)
M = np.random.randint(1, 10, size=(3, 3)).astype(float)
print(f"M =\n{M}")

det = np.linalg.det(M)
print(f"\nDeterminantul lui M: {det:.4f}")

if abs(det) < 1e-10:
    print("Matricea M este singulară (determinant ≈ 0) — nu poate fi inversată.")
else:
    M_inv = np.linalg.inv(M)
    print(f"\nInversa lui M:\n{M_inv.round(4)}")

    # Verificare: M @ M_inv ≈ I
    produs = M @ M_inv
    este_identitate = np.allclose(produs, np.eye(3))
    print(f"\nM @ inv(M) ≈ I (matrice identitate)? {este_identitate}")
    print(f"M @ inv(M) =\n{produs.round(6)}")
