
### Objetos dentro de objetos 


class Productos: 
    # Constructor de clase 
    def __init__(self,nombre,precio,marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        print("Se ha crado el producto",self.nombre)

    def __str__(self) -> str:
        return f"la película {self.nombre} con precio {self.precio} y de la marca {self.marca}"
    
class Catalogo: 
    productos = []  # Esta lista contendrá objetos de la clase Producto
    
    def __init__(self):
        self.productos = []

    def agregar(self,p:Productos): # p será un objeto Producto
        self.productos.append(p)

    def mostrar(self):
        for p in self.productos:
            print(p)
            print(f"El producto {p.nombre} con precio de {p.precio} y de la marca {p.marca}")

p1 = Productos('zapatilla',300,'nike') 
p2 = Productos('celular',320,'Apple')
p3 = Productos('medias',20,'Adidas')   

c1 = Catalogo()
c1.agregar(p1)
c1.agregar(p2)
c1.agregar(p3)

c1.mostrar()
