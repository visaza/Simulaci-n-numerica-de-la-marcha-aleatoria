import numpy as np
import matplotlib.pyplot as plt
from numba import njit


@njit
def caminata_unidimensional(n_pasos: int, salto: float = 1.0) -> float:
    """
    Simula una caminata aleatoria en una dimensión.
    En cada iteración se suma +salto o -salto con igual probabilidad.
    
    Parámetros
    ----------
    n_pasos : int
        Número de pasos de la caminata.
    salto : float, opcional
        Tamaño de cada incremento (por defecto = 1.0).
    
    Retorna
    -------
    float
        Posición final después de n_pasos.
    """
    posicion = 0.0
    for _ in range(n_pasos):
        direccion = 2 * np.random.randint(0, 2) - 1  # -1 o +1
        posicion += salto * direccion
    return posicion


# --------------------------- Configuración inicial ----------------------------
num_pasos_global = 10000   # número de pasos en la simulación "grande"
num_replicas     = 80000   # número de realizaciones para estadística
delta            = 1.0     # tamaño del paso
dt               = 1.0     # intervalo temporal por paso
semilla          = 123     # para reproducibilidad
generador        = np.random.default_rng(semilla)

# ==================== (1) Una sola caminata con N pasos =======================
N_usuario = int(input("Ingrese un número de pasos (entero positivo): "))
posicion_final = caminata_unidimensional(N_usuario, salto=delta)

print("\n--- Ejemplo: una caminata ---")
print(f"N = {N_usuario}, salto = {delta}")
print(f"Posición final tras N pasos: {posicion_final:.4f}")

# ================= (2) Distribución de posiciones finales =====================
# Generar múltiples caminatas de N fijo (num_pasos_global)
trayectorias = generador.choice((-delta, delta), size=(num_replicas, num_pasos_global))
pos_finales = trayectorias.sum(axis=1)

media_emp = pos_finales.mean()
var_emp   = pos_finales.var(ddof=1)
desv_emp  = np.sqrt(var_emp)
desv_teo  = np.sqrt(num_pasos_global) * delta  # predicción por TCL

print("\n--- Comparación con Teorema Central del Límite ---")
print(f"Cantidad de simulaciones: {num_replicas}")
print(f"<x> ≈ {media_emp:.5f}")
print(f"Var[x] ≈ {var_emp:.5f}")
print(f"Desv.est. simulada  = {desv_emp:.5f}")
print(f"Desv.est. teórica   = {desv_teo:.5f}")

# Error relativo
err_std = abs(desv_emp - desv_teo) / desv_teo * 100
err_var = abs(var_emp - num_pasos_global * delta**2) / (num_pasos_global * delta**2) * 100

print("\nErrores relativos:")
print(f"Desviación estándar: {err_std:.3f}%")
print(f"Varianza:            {err_var:.3f}%")

# Histograma y gaussiana teórica
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(pos_finales, bins=50, density=True, alpha=0.6, color="skyblue", label="Simulación")

x_axis = np.linspace(pos_finales.min(), pos_finales.max(), 800)
gauss_teo = (1.0 / (np.sqrt(2*np.pi) * desv_teo)) * np.exp(-(x_axis**2) / (2 * desv_teo**2))
ax.plot(x_axis, gauss_teo, 'r-', lw=2, label="TCL (gaussiana)")

ax.set_xlabel("Posición final")
ax.set_ylabel("Probabilidad")
ax.set_title(f"Caminata 1D: N={num_pasos_global}, repeticiones={num_replicas}")
ax.legend()
plt.tight_layout()
plt.show()

# ================== (3) Relación varianza <x²> vs número de pasos =============

def generar_muestras(num_pasos: int, repeticiones: int, salto: float = 1.0, rng=None) -> np.ndarray:
    """
    Ejecuta múltiples caminatas y retorna el vector de posiciones finales.
    """
    if rng is None:
        rng = np.random.default_rng()
    pasos = rng.choice((-salto, salto), size=(repeticiones, num_pasos))
    return pasos.sum(axis=1)


ensayos = 15000
lista_N = [40, 80, 200, 400, 800, 1600, 3000]

medias = []
varianzas = []

for n in lista_N:
    resultados = generar_muestras(n, ensayos, salto=delta, rng=generador)
    medias.append(resultados.mean())
    varianzas.append(resultados.var(ddof=1))

N_array   = np.array(lista_N, dtype=float)
var_array = np.array(varianzas, dtype=float)

# Ajuste lineal: Var[x] = pendiente * N + ordenada
pendiente, ordenada = np.polyfit(N_array, var_array, 1)

# Estimación de la constante de difusión
D_calc = pendiente / (2.0 * dt)
D_teo  = (delta**2) / (2.0 * dt)

# R^2 del ajuste
ajuste = pendiente * N_array + ordenada
ss_res = np.sum((var_array - ajuste)**2)
ss_tot = np.sum((var_array - var_array.mean())**2)
R2 = 1 - ss_res/ss_tot

print("\n--- Varianza vs número de pasos ---")
for n, m, v in zip(lista_N, medias, var_array):
    print(f"N={n:5d}  <x>={m: .5f}   Var[x]={v: .5f}")

print("\nAjuste lineal Var[x] ≈ pendiente * N + ordenada")
print(f"pendiente  = {pendiente:.5f}   (teórico ≈ {delta**2:.5f})")
print(f"ordenada   = {ordenada:.5f}")
print(f"R^2        = {R2:.5f}")

print("\nConstante de difusión:")
print(f"D calculada = {D_calc:.5f}")
print(f"D teórica   = {D_teo:.5f}")

# Gráfico de la varianza vs N
plt.figure(figsize=(7, 4))
plt.plot(N_array, var_array, 'o', label="Simulación")
plt.plot(N_array, ajuste, '-', label="Ajuste lineal")
plt.xlabel("Número de pasos (N)")
plt.ylabel("Var[x]")
plt.title(f"Relación Var[x] vs N (ensayos={ensayos})")
plt.legend()
plt.tight_layout()
plt.show()
