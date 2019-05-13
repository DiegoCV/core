import mysql.connector
from util_bd.bd_general.BD_config import * 

class BD_mysql:
	def __init__(self):
		c = BD_config()
		self.mydb = mysql.connector.connect(
	        host = c.obtenerAtributo("host"),
		  	user = c.obtenerAtributo("usuario"),
		  	passwd = c.obtenerAtributo("pass")
		)
	
	
	def getConector(self):
		return self.mydb


