class Productos:
	def __init__(self, id):
		self.id=id
		print("Creando producto con id:", self.id)
	def __del__(self):
		print("eliminando de la memoria el producto con id:", self.id)
	def setDatos(self, nombre, tipo, laboratorio):
		self.nombre=nombre
		self.nombre=nombre
		self.laboratorio = laboratorio
		self.tipo = tipo

print("Clase Prodcutos para una Farmacia")
prodcuto1=Productos(1)
prodcuto1.setDatos("Paracetamol", "Medicamento", "Laboratorio Chile")
print("Datos: {}, {}, {}".format(prodcuto1.nombre, prodcuto1.tipo, prodcuto1.laboratorio))
prodcuto1.__del__

print("--------------------------------------------------------------------------------")

class Libro:
	def __init__(self, id):
		self.id=id
		print("Creando libro con id:", self.id)
	def __del__(self):
		print("eliminando de la memoria el libro con id:", self.id)
	def setDatos(self, nombre, autor, anoPublicacion):
		self.nombre=nombre
		self.autor = autor
		self.anoPublicacion = anoPublicacion

print("Clase Libro para una Biblioteca")
libro1=Libro(1)
libro1.setDatos("Como agua para chocolate", "Laura Esquivel", "1989")
print("Datos: {}, {}, {}".format(libro1.nombre, libro1.autor, libro1.anoPublicacion))
libro1.__del__
