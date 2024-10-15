import csv

#leer un archivo
'''with open('Products.csv',mode = 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)'''

# mostrar la informacion  por columnas
with open('Products.csv', mode = 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")