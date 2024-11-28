#Relación entre elementos y electronegatividad

import matplotlib.pyplot as plt

# Datos para electronegatividad
elementos = ['H', 'C', 'O', 'N', 'Cl', 'S', 'F', 'P', 'I', 'Br']
electronegatividad = [2.20, 2.55, 3.44, 3.04, 3.16, 2.58, 3.98, 2.19, 2.66, 2.96]

# Gráfico de electronegatividad
plt.figure(figsize=(8, 5))
plt.bar(elementos, electronegatividad, color='skyblue')
plt.title('Relación entre Elementos y Electronegatividad')
plt.xlabel('Elementos')
plt.ylabel('Electronegatividad (Pauling)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
