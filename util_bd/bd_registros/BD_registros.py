from util_bd.bd_registros.IBD_registros import * 
from util_bd.bd_general.BD_conexion import * 
class BD_registros(IBD_registros):
    def registrarEntrada(self,entrada):
        '''El argumento para el parámetro es un objetivo tipo entrada'''
        pass
    
    def registrarSalida(self,salida):
        '''El argumento para el parámetro es un objetivo tipo salida'''
        pass

    def testearConexion(self):
        conexion = BD_conexion()
        print(conexion.test())


