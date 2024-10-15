#para el uso de diccionario se usa llaves {}
numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])

information = {"nombre": "Hugo",
               "Apellido": "Rodriguez",
               "Altura": 1.54,
               "Edad": 22}
print(information)
#eliminar el ultimo elemento
del information["Edad"]
print(information)
claves = information.keys()
print(claves)

#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)

contacts = {"Carla": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},
                "Diego": {"Apellido": "Antezana",
               "Altura": 1.80,
               "Edad": 32}}
print(contacts["Carla"])