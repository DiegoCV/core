class Animal:
    '''Clase base de todos los animales.'''
    
    def __init__(self, nombre):
        self.nombre = nombre
        print('Hola. Mi nombre es {}.'.format(self.nombre))
    
    def reproduccion(self):
        '''Sólo define una interfaz.'''
        pass
    
    def alimentacion(self):
        '''Sólo define una interfaz.'''
        pass
    
    def __del__(self):
        print("El animal {} acaba de fallecer.".format(self.nombre))