import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from server import app
from data import subjects, semesters

layout = html.Div([
	dcc.Location(id='main', refresh=True),
	html.Div([
		html.P([
			'Inserte sus asignaturas'
		], className='sign'),
        html.H1([
            dcc.Dropdown(
                options=semesters,
                multi=True,
                searchable=True,
                placeholder='Semestres de tus ramos'
            )
        ], className='un'),
		html.H1([
            dcc.Dropdown(
            options=subjects,
            multi=True,
            searchable=True,
            placeholder='Ramos'
            )
		], className='un'),
		html.Button(children='Login', n_clicks=0, type='submit', className='submit')
	], className='main'),
	html.Div(id='output-state',children='')
])
