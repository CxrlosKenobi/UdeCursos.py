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

auxgateValue = []
def getData(vaList): # vaList = ValueList abbreviation
	conn = sqlite3.connect('data.db')
	cur = conn.cursor()

	dataQuery = []
	for i in vaList:
		cur.execute(f'''SELECT name, schedule, days FROM data WHERE code IS "{i}" ''')
		aux = cur.fetchall()
		dataQuery.append(aux)
	# outQuery = cur.fetchall()
	# dataQuery = []
	# for i in outQuery:
	# 	dataQuery.append(i[0])
	conn.commit()
	cur.close()
	print(dataQuery)

	for i in dataQuery:
		i[0][1]
	
	for i in data:
		days[schedule] = name

	with open('sched_data.csv', 'w') as file:
    	file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    	file.writerow(['H', 'Horario', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'])
    for i in range(0, 11):
        file.writerow([f'{H[i]}', f'{hora[i]}', f'{L[i]}', f'{M[i]}', f'{X[i]}', f'{J[i]}', f'{V[i]}'])

	return dataQuery


@app.callback(
	Output('output-state', 'children'),
	[Input('dropdown-s', 'value')]
)
def update_output(value):
	with open('ramos.csv', 'w') as file:
		file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		file.writerow(value)
	# schedUpdate(codes=value)
	auxgateValue = value
	getData(value)
	return f'You have selected {value}!'
try:
	getData(auxgateValue)
except sqlite3.OperationalError:
	print('sqlite3 Operational Error - Warning')
	pass

@app.callback(
	Output('main', 'pathname'),
	[Input('generate-button', 'n_clicks'),
	Input('dropdown-s', 'subjects')]
)
def horario(n_clicks, subjects):
	if n_clicks > 0:
		return '/horario'