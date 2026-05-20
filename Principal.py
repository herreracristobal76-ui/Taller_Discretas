#Martin Fuentes y Cristóbal Herrera

from Hospital.hospital import Hospital
from Hospital.Hijas.medico import Medico
from Hospital.Hijas.paciente import Paciente
from Hospital.sala import Sala

if __name__ == "__main__":

    hospital = Hospital(nombre="Hospital Regional UCM", direccion="Av. San Miguel 3605", telefono=712345678)

    print("Cargando datos de ejemplo...")
    print("-------------------------------------")

    m1 = Medico(rut="12847593-4", edad=47, nombre="Valentina Obreque",  especialidad="Cirujano")
    m2 = Medico(rut="9374821-6",  edad=35, nombre="Rodrigo Inzunza",    especialidad="Cirujano")
    m3 = Medico(rut="15283947-2", edad=54, nombre="Francisca Navarrete",especialidad="Traumatólogo")
    m4 = Medico(rut="8192736-K", edad=42, nombre="Sebastián Llanos",   especialidad="Pediatra")

    p1 = Paciente(rut="17364829-1", edad=34, nombre="Ignacio Rebolledo",  direccion="Pasaje Los Aromos 45",   telefono="912847365")
    p2 = Paciente(rut="16254738-0", edad=27, nombre="Camila Zuñiga",      direccion="Villa Cordillera 210",   telefono="923748291")
    p3 = Paciente(rut="14738291-5", edad=63, nombre="Héctor Mardones",    direccion="Calle Lircay 890",       telefono="934829173")
    p4 = Paciente(rut="19283746-3", edad=19, nombre="Isidora Pizarro",    direccion="Los Boldos 33",          telefono="945918273")
    p5 = Paciente(rut="13847265-8", edad=48, nombre="Mauricio Espinace",  direccion="Av. O'Higgins 1204",     telefono="956273849")

    s1 = Sala(id=1, Cantidad_C=2)
    s2 = Sala(id=2, Cantidad_C=3)
    s3 = Sala(id=3, Cantidad_C=1)

    for m in [m1, m2, m3, m4]:
        hospital.agregarMedico(m)
    for p in [p1, p2, p3, p4, p5]:
        hospital.agregarPaciente(p)
    for s in [s1, s2, s3]:
        hospital.agregarSala(s)

    # Asignaciones de ejemplo
    hospital.asignarPacienteMedico("12847593-4", "17364829-1") 
    hospital.asignarPacienteMedico("12847593-4", "16254738-0") 
    hospital.asignarPacienteMedico("9374821-6",  "14738291-5") 
    hospital.asignarPacienteMedico("15283947-2", "19283746-3")  

    hospital.asignarPacienteSala(1, "17364829-1") 
    hospital.asignarPacienteSala(1, "16254738-0")  
    hospital.asignarPacienteSala(2, "14738291-5")  

    print("Datos de ejemplo cargados correctamente.")

    while True:
        print("\n-------------------------------------------")
        print(f"Menú {hospital.getnombre()}")
        print("-------------------------------------------")
        print("1.  Crear sala")
        print("2.  Crear médico")
        print("3.  Crear paciente")
        print("4.  Ver salas")
        print("5.  Ver médicos")
        print("6.  Ver pacientes")
        print("7.  Buscar por sala")
        print("8.  Buscar por médico")
        print("9.  Buscar por paciente")
        print("10. Asignar paciente a médico")
        print("11. Asignar paciente a sala")
        print("12. Salir")
        print("-------------------------------------------")
        print("12. Consultas")
        print("-------------------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n---Crear Sala---")
            try:
                id_sala = int(input("ID de la sala: "))
                camas   = int(input("Cantidad de camas: "))
                hospital.agregarSala(Sala(id=id_sala, Cantidad_C=camas))
            except ValueError:
                print("ID y camas deben ser números enteros.")

        elif opcion == "2":
            print("\n---Crear Médico---")
            rut = input("RUT: ").strip()
            nombre = input("Nombre: ").strip()
            try:
                edad = int(input("Edad: "))
            except ValueError:
                print("La edad debe ser un número.")
                continue
            especialidad = input("Especialidad: ").strip()
            hospital.agregarMedico(Medico(rut=rut, edad=edad, nombre=nombre, especialidad=especialidad))

        elif opcion == "3":
            print("\n---Crear Paciente---")
            rut = input("RUT: ").strip()
            nombre = input("Nombre: ").strip()
            try:
                edad = int(input("Edad: "))
            except ValueError:
                print("La edad debe ser un número.")
                continue
            direccion = input("Dirección: ").strip()
            telefono  = input("Teléfono: ").strip()
            hospital.agregarPaciente(Paciente(rut=rut, edad=edad, nombre=nombre,
                                              direccion=direccion, telefono=telefono))

        elif opcion == "4":
            hospital.showSalas()

        elif opcion == "5":
            hospital.showMedicos()

        elif opcion == "6":
            hospital.showPacientes()

        elif opcion =="7":
            print("\n---Buscar por Sala---")
            try:
                id_sala = int(input("Ingrese el ID de la sala: "))
                hospital.buscarSala(id_sala)
            except ValueError:
                print("El ID debe ser un número entero.")

        elif opcion == "8":
            print("\n---Buscar por Médico---")
            rut = input("Ingrese el RUT del médico: ").strip()
            hospital.buscarMedico(rut)

        elif opcion == "9":
            print("\n---Buscar por Paciente---")
            rut = input("Ingrese el RUT del paciente: ").strip()
            hospital.buscarPaciente(rut)

        elif opcion == "10":
            print("\n---Asignar Paciente a Médico---")
            rut_medico   = input("RUT del médico: ").strip()
            rut_paciente = input("RUT del paciente: ").strip()
            hospital.asignarPacienteMedico(rut_medico, rut_paciente)

        elif opcion == "11":
            print("\n---Asignar Paciente a Sala--")

            try:
                id_sala = int(input("ID de la sala: "))
            except ValueError:
                print("El ID debe ser un número entero.")
                continue

            rut_paciente = input("RUT del paciente: ").strip()

            hospital.asignarPacienteSala(id_sala, rut_paciente)
        
        elif opcion == "12":
            print("\nSaliendo del sistema. ¡Hasta luego!\n")
            break

        elif opcion == "13":
            print("\n---Consultas---")
            hospital.consulta1_pacientesConAsignacion()
            hospital.consulta2_comitesMedicos()
            hospital.consulta3_asignacionesDistintas()
            hospital.consulta4_personasVisibles()
            hospital.consulta5_minimosPacientesPorSala()
            hospital.consulta6_probabilidadPacienteConMedico()
            hospital.consulta7_probabilidadSalaDadoMedico()


        else:
            print("Opción no válida. Intente nuevamente.")

