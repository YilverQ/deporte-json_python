class Deporte:
	def __init__(self):
		self.nombre = self.nombre_deporte()


	def datos_del_deporte(self):
		self.jugadores = self.jugadores_equipo()
		self.campo = self.tipo_campo()
		self.pelota = self.juega_pelota()
		self.valor_completo = self.generara_valores_diccionairo()

	def nombre_deporte(self):
		return input("Ingresar Nombre del Deporte: \n|: ").title()

	
	def jugadores_equipo(self):
		return int(input("Ingresar Numero de Jugadores por Equipo: \n|: "))


	def tipo_campo(self):
		opc = True
		while opc:
			opcion = int(input("1. Grama\n2. Tabloncillo\n3. Piso\n4. Mesa\n5. Otro Tipo\n|: "))
			opc = not(self.comprobar_opcion(opcion,5))
		return self.opcion_tipo_campo(opcion)


	def opcion_tipo_campo(self,opcion):
		lista = ["Grama","Tabloncillo","Piso","Mesa","Otro Tipo"]
		return lista[opcion-1]


	def juega_pelota(self):
		opc = True
		while opc:
			opcion = int(input("1. Si Juega\n2. No Juega\n|: "))
			opc = not(self.comprobar_opcion(opcion,2))
		return True if opcion == 1 else False


	def generara_valores_diccionairo(self):
		return {"Nombre":self.nombre,
				"Jugadores":self.jugadores,
				"Campo":self.campo,
				"Pelota":self.pelota}


	def devolverValorCompleto(self):
		return self.valor_completo


	def comprobar_opcion(self,opcion,numero_max):
		return True if opcion>0 and opcion<=numero_max else False


	def opciones_modificar(self):
		opc = True
		while opc:
			opcion = int(input("1. Nombre\n2. Numero de Jugadores\n3. Tipo de Campo\n4. Pelota\n|: "))
			opc = not(self.comprobar_opcion(opcion,4))
		return opcion