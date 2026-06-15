import numpy as np
import time

def minimos_cuadrados(X, Y):
    n = len(X)
    suma_x = np.sum(X)
    suma_y = np.sum(Y)
    suma_xy = np.sum(X * Y)
    suma_x2 = np.sum(X**2)
    
    denominador = n * suma_x2 - (suma_x)**2
    if denominador == 0:
        raise ValueError("Error: Datos verticalmente alineados (Division por cero).")
        
    m = (n * suma_xy - suma_x * suma_y) / denominador
    c = (suma_y - m * suma_x) / n
    return m, c

# 1. Datos de telemetria simulados (Carga de usuarios vs Latencia en ms)
# Se incluye ruido aleatorio emulando el comportamiento de una red real
np.random.seed(42)
usuarios = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], dtype=float)
# Relacion base: latencia = 2.5 * usuarios + 120 + ruido
ruido = np.random.normal(0, 8, len(usuarios))
latencia = 2.5 * usuarios + 120 + ruido

# 2. Medicion del tiempo de ejecucion del algoritmo propio
inicio_propio = time.perf_counter()
m_propio, c_propio = minimos_cuadrados(usuarios, latencia)
fin_propio = time.perf_counter()
tiempo_propio = fin_propio - inicio_propio

# 3. Validacion con funcion de libreria oficial (numpy.polyfit)
inicio_lib = time.perf_counter()
m_lib, c_lib = np.polyfit(usuarios, latencia, 1)
fin_lib = time.perf_counter()
tiempo_lib = fin_lib - inicio_lib

# 4. Calculo del Coeficiente de Determinacion R2 (Analisis de Error)
y_pred = m_propio * usuarios + c_propio
y_barra = np.mean(latencia)
Sr = np.sum((latencia - y_pred)**2)
St = np.sum((latencia - y_barra)**2)
R2 = 1 - (Sr / St)

# 5. Despliegue de resultados en consola
print("--- RESULTADOS ALGORITMO PROPIO ---")
print(f"Pendiente (m): {m_propio:.4f} ms/usuario")
print(f"Interseccion (c): {c_propio:.4f} ms (Latencia base)")
print(f"Tiempo de ejecucion: {tiempo_propio * 1e6:.2f} microsegundos")
print(f"Coeficiente R2 (Calidad del ajuste): {R2:.4f}")

print("\n--- VALIDACION CON LIBRERIA (polyfit) ---")
print(f"m_lib: {m_lib:.4f} | c_lib: {c_lib:.4f}")
print(f"Tiempo de ejecucion libreria: {tiempo_lib * 1e6:.2f} microsegundos")