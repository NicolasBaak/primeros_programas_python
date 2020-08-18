#Nos piden diseñar un procedimiento que recibe como datos las dos listas y una cadena con
#el nombre de un estudiante. Si el estudiante pertenece a la clase, el procedimiento imprimirá
#su nombre y nota en pantalla. Si no es un alumno incluido en la lista, se imprimirá un mensaje
#que lo advierta.

def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
    encontrado = False
    for i in range(len(alumnos)):
        if alumnos[i]==alumno_buscado:
            print(alumno_buscado,notas[i])
            return
        if not encontrado:
            print('El alumno {0} no pertenece al grupo.'.format(alumno_buscado))