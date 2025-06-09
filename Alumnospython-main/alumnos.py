alumnos = []

def agregar_alumno(nombre, cedula, curso, nota):
    for a in alumnos:
        if a['cedula'] == cedula:
            print("Error: Ya existe un alumno con esa cédula.")
            return

    alumno = {
        'nombre': nombre.upper(),
        'cedula': cedula,
        'curso': curso,
        'nota': nota
    }
    alumnos.append(alumno)
    print("Alumno agregado correctamente.")

def consultar_alumnos():
    return alumnos

def cantidad_estudiantes():
    return len(alumnos)

def promedio_general():
    if not alumnos:
        return 0
    total = sum([a['nota'] for a in alumnos])
    return total / len(alumnos)

def estadisticas():
    promedio = promedio_general()
    stats = {'aprobados': 0, 'aplazados': 0, 'reprobados': 0, 'mayor_que_promedio': 0}
    for a in alumnos:
        nota = a['nota']
        if nota >= 70:
            stats['aprobados'] += 1
        elif nota >= 60:
            stats['aplazados'] += 1
        else:
            stats['reprobados'] += 1

        if nota > promedio:
            stats['mayor_que_promedio'] += 1

    return stats
