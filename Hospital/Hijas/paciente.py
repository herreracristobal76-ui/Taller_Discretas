from Hospital.Hijas.persona import Persona

class Paciente(Persona):

    def __init__(self, rut="", edad=int, nombre="", direccion="", telefono=""):
        super().__init__(rut, edad, nombre)
        self.__direccion = direccion
        self.__telefono = telefono

    def __str__(self):
        return f"Paciente:{self.getnombre()}\nEdad:{self.getedad}\nRut:{self.getrut}\nDirección:{self.__direccion}\nTeléfono:{self.__telefono}"
    
    def getdireccion(self):
        return self.__direccion
    
    def gettelefono(self):
        return self.__telefono
    
    def setdireccion(self, direccion):
        self.__direccion = direccion

    def settelofono(self, telefono):
        self.__telefono = telefono
    
    @staticmethod
    def rol():
        print("El rol es de Paciente")
