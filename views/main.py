import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from server import app
from datapy import subjects, semesters, schedUpdate
import csv
import sqlite3

layout = html.Div([
	dcc.Location(id='main', refresh=True),
	html.Div([
		html.P([
			'Generador de horario'
		], className='sign'),
        html.H1([
            dcc.Dropdown(
                options=semesters,
                multi=True,
                searchable=True,
                placeholder='Semestres de tus ramos',
				optionHeight=50,
				persistence=True,
				persistence_type='session',
				className='select_box'
            )
        ], className='un'),
		html.H1([
            dcc.Dropdown(
				id='dropdown-s',
	            options=subjects,
	            multi=True,
	            searchable=True,
	            placeholder='Ramos',
				optionHeight=50,
				persistence=True,
				persistence_type='session',
				className='select_box',
            )
		], className='un'),
		html.Button(
			id='generate-button',
			children='Generar',
			n_clicks=0,
			type='submit',
			className='button'
		)
	], className='main'),
	html.Div(id='output-state')
])

@app.callback(
	Output('output-state', 'children'),
	[Input('dropdown-s', 'value')]
)
def update_output(value):
	conn = sqlite3.connect('data.db')
	cur = conn.cursor()
	cur.execute(f'UPDATE data SET chosen = 0')

	dataQuery = []
	for i in value:
		cur.execute(f'UPDATE data SET chosen = 1 WHERE code IS "{i}"')
		cur.execute(f'''SELECT chosen, name, schedule, days FROM data WHERE code IS "{i}" ''')
		aux = cur.fetchall()
		dataQuery.append(aux)	

	conn.commit()
	cur.close()
	print(dataQuery)


	H = [t for t in range(1, 12)]
	hora = [f'{h}:15 - {h+1}:00' for h in range(8, 19)]
	L = ['' for l in range(1, 12)]
	M = ['' for m in range(1, 12)]
	X = ['' for x in range(1, 12)]
	J = ['' for j in range(1, 12)]
	V = ['' for v in range(1, 12)]

	L[4] = 'Tshh'
	
	# outQuery = cur.fetchall()
	# dataQuery = []
	# for i in outQuery:
	# 	dataQuery.append(i[0])
	# for i in data:
	# 	days[schedule] = name

	# dataQuery[0][0]
	# ('Cálculo I[6]', 'M-J', '0-1, 0-1')

	# dataQuery[0][0][1] == Days
	# dataQuery[0][0][2] == Schedule

	with open('sched_data.csv', 'w') as file:
		file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		file.writerow(['H', 'Horario', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'])
		for i in range(0, 11):
			file.writerow([f'{H[i]}', f'{hora[i]}', f'{L[i]}', f'{M[i]}', f'{X[i]}', f'{J[i]}', f'{V[i]}'])

	return f'You have selected {value}!'



# for i in range(0,11):
#     if i == None or i == ' ':
#         L[i] = '1'



@app.callback(
	Output('main', 'pathname'),
	[Input('generate-button', 'n_clicks'),
	Input('dropdown-s', 'subjects')]
)
def horario(n_clicks, subjects):
	if n_clicks > 0:
		return '/horario'