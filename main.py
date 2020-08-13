from deporte import *
from datos_json import *


class Menu:
	def __init__(self):
		self.obj_json = Datos()
		self.obj_json.comprobarJson()


	def imprimir_mensaje(self,mensaje):
		print("---- ---- ----")
		print(f"{mensaje}")
		print("---- ---- ----")


	def agregar(self):
		self.imprimir_mensaje("Agregar Deporte") 
		obj_Deporte = Deporte()

		if self.obj_json.buscar_nombre(obj_Deporte.nombre):
			return "El Deporte Ya Está Regristrado"
		else:
			obj_Deporte.datos_del_deporte()
			self.obj_json.obtener_datos(obj_Deporte.devolverValorCompleto())
			self.obj_json.ingresar_deporte()
			return f"El Deporte {obj_Deporte.nombre} Se Registro!"


	def ver_deporte(self):
		self.imprimir_mensaje("Caracteristica de un Deporte")
		nombre_buscar = input("Ingresa el Nombre a Buscar: ").title()

		if self.obj_json.buscar_nombre(nombre_buscar):
			for clave,valor in self.obj_json.devolver_datos_deporte(nombre_buscar).items():
				print(f"{clave}: {valor}")
			return f"Fin de las Caracteristica de {nombre_buscar}"
		else:
			return "EL Deporte Ingresado no Está Registrado"


	def ver_listado(self):
		self.imprimir_mensaje("Lista de Deportes")
		lista = self.obj_json.devolver_listado()

		if len(lista)!=0:
			for i in range(len(lista)):
				print(f"{i+1}. {lista[i]}")
			return "Fin de la Lista"
		else:
			return "No Hay Deportes Registrado"


	def modificar_deporte(self):
		self.imprimir_mensaje("Lista de Deportes")
		deporte_modificar = Deporte()

		if self.obj_json.buscar_nombre(deporte_modificar.nombre):
			opcion_elegida = deporte_modificar.opciones_modificar()
			return deporte_modificar, opcion_elegida
		else:
			return "EL Deporte Ingresado no Está Registrado"


	def menu_modificar(self,obj_deporte,opcion_elegida):
		if opcion_elegida == 1:
			nuevo_valor = obj_deporte.nombre_deporte()
		elif opcion_elegida == 2:
			nuevo_valor = obj_deporte.jugadores_equipo()
		elif opcion_elegida == 3:
			nuevo_valor = obj_deporte.tipo_campo()
		elif opcion_elegida == 4:
			nuevo_valor = obj_deporte.juega_pelota()

		return nuevo_valor


	def vaciar(self):
		self.obj_json.vaciar_json()
		return "Lista de Deportes Borrada!"


	def ejecucion_modificar(self):
		var_modificar = self.modificar_deporte()
		if type(var_modificar)==type((1,2,3)):
			var_modificar = list(var_modificar)
			var_modificar.append(self.menu_modificar(var_modificar[0],var_modificar[1]))
			self.obj_json.modificar_atributos(var_modificar[0].nombre,var_modificar[1],var_modificar[2])
			self.obj_json.actualizar_atributos()
			return "Atributos Modificados"
		else:
			return var_modificar


	def menu_opciones(self, opcion):
		if opcion>=1 and opcion<=5:
			if opcion == 1:
				print(self.agregar())
			elif opcion == 2:
				print(self.ver_deporte())
			elif opcion == 3:
				print(self.ver_listado())
			elif opcion == 4:
				print(self.ejecucion_modificar())
			else:
				print(self.vaciar())
			return True
		else:
			print("Saliendo del Programa")
			return False


	def menu_inicio(self):
		opc = True
		while opc:
			self.imprimir_mensaje("Menu")
			print("1. Ingresar Deporte\n2. Ver Detalles de Deporte\n3. Ver Lista de Deportes")
			print("4. Modificar un Deporte\n5. Vaciar Lista\n6. Salir")
			opcion = int(input("Ingresa una Opcion: "))
			if opcion>=1 and opcion<=6:
				opc = self.menu_opciones(opcion)
			else:
				print(f"Opcion Ingresada no es Valida!")

		return "Fin Del Programa"


hola = Menu()
hola.menu_inicio()