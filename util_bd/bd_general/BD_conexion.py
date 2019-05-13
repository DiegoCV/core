from util_bd.bd_general.conexion_mysql.BD_mysql import * 

class BD_conexion:

    def test(self):
    	con = BD_mysql()
    	return con.getConector()




