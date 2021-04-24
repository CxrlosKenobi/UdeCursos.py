import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from server import app
from data import subjects, semesters, schedUpdate
import csv

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
	with open('ramos.csv', 'w') as file:
		file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		file.writerow(value)
	schedUpdate(codes=value)
	return f'You have selected {value}!'

@app.callback(
	Output('main', 'pathname'),
	[Input('generate-button', 'n_clicks'),
	Input('dropdown-s', 'subjects')]
)
def horario(n_clicks, subjects):
	if n_clicks > 0:
		return '/horario'

