from Hospital.Hijas.medico import Medico
from Hospital.Hijas.paciente import Paciente
from Hospital.sala import Sala
from math import comb
 
class Hospital():
 
    def __init__(self, nombre="", direccion="", telefono=0):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__ListadoMedico = []
        self.__ListadoSala = []
        self.__ListadoPaciente = []

    def __str__(self):
        return f"Hospital: {self.__nombre}\nDirección: {self.__direccion}\nTeléfono: {self.__telefono}"
 
    def getnombre(self):
        return self.__nombre
 
    def getdireccion(self):
        return self.__direccion
 
    def gettelefono(self):
        return self.__telefono
 
    def getListadoMedico(self):
        return self.__ListadoMedico
 
    def getListadoSala(self):
        return self.__ListadoSala
 
    def getListadoPaciente(self):
        return self.__ListadoPaciente
 
    def setnombre(self, nombre):
        self.__nombre = nombre
 
    def setdireccion(self, direccion):
        self.__direccion = direccion
 
    def settelefono(self, telefono):
        self.__telefono = telefono
    
    def agregarSala(self, sala_nueva):
        self.__ListadoSala.append(sala_nueva)
        print(f"Sala {sala_nueva.getid()} agregada correctamente.")
 
    def agregarMedico(self, medico_nuevo):
        self.__ListadoMedico.append(medico_nuevo)
        print(f"Médico {medico_nuevo.getnombre()} agregado correctamente.")
 
    def agregarPaciente(self, paciente_nuevo):
        self.__ListadoPaciente.append(paciente_nuevo)
        print(f"Paciente {paciente_nuevo.getnombre()} agregado correctamente.")
    
    def showSalas(self):
        if len(self.__ListadoSala) == 0:
            print("No hay salas registradas.")
        else:
            print("\nSALAS")
            for sala in self.__ListadoSala:
                print(f"ID:{sala.getid()}\nCamas: {sala.getCantidad_C()}")
    
    def showPacientes(self):
        if len(self.__ListadoPaciente) == 0:
            print("No hay pacientes registrados.")
        else:
            print("\nPACIENTES")
            for p in self.__ListadoPaciente:
                print(f"Nombre:{p.getnombre()}\nRUT:{p.getrut()}\nEdad:{p.getedad()}")
    
    def showMedicos(self):
        if len(self.__ListadoMedico) == 0:
            print("No hay médicos registrados.")
        else:
            print("\nMÉDICOS")
            for m in self.__ListadoMedico:
                print(f"Nombre:{m.getnombre()}\nRUT:{m.getrut()}\nEspecialidad:{m.getespecialidad()}")
    
    def buscarSala(self, id):
        sala_encontrada = None
        for sala in self.__ListadoSala:
            if sala.getid() == id:
                sala_encontrada = sala
                break

        if sala_encontrada is None:
            print(f"El ID {id} no corresponde a ninguna sala registrada.")
            return
    
        print(f"\n---SALA {id}---")
        pacientes_en_sala = sala_encontrada.getListadoPaciente()

        if len(pacientes_en_sala) == 0:
            print("Sin pacientes asignados.")
        else:
            for paciente in pacientes_en_sala:
                print(f"Nombre Paciente:{paciente.getnombre()}\nRUT:{paciente.getrut()}")
                medico = self.__buscarMedicoDeUnPaciente(paciente.getrut())
                if medico:
                    print(f"Médico tratante → Nombre:{medico.getnombre()}\nRUT:{medico.getrut()}")
                else:
                    print("Médico sin asignar")
    
    def buscarPaciente(self, rut):
        paciente_encontrado = None
        for p in self.__ListadoPaciente:
            if p.getrut() == rut:
                paciente_encontrado = p
                break
        
        if paciente_encontrado is None:
            print(f"El RUT {rut} no está registrado en el sistema.")
            return
        
        print(f"\n---Paciente:{paciente_encontrado.getnombre()}---")

        print(f"RUT:{paciente_encontrado.getrut()}\nEdad:{paciente_encontrado.getedad()}")

        sala = self.__buscarSalaDeUnPaciente(rut)

        if sala:
            print(f"Sala asignada:{sala.getid()}")
        else:
            print("Sala no asignada")
 
        medico = self.__buscarMedicoDeUnPaciente(rut)

        if medico:
            print(f"Médico desigando:{medico.getnombre()}\nRUT:{medico.getrut()}")
        else:
            print("Médico no designado")

    def buscarMedico(self, rut):
        medico_encontrado = None

        for m in self.__ListadoMedico:
            if m.getrut() == rut:
                medico_encontrado = m
                break
 
        if medico_encontrado is None:
            print(f"El RUT {rut} no está registrado como médico en el sistema.")
            return
 
        print(f"\n---Médico: {medico_encontrado.getnombre()}---")
        print(f"RUT:{medico_encontrado.getrut()}\nEspecialidad:{medico_encontrado.getespecialidad()}")
 
        pacientes = medico_encontrado.getListadoPacientes()

        if len(pacientes) == 0:
            print("Sin pacientes asignados.")
        else:
            for paciente in pacientes:
                print(f"\nNombre_Paciente:{paciente.getnombre()}\nRUT:{paciente.getrut()}")
                sala = self.__buscarSalaDeUnPaciente(paciente.getrut())
                if sala:
                    print(f"ID Sala asignada:{sala.getid()}")
                else:
                    print("Sala no asiganda")
    
    def asignarPacienteMedico(self, rut_medico, rut_paciente):
        medico = None

        for m in self.__ListadoMedico:
            if m.getrut() == rut_medico:
                medico = m
                break
 
        if medico is None:
            print(f"El médico con RUT {rut_medico} no está registrado.")
            return
 
        paciente = None
        for p in self.__ListadoPaciente:
            if p.getrut() == rut_paciente:
                paciente = p
                break
 
        if paciente is None:
            print(f"El paciente con RUT {rut_paciente} no está registrado.")
            return
 
        medico.asignarpaciente(paciente)
        print(f"Paciente {paciente.getnombre()} asignado al médico {medico.getnombre()}.")
    
    def asignarPacienteSala(self, id_sala, rut_paciente):
        sala = None

        for s in self.__ListadoSala:
            if s.getid() == id_sala:
                sala = s
                break
 
        if sala is None:
            print(f"La sala con ID {id_sala} no está registrada.")
            return
 
        paciente = None
        for p in self.__ListadoPaciente:
            if p.getrut() == rut_paciente:
                paciente = p
                break
 
        if paciente is None:
            print(f"El paciente con RUT {rut_paciente} no está registrado.")
            return
 
        sala.asignarpaciente(paciente)

    def __buscarMedicoDeUnPaciente(self, rut_paciente):
        for medico in self.__ListadoMedico:
            for p in medico.getListadoPacientes():
                if p.getrut() == rut_paciente:
                    return medico
        return None
 
    def __buscarSalaDeUnPaciente(self, rut_paciente):
        for sala in self.__ListadoSala:
            for p in sala.getListadoPaciente():
                if p.getrut() == rut_paciente:
                    return sala
        return None
    
    def consulta1_pacientesConAsignacion(self):
        count = 0

        for p in self.__ListadoPaciente:
            tiene_medico = self.__buscarMedicoDeUnPaciente(p.getrut()) is not None
            tiene_sala = self.__buscarSalaDeUnPaciente(p.getrut()) is not None
            if tiene_medico or tiene_sala:
                count += 1
        print(f"\nPacientes con al menos una asignación:{count}")
        return count
    
    def consulta2_comitesMedicos(self):
        total = len(self.__ListadoMedico)
        cirujanos = sum(1 for m in self.__ListadoMedico if "cirujano" in m.getespecialidad().lower())
        no_cirujanos = total - cirujanos
        total_comites = comb(total, 3)
        sin_cirujano = comb(no_cirujanos, 3)
        resultado = total_comites - sin_cirujano
 
        print(f"\nMédicos totales:{total}\nCirujanos:{cirujanos}")

        print(f"Comités posibles con al menos un cirujano:{resultado}")
        return resultado
    
    def consulta3_asignacionesDistintas(self):
        m = len(self.__ListadoMedico)
        p = len(self.__ListadoPaciente)
        s = len(self.__ListadoSala)

        resultado = m * p * s

        print(f"\nMédicos: {m}\nPacientes: {p}\nSalas: {s}")

        print(f"Asignaciones distintas (médico, paciente, sala): {resultado}")
        return resultado
    
    def consulta4_personasVisibles(self):
        m = len(self.__ListadoMedico)
        p = len(self.__ListadoPaciente)

        resultado = m + p  

        print(f"\nMédicos: {m}\nPacientes: {p}")

        print(f"Personas visibles (Médicos o Pacientes): {resultado}")
        return resultado
    
    def consulta5_minimosPacientesPorSala(self):
        s = len(self.__ListadoSala)
        p = len(self.__ListadoPaciente)

        if s == 0:
            print("\nNo hay salas registradas.")
            return 0

        minimo = -(-p // s) 

        print(f"\nPacientes: {p}\nSalas:{s}")
        print(f"Mínimo de pacientes por sala:{minimo}")
        return minimo
    
    def consulta6_probabilidadPacienteConMedico(self):
        total = len(self.__ListadoPaciente)

        if total == 0:
            print("\nNo hay pacientes registrados.")
            return 0.0
        con_medico = sum(
            1 for p in self.__ListadoPaciente
            if self.__buscarMedicoDeUnPaciente(p.getrut()) is not None
        )

        prob = con_medico / total

        print(f"\nPacientes con médico:{con_medico}\nTotal:{total}")
        print(f"Probabilidad: {prob:.4f} ({prob*100:.2f}%)")
        return prob
    
    def consulta7_probabilidadSalaDadoMedico(self):
        con_medico = [
            p for p in self.__ListadoPaciente
            if self.__buscarMedicoDeUnPaciente(p.getrut()) is not None
        ]

        if len(con_medico) == 0:
            print("\nNingún paciente tiene médico asignado.")
            return 0.0
        
        con_medico_y_sala = sum(1 for p in con_medico if self.__buscarSalaDeUnPaciente(p.getrut()) is not None)

        prob = con_medico_y_sala / len(con_medico)

        print(f"\nCon médico:{len(con_medico)}\nCon médico Y sala:{con_medico_y_sala}")
        print(f"P(sala/médico): {prob:.4f} ({prob*100:.2f}%)")
        return prob