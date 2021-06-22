"""
Crear una clase descuento que tiene los siguientes atributos:
	- tipo: es un string y solo puede ser fijo o porcentaje
	- valor: es un numero. si es fijo debe ser mayor que 0 y 
	si es porcentaje debe estar entre 1 y 100.
Tiene la siguiente funcionalidad:
	- aplicar:descuento(precio)
		- si el tipo es fijo, se le resta la cantidad al precio
		- si el tipo de porcentaje, se le resta el porcentaje al 
		precio
Aniadir este descuento al producto esre sera opcional y solo se 
aplicara si tiene descuento
Validar que el descuento se crea correctamente
"""

TIPO_DESC_FIJO="Fijo"
TIPO_DESC_PORC="Porcentaje"


class Descuento:
	"""docstring for Descuento"""
	def __init__(self, tipo, valor):
		if not isinstance(valor, int):
			raise ValueError("contructor descuento: valor debe ser numerico")
		if not isinstance(tipo, str):
			raise ValueError("contructor descuento: valor debe ser string")
		if tipo!=TIPO_DESC_PORC and tipo!=TIPO_DESC_FIJO:
			raise ValueError("constructor descuento: el tipo debe ser fijo o porcentaje")
		if tipo==TIPO_DESC_FIJO and valor<=0:
			raise ValueError("constructor descuento: el valor es el tipo fijo sea mayor que 0")
		if tipo==TIPO_DESC_PORC and (valor<=0 or valor>100):
			raise ValueError("constructor descuento: el valor en el tipo porcentaje debe esta entre 1 y 100r")

		self.__tipo=tipo
		self.__valor=valor

	@property
	def tipo(self):
		return self.__tipo

	@tipo.setter
	def tipo(self, valor):
		self.__tipo=valor

	@property
	def valor(self):
		return self.__valor

	@valor.setter
	def valor(self, valor):
		self.__valor=valor	

	def aplicar_descuento(self, precio):
		if self.__tipo==TIPO_DESC_FIJO:
			if precio>self.__valor:
				return precio-self.__valor
			else:
				return 0
		else:
			return precio-(precio*(self.__valor/100))