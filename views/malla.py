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
        className='semester')

def subject(name, color, column, row):
    max_fsize = 11 if len(name.split(' ')[0]) > 12 else 12
    row *= 80 # 75
    column *= 102 # 105
    return html.Button(
        id='subject-button',
        children=name,
        n_clicks=0,
        className='ramo',
        style={
            'background-color': f'{color}',
            'top': f'{90+row}px',
            'left': f'{18+column}px',
            'font-size': f'{max_fsize}px'
        }
    )

layout = html.Section([
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
                subject(name='Cálculo II', color='#284ABF', column=1, row=0),
                subject(name='Álgebra II', color='#284ABF', column=1, row=1),
                subject(name='Física II', color='#572364', column=1, row=2),
                subject(name='Intro. al Desarrollo de Soluciones Informáticas', color='#609B89', column=1, row=3),
                subject(name='Intro. a la Innovación en Ingeniería', color='#609B89', column=1, row=4),

                # Semestre III
                subject(name='Cálculo III', color='#284ABF', column=2, row=0),
                subject(name='Ecuaciones Diferenciales Ordinarias', color='#4e88c7', column=2, row=1),
                subject(name='Lógica', color='#A51C30', column=2, row=2),
                subject(name='Programación I', color='#4db848', column=2, row=3),

                # Semestre IV
                subject(name='Cálculo Númerico', color='#4e88c7', column=3, row=0),
                subject(name='Matemáticas Discretas', color='#4e88c7', column=3, row=1),
                subject(name='Electromagnetismo Aplicado', color='#A51C30', column=3, row=2),
                subject(name='Programación II', color='#4db848', column=3, row=3),
                subject(name='Complementario 1', color='#609B89', column=3, row=4),

                # Semestre V
                subject(name='Estadística', color='#4e88c7', column=4, row=0),
                subject(name='Mecánica y Termodinámica', color='#A51C30', column=4, row=1),
                subject(name='Estructuras de datos', color='#4db848', column=4, row=2),
                subject(name='Electivo 1', color='#609B89', column=4, row=3),
                subject(name='Complementario 2', color='#609B89', column=4, row=4)
            ]),
        ], className='canvas'),
    ], className='col'),
], className='container-fluid')
