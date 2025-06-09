# main.py

import alumnos
import profesores
import cursos
import reportes

def menu():
    while True:
        print("\nSistema Escolar")
        print("1. Agregar / Consultar Alumnos")
        print("2. Agregar / Consultar Profesores")
        print("3. Ver / Agregar / Eliminar Cursos")
        print("4. Ver Reportes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            subopcion = input("1) Agregar Alumno\n2) Consultar Alumnos\nSeleccione una opción: ").lower()
            if subopcion == '1':
                nombre = input("Nombre del alumno: ")
                cedula = input("Cédula del alumno: ")
                curso = input("Código del curso: ")

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

        elif opcion == '2':
            subopcion = input("1) Agregar Profesor\n2) Consultar Profesores\nSeleccione una opción: ").lower()
            if subopcion == '1':
                cedula = input("Cédula del profesor: ")
                nombre = input("Nombre del profesor: ")
                curso = input("Código del curso asignado: ")

                if cursos.curso_existe(curso):
                    profesores.agregar_profesor(cedula, nombre, curso)
                else:
                    print("Error: El curso no existe.")

            elif subopcion == '2':
                print("\nLista de profesores:")
                for p in profesores.consultar_profesores():
                    print(p)

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

        elif opcion == '4':
            subopcion = input("\n1) Reporte general\n2) Reporte por estudiante\n3) Reporte por curso\nSeleccione una opción: ").lower()

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

            elif subopcion == '2':
                cedula = input("Ingrese la cédula del estudiante: ")
                reportes.reporte_por_estudiante(cedula)

            elif subopcion == '3':
                codigo = input("Ingrese el código del curso: ")
                reportes.reporte_por_curso(codigo)

        elif opcion == '5':
            print("Gracias por usar el sistema escolar.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()

