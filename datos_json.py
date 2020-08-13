import json
import os

class Datos:
	def __init__(self):
		self.datos = {}
		self.variable_datos = {}

	def comprobarJson(self):
		if os.stat("data.json").st_size == 0:
			json_data = {"Deporte":[]}
			with open("data.json", "w") as file:
				json.dump(json_data, file, indent=4)


	def obtener_datos(self,datos):
		self.datos = datos 

		
	def cargar_datos(self):
		with open("data.json", "r") as file:
			self.variable_datos = json.load(file)


	def ingresar_deporte(self):
		with open("data.json", "w") as file:
			self.variable_datos["Deporte"].append(self.datos)
			json.dump(self.variable_datos, file, indent=4)

		
	def buscar_nombre(self,nombre):
		self.cargar_datos()
		for i in self.variable_datos["Deporte"]:
			if i["Nombre"] == nombre:
				return True

		return False


	def devolver_datos_deporte(self,nombre):
		self.cargar_datos()
		for i in self.variable_datos["Deporte"]:
			if i["Nombre"] == nombre:
				return i


	def devolver_listado(self):
		self.cargar_datos()
		lista = []
		for i in self.variable_datos["Deporte"]:
			lista.append(i["Nombre"])

		return lista


	def modificar_atributos(self,nombre_deporte_elegido, opcion_elegido, nuevo_atributo):
		self.cargar_datos()
		lista_opciones = ["Nombre","Jugadores","Campo","Pelota"]
		for i in self.variable_datos["Deporte"]:
			if i["Nombre"] == nombre_deporte_elegido:
				i[lista_opciones[opcion_elegido-1]] = nuevo_atributo


	def actualizar_atributos(self):
		with open("data.json", "w") as file:
			json.dump(self.variable_datos, file, indent=4)


	def vaciar_json(self):
		with open("data.json", "w") as file:
			pass