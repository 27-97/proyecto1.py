#Relación de elementos y su masa molar 

import matplotlib.pyplot as plt

# Datos: Elementos químicos y sus masas molares (g/mol)
elementos = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
masas_molares = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.bar(elementos, masas_molares, color='skyblue', edgecolor='black')

# Personalización del gráfico
plt.title('Relación entre Elementos y su Masa Molar', fontsize=14)
plt.xlabel('Elementos Químicos', fontsize=12)
plt.ylabel('Masa Molar (g/mol)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
