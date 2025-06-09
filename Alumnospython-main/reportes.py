import alumnos
import profesores
import cursos

def reporte_por_estudiante(cedula):
    encontrado = False
    for a in alumnos.alumnos:
        if a['cedula'] == cedula:
            print(f"\nNombre     : {a['nombre']}")
            print(f"Cédula     : {a['cedula']}")
            print(f"Curso      : {a['curso']}")
            print(f"Nota       : {a['nota']}")
            encontrado = True
    if not encontrado:
        print("Estudiante no encontrado.")

def reporte_por_curso(codigo):
    curso_info = None
    for c in cursos.cursos:
        if c['codigo'] == codigo:
            curso_info = c
            break

    if not curso_info:
        print("Curso no encontrado.")
        return

    print(f"\nCurso: {curso_info['codigo']} - {curso_info['nombre']}")

    profe = None
    for p in profesores.profesores:
        if p['curso'] == codigo:
            profe = p
            break

    if profe:
        print(f"Profesor asignado: {profe['nombre']} ({profe['cedula']})")
    else:
        print("No hay profesor asignado.")

    print("\nEstudiantes del curso:")
    hay_estudiantes = False
    for a in alumnos.alumnos:
        if a['curso'] == codigo:
            print(f"{a['cedula']} - {a['nombre']} - Nota: {a['nota']}")
            hay_estudiantes = True

    if not hay_estudiantes:
        print("No hay estudiantes inscritos en este curso.")
