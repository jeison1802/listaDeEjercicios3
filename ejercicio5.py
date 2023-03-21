
import os 

class Producto:
    ### atributos y que funcionalidades hace
    # nombre, edad, producto_que_elige 
    # comprar, caminar  

    nombre =""
    codigo =""
    
    def __init__(self,nombre,codigo) -> None:
        self.nombre = nombre
        self.codigo = codigo
        
    ### describan la clase x sus atributos y métodos. 
    

    def __str__(self) -> str:
        return f"El producto con nombre {self.nombre} tiene el codigo {self.codigo}"

    def verificar_pais(self,codigo):
         
         print("El pais es: ",end="")
         for i in self.codigo: 
            if i == "-":
               break
      
            print(i,end ="")
      
    
    def verificar_lote(self,codigo):
        print("El lote es: ",end="")
        
        d = self.codigo.index("-")
        nuevo_codigo = self.codigo[d+1:]
        e = nuevo_codigo.index("-")
        print(nuevo_codigo[:e])

try: 
    px = Producto("zapatilla","TAILANDIA-0002-2022")
    print("Este es el print del objet: ",px)
    px.verificar_lote("TAILANDIA-0002-2022")
    px.verificar_pais("TAILANDIA-0002-2022")
    print("\n")
    print(__name__)
except Exception as E:
    print(E)

else: print(os.getcwd())

finally: 
    print("proceso terminado")

## describan una clase x sus atributos y métodos. 
