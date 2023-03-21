### Introducción a programación orientada a objetos
## Todos los elementos de python son clases

### Creando clases


class Customer:
    ### atributos y que funcionalidades hace
    # nombre, edad, producto_que_elige 
    # comprar, caminar  
    id = 0
    fullname =""
    dni =""
    productoComprado = ""
    fechas =""
    def __init__(self,idParametro,fullnameParametro,dniParametro) -> None:
        self.id = idParametro
        self.fullname = fullnameParametro
        self.dni = dniParametro
    ### describan la clase x sus atributos y métodos. 
    
    def __str__(self) -> str:
        return f"El cliente se llama {self.fullname} con identificador {self.dni}"

    def verificar(self,fullname):
        print("El nombre completo es: ", self.fullname)
    
    def comprar(self,product):
        self.productoComprado  =product

try: 
    ismael = Customer(1,'Ismael Marin','72403104')
    ismael.comprar("celular")
    print(ismael.productoComprado)
    print(ismael.fullname)
    print("este es el print del objet: ",ismael)
    print(__name__)
except Exception as E:
    print(E)

## describan una clase x sus atributos y métodos. 


### Objetos dentro de objetos 


class Pelicula: 
    # Constructor de clase 
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha crado la pelicula ",self.titulo)

    def __str__(self) -> str:
        return f"la película {self.titulo} con duración {self.duracion}"
    
class Catalogo: 
    peliculas = []  # Esta lista contendrá objetos de la clase Película
    
    def __init__(self):
        self.peliculas = []

    def agregar(self,p:Pelicula): # p será un objeto Película
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)
            print(f"La película {p.titulo} con duracion de {p.duracion}")

p1 = Pelicula('avatar',160,2022) 
p2 = Pelicula('antman',120,2023)
p3 = Pelicula('avengers',150,2019)   

c1 = Catalogo()
c1.agregar(p1)
c1.agregar(p2)
c1.agregar(p3)

c1.mostrar()
