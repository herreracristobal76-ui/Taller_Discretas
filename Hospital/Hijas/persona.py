class Persona:

    def __init__(self, rut="", edad=int, nombre=""):
        self.__rut = rut
        self.__edad = edad
        self.__nombre = nombre

    def getrut(self):
        return self.__rut
    
    def getedad(self):
        return self.__edad
    
    def getnombre(self):
        return self.__nombre
    
    def setrut(self, rut):
        self.__rut = rut

    def setedad(self, edad):
        self.__edad = edad

    def setnombre(self, nombre):
        self.__nombre= nombre
    
    @staticmethod
    def rol():
        pass