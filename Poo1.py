"""
Crear una clase Producto con los siguientes atributos:
	codigo, nombre, precio
contentra su constructor, getter, seter y una función calcular total,
donde le pasaremos unas unidades y nps debe calcular el precio final.
"""
class Producto:
	
	#constructor
	def __init__(self, codigo, nombre, precio, descuento=None):#el parametro que tiene None es parametro opcional
		self.__codigo=codigo
		self.__nombre=nombre
		self.__precio=precio
		self.__descuento=descuento

	@property#siembre agregar @property	
	def codigo(self):#metodo get 
		return self.__codigo

	@codigo.setter
	def codigo(self, valor):#metodo set
		self.__codigo=valor

	@property
	def nombre(self):
		return self.__nombre

	@nombre.setter
	def nombre(self, valor):
		self.__nombre=valor

	@property 
	def precio(self):
		if self.__descuento==None:
			return self.__precio
		else:
			return self.__descuento.aplicar_descuento(self.__precio)

	@precio.setter
	def precio(self, valor):
		self.__precio=valor

	def calcular_total(self, unidades):
		return self.__precio*unidades

	#metodo toString
	def __str__(self):
		return 'Codigo: '+str(self.__codigo)+' Nombre: '+self.__nombre+' Precio:'+str(self.precio)




