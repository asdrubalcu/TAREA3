cursos = []

def agregar_curso(codigo, nombre):
    for c in cursos:
        if c['codigo'] == codigo:
            print("Error: Ya existe un curso con ese código.")
            return
    curso = {
        'codigo': codigo,
        'nombre': nombre
    }
    cursos.append(curso)
    print("Curso agregado correctamente.")

def eliminar_curso(codigo):
    for c in cursos:
        if c['codigo'] == codigo:
            cursos.remove(c)
            print("Curso eliminado.")
            return
    print("Error: Curso no encontrado.")

def consultar_cursos():
    return cursos

def curso_existe(codigo):
    for c in cursos:
        if c['codigo'] == codigo:
            return True
    return False
