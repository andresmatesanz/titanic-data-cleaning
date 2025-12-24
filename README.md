# Proyecto Titanic – Limpieza y Análisis de Datos con Pandas

Este proyecto forma parte del Bootcamp de Data Science y tiene como objetivo realizar un **análisis y limpieza exhaustiva del dataset del Titanic**, preparando los datos para análisis más avanzados y modelado posterior.

---

## 🔹 Objetivos

1. Comprobar y manejar valores nulos en el dataset.
2. Limpiar columnas de texto y estandarizar nombres de columnas.
3. Filtrar y categorizar datos según edad y tarifa.
4. Crear nuevas columnas calculadas:
   - `Categoria_Edad`  
   - `Fare_Rank`  
   - `Puntuación` de cada pasajero
   - `Indice_Sobrevivencia` y clasificación asociada
5. Identificar patrones y posibles insights sobre la supervivencia de los pasajeros.

---

## 🔹 Contenido del proyecto

- **Notebook:** `notebooks/titanic_cleaning.ipynb`  
  Contiene todo el análisis paso a paso, con comentarios y visualizaciones intermedias.

- **Script Python:** `scripts/titanic_cleaning.py`  
  Permite ejecutar todo el proceso de limpieza y cálculo de puntuaciones de manera automática.

- **Dataset:** `data/titanic.csv`  
  Dataset original usado para el análisis.

---

## 🔹 Tecnologías y librerías usadas

- Python 3.x
- pandas
- numpy
- regex (re)
- Jupyter Notebook (opcional para visualización paso a paso)

Instalación rápida de dependencias:

```bash
pip install -r requirements.txt
