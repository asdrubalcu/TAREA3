import cursos

profesores = []

def agregar_profesor(cedula, nombre, curso):
    # Validar cédula única
    for p in profesores:
        if p['cedula'] == cedula:
            print("Error: Ya existe un profesor con esa cédula.")
            return

    # Validar existencia del curso
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
