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


class Pedido:
    def __init__(self):
        self.productos = []  # Lista de productos
        self.cantidades = []  # Lista de cantidades correspondientes a los productos
    
    # Función para añadir un producto al pedido
    def agregar_producto(self, producto, cantidad):
        self.productos.append(producto)
        self.cantidades.append(cantidad)
    
    # Función para calcular el precio total del pedido
    def total_pedido(self):
        total = 0
        for i in range(len(self.productos)):
            total += self.productos[i].calcular_total(self.cantidades[i])
        return total
    
    # Función para mostrar los productos del pedido
    def mostrar_productos(self):
        print("Productos en el pedido:")
        for i in range(len(self.productos)):
            producto = self.productos[i]
            cantidad = self.cantidades[i]
            print(f"{producto.get_nombre()} (Código: {producto.get_codigo()}) - {cantidad} unidades - Precio unitario: {producto.get_precio()}€")


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto(101, "Camiseta", 15.99)
    producto2 = Producto(102, "Pantalón", 25.50)
    
    # Crear un pedido
    pedido = Pedido()
    
    # Agregar productos al pedido
    pedido.agregar_producto(producto1, 3)  # 3 camisetas
    pedido.agregar_producto(producto2, 2)  # 2 pantalones
    
    # Mostrar los productos del pedido
    pedido.mostrar_productos()
    
    # Calcular el precio total del pedido
    total = pedido.total_pedido()
    print(f"\nEl precio total del pedido es: {total:.2f}€")