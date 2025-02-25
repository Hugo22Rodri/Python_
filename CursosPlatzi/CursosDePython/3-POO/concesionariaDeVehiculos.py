class Vehicle:
    #Encapsulacion
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
 
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No esta disponible")
    #Abstraccion
    def check_available(self):
        return self.is_available
    #Abstraccion
    def get_price(self):
        return self.price
    
    def star_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

#subclase
#Herencia
class Car(Vehicle):
    def star_engine(self):#Polimorfismo
        if not self.is_available:
             return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche no esta disponible"
        
    def stop_engine(self):#Polimorfismo
        if self.is_available:
               return f"El motro del coche se ha detenido."
        else:
            return f"El coche {self.brand} No esta disponible."
#Herencia        
class Bike(Vehicle):
    def star_engine(self):
        if not self.is_available:
             return f"La bicicleta {self.brand} esta en marcha"
        else:
            return f"La bicicleta no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
               return f"La bicicleta se ha detenido."
        else:
            return f"La bicicleta {self.brand} No esta disponible."

class Truck(Vehicle):
    def star_engine(self):
        if not self.is_available:
             return f"El motor del camion {self.brand} esta en marcha"
        else:
            return f"El camion no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
               return f"El motro del camion se ha detenido."
        else:
            return f"El camion {self.brand} No esta disponible."
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicles(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no esta disponible.")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
            print(f"El {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []
    
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventadorio")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añanido.")

    def show_available_vehicle(self):
        print(f"Vehiculos disponibles en la tienda.")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")
#
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#coches disponibles
dealership.show_available_vehicle()

#Consultar coches
customer1.inquire_vehicle(car1)

#comprar un coche
customer1.buy_vehicles(car1)

#muetra los coches disponibles
dealership.show_available_vehicle()