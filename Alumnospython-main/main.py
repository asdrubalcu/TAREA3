# main.py

# Se importan los módulos creados
import alumnos
import profesores
import cursos
import reportes

# Función principal con el menú del sistema
def menu():
    while True:
        # Menú principal
        print("\nSistema Escolar")
        print("1. Agregar / Consultar Alumnos")
        print("2. Agregar / Consultar Profesores")
        print("3. Ver / Agregar / Eliminar Cursos")
        print("4. Ver Reportes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        # Opción 1: Alumnos
        if opcion == '1':
            subopcion = input("1) Agregar Alumno\n2) Consultar Alumnos\nSeleccione una opción: ").lower()
            if subopcion == '1':
                nombre = input("Nombre del alumno: ")
                cedula = input("Cédula del alumno: ")
                curso = input("Código del curso: ")

                # Validar que el curso exista
                if not cursos.curso_existe(curso):
                    print("Error: El curso no existe.")
                    continue

                try:
                    nota = float(input("Nota del alumno: "))
                except ValueError:
                    print("Nota inválida.")
                    continue

                alumnos.agregar_alumno(nombre, cedula, curso, nota)

            elif subopcion == '2':
                print("\nLista de alumnos:")
                for a in alumnos.consultar_alumnos():
                    print(a)

        # Opción 2: Profesores
        elif opcion == '2':
            subopcion = input("1) Agregar Profesor\n2) Consultar Profesores\nSeleccione una opción: ").lower()
            if subopcion == '1':
                cedula = input("Cédula del profesor: ")
                nombre = input("Nombre del profesor: ")
                curso = input("Código del curso asignado: ")

                # Validar que el curso exista
                if cursos.curso_existe(curso):
                    profesores.agregar_profesor(cedula, nombre, curso)
                else:
                    print("Error: El curso no existe.")

            elif subopcion == '2':
                print("\nLista de profesores:")
                for p in profesores.consultar_profesores():
                    print(p)

        # Opción 3: Cursos
        elif opcion == '3':
            subopcion = input("1) Ver Cursos\n2) Agregar Curso\n3) Eliminar Curso\nSeleccione una opción: ").lower()
            if subopcion == '1':
                print("\nCursos disponibles:")
                for c in cursos.consultar_cursos():
                    print(f"{c['codigo']} - {c['nombre']}")

            elif subopcion == '2':
                codigo = input("Código del nuevo curso: ")
                nombre = input("Nombre del curso: ")
                cursos.agregar_curso(codigo, nombre)

            elif subopcion == '3':
                codigo = input("Código del curso a eliminar: ")
                cursos.eliminar_curso(codigo)

        # Opción 4: Reportes
        elif opcion == '4':
            subopcion = input("\n1) Reporte general\n2) Reporte por estudiante\n3) Reporte por curso\nSeleccione una opción: ").lower()

            # Reporte general del sistema
            if subopcion == '1':
                total = alumnos.cantidad_estudiantes()
                promedio = alumnos.promedio_general()
                estadisticas = alumnos.estadisticas()
                print(f"\nTotal de estudiantes: {total}")
                print(f"Promedio general: {promedio:.2f}")
                print(f"Aprobados: {estadisticas['aprobados']}")
                print(f"Aplazados: {estadisticas['aplazados']}")
                print(f"Reprobados: {estadisticas['reprobados']}")
                print(f"Estudiantes con nota superior al promedio: {estadisticas['mayor_que_promedio']}")

            # Reporte por estudiante (muestra materias y promedio)
            elif subopcion == '2':
                cedula = input("Ingrese la cédula del estudiante: ")
                reportes.reporte_por_estudiante(cedula)

            # Reporte por curso (muestra info del curso, profesor, alumnos)
            elif subopcion == '3':
                codigo = input("Ingrese el código del curso: ")
                reportes.reporte_por_curso(codigo)

        # Opción 5: Salir del sistema
        elif opcion == '5':
            print("Gracias por usar el sistema escolar.")
            break

        else:
            print("Opción inválida, intente de nuevo.")

# Ejecutar el menú principal si el archivo es principal
if __name__ == "__main__":
    menu()
