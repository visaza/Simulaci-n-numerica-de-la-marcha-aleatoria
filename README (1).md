# Simulación de Marcha Aleatoria 1D

Este repositorio contiene un programa en Python que simula **marchas aleatorias unidimensionales** 
y estudia sus propiedades estadísticas, verificando el **Teorema Central del Límite (TCL)** 
y el crecimiento lineal de la varianza con el número de pasos.

---

## 🚀 Requisitos

Antes de correr el programa, asegúrate de tener instalado Python 3 y las siguientes librerías:

```bash
pip install numpy matplotlib scipy
```

---

## ▶️ Cómo correr el programa

Ejecuta el script principal desde la terminal:

```bash
python random_walk.py
```

---

## 🖥️ Interacción con el programa

El script pedirá por consola:

```
Ingresa un número entero correspondiente al número de pasos:
```

👉 Escribe un entero positivo (ejemplo: `12000`) y presiona Enter.

---

## 📊 Qué sucede a continuación

### 1. Caminata única (N usuario)
- Simula una única realización de la caminata aleatoria.
- Muestra en consola la posición final.

### 2. Histograma vs TCL (N grande y muchas muestras)
- Ejecuta `n_samples` caminatas independientes.
- Genera un histograma de posiciones finales.
- Superpone la curva **Gaussiana teórica**.
- Reporta estadísticas y compara con el **Teorema Central del Límite**.

### 3. Varianza vs N y constante de difusión
- Simula la caminata para varios valores de N.
- Calcula **Var[x]** y ajusta una recta para comprobar el crecimiento lineal.
- Estima:
  - La pendiente del ajuste.
  - El coeficiente de determinación **R²**.
  - La constante de difusión **D_est**.
- Compara **D_est** con el valor teórico **D_teo**.
- Genera la gráfica de **varianza vs pasos**.

---

## 📂 Estructura del repositorio

```
📁 random-walk-1d
│── random_walk.py    # Código principal de la simulación
│── README.md         # Instrucciones y explicación del proyecto
```

---

## ✨ Resultados esperados

1. La distribución de posiciones finales tiende a una **Gaussiana** al aumentar el número de pasos (TCL).  
2. La **varianza crece linealmente con N**, confirmando la relación con el coeficiente de difusión.  

---

## 👩‍💻 Autor

Este código fue desarrollado para la simulación y análisis de **marchas aleatorias 1D** 
en el contexto de un proyecto académico de Física/Matemáticas Computacionales.
