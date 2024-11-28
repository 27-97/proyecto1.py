#Relación de viscosidad y temperatura de un Aceite de motor.

import matplotlib.pyplot as plt
import numpy as np

# Datos: Temperatura (°C) y viscosidad (mPa·s) de un aceite de motor
temperaturas = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]
viscosidades = [1200, 450, 200, 120, 80, 50, 35, 25, 20, 18]

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar la relación viscosidad-temperatura
ax.plot(temperaturas, viscosidades, marker='o', color='blue', label='Viscosidad vs Temperatura')

# Personalización del gráfico
ax.set_title('Relación entre Viscosidad y Temperatura de un Aceite de Motor', fontsize=14)
ax.set_xlabel('Temperatura (°C)', fontsize=12)
ax.set_ylabel('Viscosidad (mPa·s)', fontsize=12)
ax.grid(alpha=0.5)
ax.legend(fontsize=10)
ax.set_xlim(0, 200)
ax.set_ylim(0, 1300)

# Crear la tabla
column_labels = ['Temperatura (°C)', 'Viscosidad (mPa·s)']
table_data = list(zip(temperaturas, viscosidades))
table = plt.table(cellText=table_data, colLabels=column_labels, cellLoc='center', loc='bottom', bbox=[0.0, -0.4, 1, 0.3])

# Ajustar diseño para la tabla
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(column_labels))))
plt.subplots_adjust(left=0.2, bottom=0.4)

# Mostrar la gráfica y la tabla
plt.show()
