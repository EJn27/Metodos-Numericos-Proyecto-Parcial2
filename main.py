import numpy as np
import timeit

# 1. Implementación del algoritmo propio
def minimos_cuadrados(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x**2)
    
    denominador = n * sum_x2 - sum_x**2
    if denominador == 0:
        raise ValueError("Error: División por cero (Datos alineados verticalmente).")
        
    m = (n * sum_xy - sum_x * sum_y) / denominador
    c = (sum_y - m * sum_x) / n
    return m, c

# 2. Datos de prueba: Carga de usuarios vs Latencia en ms
x_data = np.array([100, 200, 300, 400, 500, 600, 700])
y_data = np.array([125, 150, 182, 210, 245, 270, 310])

# 3. Ejecución y medición de tiempo (Algoritmo propio)
start_time = timeit.default_timer()
m_propio, c_propio = minimos_cuadrados(x_data, y_data)
tiempo_ejecucion = timeit.default_timer() - start_time

# 4. Validación con la función de la librería NumPy
m_lib, c_lib = np.polyfit(x_data, y_data, 1)

# 5. Imprimir resultados
print("--- ANÁLISIS DE RESULTADOS ---")
print(f"Modelo Propio: y = {m_propio:.4f}x + {c_propio:.4f}")
print(f"Modelo NumPy:  y = {m_lib:.4f}x + {c_lib:.4f}")
print(f"Tiempo de ejecución: {tiempo_ejecucion:.8f} segundos")