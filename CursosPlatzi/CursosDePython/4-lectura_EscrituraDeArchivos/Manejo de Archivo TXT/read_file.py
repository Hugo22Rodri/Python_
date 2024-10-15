#leer archivo linea por linea
with open('la_gallina_de_los_huevos_de_oro.txt','r') as file:
    for lineas in file:
        print(lineas.strip())

#leer todas las lineas en una lista
'''with open('cuento.txt', 'r') as file:
    lines = file.readlines()
    print(lines)'''

#Añadir texto
'''with open('cuento.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")'''

#sobreescribir en el texto
''''with open('cuento.txt', 'r') as file:
    file.write("\n\nBy:ChatGPT")'''