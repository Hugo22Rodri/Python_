import os

#Obtener el directorio actual
cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)
"""
#Renombrar archivo
os.rename('la_gallina_de_los_huevos_de_oro.txt', 'lectura.txt')
print('Archivo renombrado')

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)"""