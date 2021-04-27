# Horario de SECAD
## SECAD (PDF) a CSV
## CSV a SQLAlchemy 
from csv import reader
import csv

# H = [t for t in range(1, 12)]
# hora = [f'{h}:15 - {h+1}:00' for h in range(8, 19)]
# L = ['' for l in range(1, 12)]
# M = ['' for m in range(1, 12)]
# X = ['' for x in range(1, 12)]
# J = ['' for j in range(1, 12)]
# V = ['' for v in range(1, 12)]

# for i in range(0,11):
#     if i == None or i == ' ':
#         L[i] = '1'



# with open('ramos.csv', 'r') as obj:
#     for row in reader(obj):
#         a = True

sched_L = [
    {'code': '503120-1', 'sched': 2},
    {'code': '503120-1', 'sched': 3}
]

sched_M = [
    {'code': '525140-6', 'sched': 0}, # Algebra I
    {'code': '527140-6', 'sched': 1},
    {'code': '527140-6', 'sched': 2}, # Calculo I
    {'code': '527140-6', 'sched': 3}
]

sched_X = [
    {'code': '531140-9', 'sched': 0}, # Quimica General I
    {'code': '531140-9', 'sched': 1},
    {'code': '510140-8', 'sched': 2}, # Fisica I
    {'code': '510140-8', 'sched': 3}
]
#L[5] = 'Intro. Ing Informática'
#L[3] = 'Intro. Ing Informática'

def scheds():
    L[2] = 'Intro. Ing Informática'

    M[0] = 'Cálculo I'
    M[1] = 'Cálculo I'
    M[2] = 'Álgebra I'
    M[3] = 'Álgebra I'
    M[5] = 'CADE Álgebra I'
    M[6] = 'CADE Álgebra I'
    M[7] = 'Álgebra I Lab'
    M[8] = 'Álgebra I Lab'

    X[0] = 'Química General I'
    X[1] = 'Química General I'
    X[2] = 'Física I'
    X[3] = 'Física I'
    X[4] = 'CADE Química General I'
    X[5] = 'CADE Química General I'
    X[7] = 'Cálculo I Lab'
    X[8] = 'Cálculo I Lab'

    J[0] = 'Cálculo I'
    J[1] = 'Cálculo I'
    J[2] = 'Álgebra I'
    J[3] = 'Álgebra I'
    J[7] = 'CADE Física I'
    J[8] = 'CADE Física I'

    V[0] = 'Química General I'
    V[1] = 'Química General I'
    V[4] = 'Física I'
    V[7] = 'Química General I Lab'
    V[8] = 'Química General I Lab'


subjects = [
    {'label': 'Fisica I[8]', 'value': '510140-8'},
    {'label': 'Física I[7]', 'value': '510140-7'},
    {'label': 'Física I[6]', 'value': '510140-6'},
    {'label': 'Álgebra I[8]', 'value': '525140-8'},
    {'label': 'Álgebra I[7]', 'value': '525140-7'},
    {'label': 'Álgebra I[6]', 'value': '525140-6'},
    {'label': 'Álgebra I[5]', 'value': '525140-7'},
    {'label': 'Álgebra I[4]', 'value': '525140-7'},
    {'label': 'Álgebra I[3]', 'value': '525140-7'},
    {'label': 'Álgebra I[2]', 'value': '525140-7'},
    {'label': 'Álgebra I[1]', 'value': '525140-7'},
    {'label': 'Cálculo I[6]', 'value': '527140-6'},
    {'label': 'Cálculo I[5]', 'value': '527140-5'},
    {'label': 'Cálculo I[4]', 'value': '527140-4'},
    {'label': 'Química General I[9]', 'value': '531140-9'},
    {'label': 'Química General I[8]', 'value': '531140-8'},
    {'label': 'Indu. a la vida universitaria', 'value': '890191-1'},
    {'label': 'Intr. a la Ingeniería Informática', 'value': '503120-1'}
]


def schedUpdate(codes):
    # Just creating the blank spaces ; reseting
    L = ['' for l in range(1, 12)]
    M = ['' for m in range(1, 12)]
    X = ['' for x in range(1, 12)]
    J = ['' for j in range(1, 12)]
    V = ['' for v in range(1, 12)]
    days = ['L', 'M', 'X', 'J', 'V']

    for i in sched_L:
        for j in subjects:
            if list(j.values())[1] == list(i.values())[0]:
                name = list(j.values())[1]
        if list(i.values())[0] in codes:
            L[list(i.values())[1]] = name

    for i in sched_M:
        for j in subjects:
            if list(j.values())[1] == list(i.values())[0]:
                name = list(j.values())[1]
        if list(i.values())[0] in codes:
            M[list(i.values())[1]] = name

    for i in sched_X:
        for j in subjects:
            if list(j.values())[1] == list(i.values())[0]:
                name = list(j.values())[1]
        if list(i.values())[0] in codes:
            X[list(i.values())[1]] = name

    return L, M, X, J, V




semesters = [
    {'label': 'I', 'value':'I'},
    {'label': 'II', 'value':'II'},
    {'label': 'III', 'value':'III'},
    {'label': 'IV', 'value':'IV'},
    {'label': 'V', 'value':'V'},
    {'label': 'VI', 'value':'VI'},
    {'label': 'VII', 'value':'VII'},
    {'label': 'VIII', 'value':'VIII'},
    {'label': 'IX', 'value':'IX'},
]

ramos = [
    {'name': ['Año 1', 'I', 'Álgebra I'], 'id': '1'},
    {'name': ['Año 1', 'II', 'Álgebra II'], 'id': '2'},
    {'name': ['Año 2', 'III', 'Cálculo III'], 'id': '3'},
    {'name': ['Año 2', 'IV', 'Programación II'], 'id': '4'},
    {'name': ['Año 3', 'V', 'Economía'], 'id': '5'},
    {'name': ['Año 3', 'VI', 'Estadísticas'], 'id': '6'},
    {'name': ['Año 4', 'VII', 'Sistemas Operativos'], 'id': '7'},
    {'name': ['Año 4', 'VIII', 'Optimización I'], 'id': '8'},
    {'name': ['Año 5', 'IX', 'Inteligencia Artificial'], 'id': 'codigo'},
    {'name': ['Año 5', 'X', 'Memoria de Título I'], 'id': '9'},
    {'name': ['Año 5 1/2', 'XI', 'Memoria de Título II'], 'id': '10'},

]

table = ['H', 'Horario', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

# with open('sched_data.csv', 'w') as file:
#     file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     file.writerow(['H', 'Horario', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'])
#     for i in range(0, 11):
#         file.writerow([f'{H[i]}', f'{hora[i]}', f'{L[i]}', f'{M[i]}', f'{X[i]}', f'{J[i]}', f'{V[i]}'])

