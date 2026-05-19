from Hospital.Hijas.paciente import Paciente

class Sala():

    def __init__(self, id=int, Cantidad_C=int):
        self.__id = id
        self.__Cantidad_C = Cantidad_C
        self.__ListadoPaciente = []

    def __str__(self, ):
        return f"Sala: {self.__id}\nCantidad de Camas: {self.__Cantidad_C}"
    
    def getid(self):
        return self.__id
    
    def getCantidad_C(self):
        return self.__Cantidad_C
    
    def getListadoPaciente(self):
        return self.__ListadoPaciente

    def asignarpaciente(self, paciente):
        if len(self.__ListadoPaciente) < self.__Cantidad_C:
            self.__ListadoPaciente.append(paciente)
            print("Paciente Asignado correctamente")
        else:
            print(f"Sala {self.__id} sin disponibilidad. Camas ocupadas: {len(self.__ListadoPaciente)}/{self.__Cantidad_C}")
    
    def setid(self, id):
        self.__id = id
    
    def setCantidad_C(self, Cantidad_C):
        self.__Cantidad_C = Cantidad_C

    def setListadoPaciente(self, ListadoPaciente):
        self.__ListadoPaciente = ListadoPaciente

    def showPaciente(self):
        if len(self.__ListadoPaciente) == 0:
            print("No tiene paciente asginado")
        else:
            for i in range(len(self.__ListadoPaciente)):
                print(self.__ListadoPaciente[i]) 
    
    
        

        