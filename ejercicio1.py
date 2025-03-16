class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo  # Atributo: código del producto
        self.nombre = nombre  # Atributo: nombre del producto
        self.precio = precio  # Atributo: precio del producto
    
    # Getter para el código
    def get_codigo(self):
        return self.codigo
    
    # Setter para el código
    def set_codigo(self, codigo):
        self.codigo = codigo
    
    # Getter para el nombre
    def get_nombre(self):
        return self.nombre
    
    # Setter para el nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    # Getter para el precio
    def get_precio(self):
        return self.precio
    
    # Setter para el precio
    def set_precio(self, precio):
        self.precio = precio
    
    # Función para calcular el precio total dado un número de unidades
    def calcular_total(self, unidades):
        return self.precio * unidades