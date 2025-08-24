# Simulación de marcha aleatoria 1D

Este repositorio contiene un script (random_walk.py) para simular marchas aleatorias unidimensionales
con pasos ±1 equiprobables.

Archivos generados en este experimento (en /mnt/data/random_walk_outputs):
- histogram_N500_T10000.png  : histograma y comparación con la gaussiana (TCL)
- mean2_vs_N_fit.png                  : gráfico de <x^2> vs N con ajuste lineal
- table_N_mean_mean2.csv              : tabla con N, <x>, <x^2>
- summary.txt                         : resumen numérico (slope y D estimado)

Uso del script (random_walk.py):

# Histograma para una N dada:
python random_walk.py --N 500 --trials 10000 --mode histogram --outdir outputs

# Batch (varios N) para obtener <x> y <x^2>:
python random_walk.py --mode batch --trials 5000 --outdir outputs

# Si desea fijar semilla:
python random_walk.py --N 100 --trials 10000 --seed 42 --mode histogram

Subir a GitHub:
1. Cree un repositorio nuevo en GitHub.
2. Añada random_walk.py y este README.md al repositorio.
3. Commit y push:
   git init
   git add random_walk.py README.md
   git commit -m "Simulación marcha aleatoria 1D"
   git branch -M main
   git remote add origin <URL_DEL_REPOSITORIO>
   git push -u origin main

Explicación breve:
- Cada paso toma valor +1 o -1 con probabilidad 1/2. La posición final es suma de N pasos.
- Varianza por paso = 1; por lo tanto varianza total = N. El Teorema Central del Límite predice que para N grande
  la distribución de la suma tiende a una gaussiana con media 0 y varianza N.
- La constante de difusión D se define por la relación <x^2> = 2 D t (si tomamos t = N). Para el pase ±1, se obtiene D = 1/2.