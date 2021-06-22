"""
Añadir una clase precio que tiene como atributos:
	- lista de productos
	- lista de cantidades
Añadir las siguientes funcionalidades:
	- total_precio: muestr el precio del pedido
	- mostrar productos: muestra los productos del pedido 
"""
from Poo1 import Producto
from Poo3 import Descuento 

class Pedido:
	
	def __init__(self):
		self.__productos=[]
		self.__cantidades=[]

	def aniadir_producto(self, producto, cantidad):
		if not isinstance(producto, Producto):
			raise Exception("aniadir_producto: el producto debe ser de la clase producto")#lanzar exception

		if not isinstance(cantidad, int):
			raise Exception("aniadir_producto: cantidad debe ser un numero")#lanzar exception

		if cantidad<=0:
			raise Exception("aniadir_producto: cantidad debe ser mayor a 0")
		
		if producto in self.__productos:#existe en el array
			indice=self.__productos.index(producto)
			self.__cantidades[indice]=self.__cantidades[indice]+cantidad
		else:
			self.__productos.append(producto)#agrefar el producti
			self.__cantidades.append(cantidad)

	def eliminar_producto(self, producto):
		if not isinstance(producto, Producto):
			raise Exception("eliminar_producto: el producto debe ser de la clase producto")#lanzar exception
		if producto in self.__productos:#existe en el array
			indice=self.__productos.index(producto)
			del self.__productos[indice]
			del self.__cantidades[indice]
		else:
			raise Exception("eliminar_producto: producto no existe")


	def total_pedido(self):
		total=0
		for (p,c) in zip(self.__productos, self.__cantidades):#recorrer dos arrays al mismp tiempo
			#se puede recorrer al mismo tiempo N arrays
			total=total-p.calcular_total(c)
			t=total*-1
		return t

	def mostrar_pedido(self):
		for (p,c) in zip(self.__productos, self.__cantidades):#recorrer dos arrays al mismp tiempo
			print('Producto->(' ,p, ') Cantidad: '+str(c))



desc1=Descuento("Fijo",5)
desc2=Descuento("Porcentaje",50)

p1=Producto(1,"Producto 1",5)#ccreacion de objeto
p2=Producto(2,"Producto 2",10,desc1)
p3=Producto(3,"Producto 3",20,desc2)
print("Descuento 1",p1)
print("Descuento 2",p2)
print("Descuento 3",p3)

print(p1.calcular_total(5))
print(p2.calcular_total(5))
print(p3.calcular_total(5))

productos=[p1, p2, p3]
cantidades=[15, 1, 1]

pedido=Pedido()
try:
	pedido.aniadir_producto(p1, 5)
	pedido.aniadir_producto(p2, 5)
	pedido.aniadir_producto(p3, 5)
	print("total pedido:",str(pedido.total_pedido()))
	pedido.mostrar_pedido()
	pedido.eliminar_producto(p1)
	print("total pedido:",str(pedido.total_pedido()))
	pedido.mostrar_pedido()
except Exception as e:
	print(e)

