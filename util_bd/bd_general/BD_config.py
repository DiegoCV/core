class BD_config:
	def obtenerAtributo(self,atributo):
		reglas = {
	  		"host": "localhost",
			"puerto": "3306",
			"usuario": "root",
			"pass": "Soporte",
			"nombre_bd": "controlacceso" 
		}
		return reglas[atributo]