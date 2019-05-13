from registros.IRegistro import * 
from util_bd.bd_registros.BD_registros import * 

class Registro(IRegistro):
	
    def registrarEntrada(self,entrada):
        return "hola"
    
    def registrarSalida(self,salida):
        return "hola"

    def testearConexion(self):
        conRegistro = BD_registros()
        conRegistro.testearConexion()