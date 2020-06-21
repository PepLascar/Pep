import os
os.system ("cls")

import numpy
asignaturas = numpy.empty(6, dtype='object')

for i in range(0,asignaturas.size):
    asignaturas[i] = input("Ingrese asignatura: ")

print(asignaturas)