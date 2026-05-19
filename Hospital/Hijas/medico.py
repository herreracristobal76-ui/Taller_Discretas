from Hospital.Hijas.persona import Persona

class Medico(Persona):

    def __init__(self, rut="", edad=int, nombre="", especialidad=""):
        super().__init__(rut, edad, nombre)
        self.__especialidad = especialidad
        self.__ListadoPaciente = []

    def __str__(self):
        return f"Médico: {self.getnombre()}\nRut: {self.getrut}\nEspecialidad: {self.__especialidad}"

    def getespecialidad(self):
        return self.__especialidad
    
    def getListadoPacientes(self):
        return self.__ListadoPaciente
    
    def asignarpaciente(self, paciente):
        self.__ListadoPaciente.append(paciente)
    
    def setespecialidad(self, especialidad):
        self.__especialidad = especialidad
    
    def showPaciente(self):
        if len(self.__ListadoPaciente) == 0:
            print("No tiene paciente asginado")
        else:
            for i in range(len(self.__ListadoPaciente)):
                print(self.__ListadoPaciente[i])    

    
