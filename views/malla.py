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

def subject(name, color, column, row):
    row *= 75
    column *= 105
    return html.Button(
        id='subject-button',
        children=name,
        n_clicks=0,
        className='ramo',
        style={
            'background-color': f'{color}',
            'top': f'{215+row}px',
            'left': f'{87+column}px',
        }
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
                ]),
                html.Div([
                    # Semestre I
                    subject(name='Cálculo I', color='#284ABF', column=0, row=0),
                    subject(name='Álgebra I', color='#284ABF', column=0, row=1),
                    subject(name='Física I', color='#572364', column=0, row=2),
                    subject(name='Química General I', color='#EB8C04', column=0, row=3),
                    subject(name='Intro. a la Ingeniería Informática', color='#609B89', column=0, row=4),

                    # Semestre II
                    subject(name='Cálculo II', color='#284ABF',column=1, row=0),
                    subject(name='Álgebra II', color='#284ABF', column=1, row=1),
                    subject(name='Física II', color='#572364', column=1, row=2),
                    subject(name='Intro. al Desarrollo de Soluciones Informáticas', color='#609B89', column=1, row=3),
                    subject(name='Intro. a la Innovación en Ingeniería', color='#609B89', column=1, row=4),
                ]),
            ], className='canvas')
        ], className='col')
    ], className='row')
], className='container-fluid')
