class Productos(object):
    def __init__(self, sku, nombre, tipo, laboratorio):
        self.sku=sku
        self.nombre=nombre
        self.tipo=tipo
        self.laboratorio=laboratorio

    def __del__(self):
        print("Eliminando de la memoria el producto con sku:", self.sku)

class remedio (Productos) :
	def __init__(self, sku, nombre, tipo, laboratorio, elaboracion, caducidad):
		Productos.__init__(self, sku, nombre, tipo, laboratorio)
		self.elaboracion=elaboracion
		self.caducidad=caducidad

remedio1 = remedio("10", "Paracetamol", "Medicamento", "Laboratorio Chile", "01/01/2022", "01/01/2024")
print("Datos: {}, {}, {}, {}, {} {}, {} {}".format(remedio1.sku, remedio1.nombre, remedio1.tipo, remedio1.laboratorio, "Elaboración:",remedio1.elaboracion, "Caducidad:", remedio1.caducidad))
remedio1.__del__