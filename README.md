# Titanic Data Cleaning & Feature Engineering

Este proyecto realiza un proceso completo de **análisis, limpieza y transformación de datos** sobre el dataset del Titanic utilizando **Python y pandas**.

El objetivo principal es preparar un DataFrame limpio y estructurado para análisis posteriores, aplicando técnicas habituales de **data cleaning**, **feature engineering** y **lógica de negocio**, tal y como se haría en un entorno profesional de data analytics.

---

## Objetivos del proyecto

- Analizar y detectar valores nulos en el dataset
- Aplicar distintas estrategias de imputación según el tipo de variable
- Limpiar y normalizar nombres de columnas utilizando expresiones regulares
- Unificar convenciones de nombres (minúsculas y snake_case)
- Filtrar datos según condiciones avanzadas
- Crear nuevas variables (feature engineering)
- Realizar análisis numérico y rankings
- Calcular métricas personalizadas por pasajero
- Generar un dataset final limpio y reproducible

---

## Estructura del proyecto

# Titanic Data Cleaning & Feature Engineering

Este proyecto realiza un proceso completo de **análisis, limpieza y transformación de datos** sobre el dataset del Titanic utilizando **Python y pandas**.

El objetivo principal es preparar un DataFrame limpio y estructurado para análisis posteriores, aplicando técnicas habituales de **data cleaning**, **feature engineering** y **lógica de negocio**, tal y como se haría en un entorno profesional de data analytics.

---

## Objetivos del proyecto

- Analizar y detectar valores nulos en el dataset
- Aplicar distintas estrategias de imputación según el tipo de variable
- Limpiar y normalizar nombres de columnas utilizando expresiones regulares
- Unificar convenciones de nombres (minúsculas y snake_case)
- Filtrar datos según condiciones avanzadas
- Crear nuevas variables (feature engineering)
- Realizar análisis numérico y rankings
- Calcular métricas personalizadas por pasajero
- Generar un dataset final limpio y reproducible

---

## Estructura del proyecto

titanic-data-cleaning/
│
├── data/
│ ├── titanic.xlsx # Dataset original
│ └── titanic_cleaned.csv # Dataset limpio generado por el script
│
├── notebooks/
│ └── titanic_cleaning.ipynb # Notebook explicativo paso a paso
│
├── scripts/
│ └── titanic_cleaning.py # Script reproducible con funciones
│
├── README.md
└── requirements.txt

---

## Dataset

- **Fuente**: Dataset clásico del Titanic
- **Formato original**: Excel (`.xlsx`)
- **Contenido**: Información demográfica, socioeconómica y de supervivencia de los pasajeros

---

## Flujo de trabajo

### 1. Comprobación de valores nulos
- Creación de un DataFrame booleano para identificar valores faltantes
- Conteo de valores nulos por columna y total del DataFrame

### 2. Relleno de valores nulos
Se aplican distintas estrategias según la naturaleza de la variable:
- `Age`: media de la columna
- `Fare`: valor constante (100)
- `Embarked`: moda
- `Cabin`: forward fill (`ffill`) y backward fill (`bfill`)

### 3. Limpieza de columnas
- Eliminación de acentos y caracteres especiales
- Eliminación de espacios en blanco
- Conversión a minúsculas
- Uso de convención `snake_case`

### 4. Filtrado avanzado
- Pasajeros con edad entre 18 y 60 años
- Tarifa (`fare`) por encima del percentil 50

### 5. Feature engineering
- Creación de la variable `categoria_edad`:
  - Joven: < 30 años
  - Adulto: 30–45 años
  - Mayor: > 45 años

### 6. Análisis numérico
- Ordenación por tarifa descendente
- Eliminación de duplicados (`passengerid` + `pclass`)
- Creación de ranking de tarifas (`fare_rank`)

### 7. Puntuación personalizada
Se calcula una puntuación por pasajero en función de:
- Supervivencia
- Edad
- Tarifa
- Clase del pasajero

### 8. Índice de sobrevivencia
Se crea una métrica compuesta (`indice_sobrevivencia`) basada en:
- Tarifa
- Edad
- Clase
- Sexo
- Supervivencia

Finalmente, los pasajeros se clasifican en:
- **Alta**
- **Media**
- **Baja** probabilidad de sobrevivencia

---

## Cómo ejecutar el proyecto

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/titanic-data-cleaning.git
cd titanic-data-cleaning
```

2. (Opcional) Crea y activa un entorno virtual:
```bash
python -m venv titanic-env
source titanic-env/bin/activate  # Linux/Mac
titanic-env\Scripts\activate     # Windows
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta el script principal:
```bash
python scripts/titanic_cleaning.py
```

El dataset limpio se generará automáticamente en:
```bash
data/titanic_cleaned.csv
```
---

## Notebook vs Script

En este proyecto se incluyen dos formas de trabajar con los datos del Titanic:

- **Notebook (`notebooks/titanic_cleaning.ipynb`)**  
  El notebook sirve como documento explicativo paso a paso. Contiene:
  - Explicaciones en Markdown sobre cada etapa del análisis.
  - Visualización de outputs intermedios.
  - Código lineal que sigue el flujo del proyecto.
  
  Es ideal para presentar el razonamiento y la metodología del proyecto, y para que un recruiter o tutor pueda entender claramente cada paso.

- **Script (`scripts/titanic_cleaning.py`)**  
  El script es la versión profesional y reproducible del proyecto. Contiene:
  - Funciones modulares que encapsulan la lógica de limpieza, filtrado y feature engineering.
  - Lectura del dataset y escritura del CSV final de manera automatizada.
  - Permite ejecutar todo el pipeline con un solo comando:
  
  ```bash
  python scripts/titanic_cleaning.py

---

## Tecnologías utilizadas
- Python
- pandas
- unidecode
- Jupyter Notebook

---

## Autor
**Autor:** Andrés Matesanz
[LinkedIn](https://www.linkedin.com/in/andresmatesanz/) | [GitHub](https://github.com/andresmatesanz)

Proyecto realizado como parte de un proceso formativo en análisis de datos y refactorizado posteriormente para su uso como proyecto de portfolio.