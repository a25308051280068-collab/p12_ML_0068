import pandas as pd

print("Christian garcia Jimenez NC=0068")

# 1. Crear el dataset con los datos asignados al número 24
datos24 = {
    'distancia_km': [4.3, 1.5, 3.8, 6.2, 2.1],
    'trafico_nivel': [2, 1, 3, 2, 1],        # 1: Bajo, 2: Medio, 3: Alto
    'edad_repartidor': [36, 23, 43, 28, 32],
    'tiempo_entrega_min': [35, 11, 36, 52, 15] # Target / Variable a predecir
}

df_24 = pd.DataFrame(datos24)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df_24[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df_24['tiempo_entrega_min']                                # Target / Salida

# 3. Mostrar estructura de las primeras filas
print("--- DATOS DE ENTRADA (FEATURES - X) [datos24] ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) [datos24] ---")
print(y.head(2))

print("Christian garcia Jimenez NC=0068")