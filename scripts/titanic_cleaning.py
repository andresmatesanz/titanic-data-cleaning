import pandas as pd
from unidecode import unidecode


# =========================
# 1. Carga de datos
# =========================
def cargar_datos(path="data/titanic.csv"):
    """
    Carga el dataset del Titanic desde la carpeta data.
    """
    return pd.read_csv(path)


# =========================
# 2. Análisis de valores nulos
# =========================
def analizar_nulos(df):
    """
    Devuelve el número de valores nulos por columna
    y el total de valores nulos del DataFrame.
    """
    nulos_por_columna = df.isnull().sum()
    total_nulos = nulos_por_columna.sum()
    return nulos_por_columna, total_nulos


# =========================
# 3. Limpieza de valores nulos
# =========================
def limpiar_nulos(df):
    """
    Aplica distintas estrategias de imputación
    según el enunciado del proyecto.
    """
    df["age"].fillna(df["age"].mean(), inplace=True)
    df["fare"].fillna(100, inplace=True)
    df["embarked"].fillna(df["embarked"].mode()[0], inplace=True)
    df["cabin"].fillna(method="ffill", inplace=True)
    df["cabin"].fillna(method="bfill", inplace=True)
    return df


# =========================
# 4. Limpieza de columnas (regex)
# =========================
def limpiar_columnas(df):
    """
    Limpia nombres de columnas:
    - elimina acentos
    - elimina espacios
    - convierte a minúsculas
    """
    df.columns = [unidecode(col) for col in df.columns]
    df.columns = df.columns.str.strip().str.lower()
    return df


# =========================
# 5. Filtrado avanzado
# =========================
def filtrar_pasajeros(df):
    """
    Filtra pasajeros con:
    - edad entre 18 y 60
    - tarifa por encima del percentil 50
    """
    return df.loc[
        (df["age"].between(18, 60)) &
        (df["fare"] > df["fare"].quantile(0.50))
    ]


# =========================
# 6. Feature engineering: categoría de edad
# =========================
def crear_categoria_edad(df):
    """
    Crea la columna categoria_edad según la edad del pasajero.
    """
    df.loc[df["age"] < 30, "categoria_edad"] = "Joven"
    df.loc[df["age"].between(30, 45), "categoria_edad"] = "Adulto"
    df.loc[df["age"] > 45, "categoria_edad"] = "Mayor"
    return df


# =========================
# 7. Análisis numérico de tarifas
# =========================
def analizar_tarifas(df):
    """
    Ordena por tarifa descendente, elimina duplicados
    y crea un ranking de tarifas.
    """
    df = df.sort_values("fare", ascending=False)
    df = df.drop_duplicates(["passengerid", "pclass"])
    df["fare_rank"] = df["fare"].rank(ascending=False)
    return df


# =========================
# 8. Puntuación personalizada
# =========================
def calcular_puntuacion(df):
    """
    Calcula una puntuación para cada pasajero
    según reglas definidas en el enunciado.
    """
    df["puntuacion"] = 0

    df.loc[df["survived"] == 1, "puntuacion"] += 5
    df.loc[df["age"] >= 50, "puntuacion"] += 4
    df.loc[df["fare"] > 200, "puntuacion"] += 3
    df.loc[df["pclass"] == 1, "puntuacion"] += 2
    df.loc[df["pclass"] == 3, "puntuacion"] -= 2

    return df


# =========================
# 9. Índice de sobrevivencia
# =========================
def calcular_indice_sobrevivencia(df):
    """
    Calcula el índice de sobrevivencia y clasifica
    a los pasajeros en Alta, Media o Baja.
    """
    df["indice_sobrevivencia"] = df["fare"] * 2

    df.loc[df["age"] > 50, "indice_sobrevivencia"] -= 10
    df.loc[df["pclass"] == 1, "indice_sobrevivencia"] += 15
    df.loc[
        (df["sex"] == "male") & (df["survived"] == 1),
        "indice_sobrevivencia"
    ] *= 1.2
    df.loc[
        (df["pclass"] == 3) & (df["age"] > 60),
        "indice_sobrevivencia"
    ] /= 2

    df.loc[df["indice_sobrevivencia"] > 200, "probabilidad_sobrevivencia"] = "Alta"
    df.loc[df["indice_sobrevivencia"].between(100, 200), "probabilidad_sobrevivencia"] = "Media"
    df.loc[df["indice_sobrevivencia"] < 100, "probabilidad_sobrevivencia"] = "Baja"

    return df


# =========================
# 10. Ejecución principal
# =========================
if __name__ == "__main__":
    df = cargar_datos()
    df = limpiar_columnas(df)

    analizar_nulos(df)

    df = limpiar_nulos(df)
    df = filtrar_pasajeros(df)
    df = crear_categoria_edad(df)
    df = analizar_tarifas(df)
    df = calcular_puntuacion(df)
    df = calcular_indice_sobrevivencia(df)

    df.to_csv("data/titanic_cleaned.csv", index=False)
