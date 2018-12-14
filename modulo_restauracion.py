class Restaurante():
    """Intentamos modelizar un restaurante"""
    def __init__(self, nombre, cocina, clientes):
        """Inicicializa nombre,tipo de cocina y numero de clientes"""
        self.nombre=nombre
        self.cocina=cocina
        self.clientes=clientes

    def info(self):
        """Muestra la informacion del restaurante incluido el numero de clientes"""
        print("\nRestaurante " + self.nombre.title()+
          " donde puedo comer cocina "+self.cocina)
        print("Restaurante "+self.nombre.title()+
          " tiene registrados "+str(self.clientes)+" clientes.")

    def set_clientes(self, clientes):
        """Establece el numero de clientes"""
        self.clientes = clientes
        
    def inc_clientes(self, incremento=1):
        """Incrementa el numero de clientes, por defecto en 1"""
        self.clientes = self.clientes + incremento

class Heladeria(Restaurante):
    """Creamos una nueva clase de restaurantes: heladerias"""
    def __init__(self, nombre, cocina, clientes, sabores):
        """utilizamos los atributos de la clase anterior"""
        Restaurante.__init__(self, nombre, cocina, clientes)
        self.sabores = sabores
    
    def info(self):
        """Informacion de la heladeria incluidos los sabores de los helados"""
        Restaurante.info(self)
        print("\nEn la heladeria " + self.nombre.title()+
          " puedes encontrar los siguientes sabores:")
        for sabor in self.sabores:
            print("\t-"+sabor.title())
