import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

from server import app
from data import subjects, semesters, ramos

def year_button(value):
    return html.Button(
        children=f'Año {value}',
        n_clicks=0,
        className='year')

def semester_button(value):
    return html.Button(
        children=value,
        n_clicks=0,
        className='semester'
    )

layout = html.Section([
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    year_button(1),
                    year_button(2),
                    year_button(3),
                    year_button(4),
                    year_button(5),
                    html.Button(
                        children='Año 5 1/2',
                        n_clicks=0,
                        className='year--1-2'),
                    semester_button('I'),
                    semester_button('II'),
                    semester_button('III'),
                    semester_button('IV'),
                    semester_button('V'),
                    semester_button('VI'),
                    semester_button('VII'),
                    semester_button('VIII'),
                    semester_button('IX'),
                    semester_button('X'),
                    semester_button('XI'),
                ])
            ], className='canvas')
        ], className='col')
    ], className='row')
], className='container-fluid')
