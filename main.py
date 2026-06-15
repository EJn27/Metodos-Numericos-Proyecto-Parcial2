import numpy as np
import time
import matplotlib.pyplot as plt

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

# 6. Construccion de la Grafica Profesional para el Informe
plt.figure(figsize=(8, 5))

# Dibujar los puntos de telemetria reales recopilados
plt.scatter(usuarios, latencia, color='red', label='Datos de Telemetria (con ruido)', zorder=5)

# Dibujar la recta de tendencia obtenida por el algoritmo del Grupo 7
plt.plot(usuarios, y_pred, color='blue', linestyle='-', linewidth=2, 
         label=f'Ajuste Propio: y = {m_propio:.2f}x + {c_propio:.1f}')

# Configuracion y estetica del grafico (Formato Reporte Academico)
plt.title('Analisis de Escalabilidad: Latencia del Servidor vs Carga de Usuarios', fontsize=12, fontweight='bold')
plt.xlabel('Usuarios Concurrentes (Carga x)', fontsize=10)
plt.ylabel('Tiempo de Respuesta en ms (Latencia y)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')

# Guardar la imagen automaticamente para Overleaf antes de mostrarla en pantalla
plt.savefig('grafica_minimos_cuadrados.png', dpi=300)

# Desplegar la ventana interactiva del grafico
plt.show()

# 7. Exportar los datos simulados a un archivo CSV obligatorio
import csv
with open('telemetria_servidor.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Usuarios_Concurrentes', 'Latencia_ms'])
    for u, l in zip(usuarios, latencia):
        writer.writerow([u, l])
print("Archivo 'telemetria_servidor.csv' generado con exito.")