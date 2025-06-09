import cursos

profesores = []

def agregar_profesor(cedula, nombre, curso):
    for p in profesores:
        if p['cedula'] == cedula:
            print("Error: Ya existe un profesor con esa cédula.")
            return

    if not cursos.curso_existe(curso):
        print("Error: El curso no existe.")
        return

    profesor = {
        'cedula': cedula,
        'nombre': nombre.upper(),
        'curso': curso
    }
    profesores.append(profesor)
    print("Profesor agregado correctamente.")

def consultar_profesores():
    return profesores
