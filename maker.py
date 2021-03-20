import csv

H = [i for i in range(1, 14)]
hora = [f'{i}:15 - {i+1}:00' for i in range(8, 19)]
L = []
M = []
X = []
J = []
V = []

with open('sched_data.csv', 'w') as file:
    fieldnames = ['H', 'Horario', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    file.writerow([f'{H}', f'{hora}', f'{L}', f'{M}', f'{X}', f'{J}', f'{V}'])
    # file.writerow([f'{}', f'{}', f'{}', f'{}', f'{}', f'{}', f'{}'])
