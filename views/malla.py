import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

from server import app
from datapy import subjects, semesters, ramos

def year_button(column, value):
    left = 18
    column *= 204
    return html.Button(
        children=f'Año {value}',
        n_clicks=0,
        className='year',
        style={
            'left': f'{left + column}px'
        })

def semester_button(column, value):
    left = 18
    column *= 102
    return html.Button(
        children=value,
        n_clicks=0,
        className='semester',
        style={
            'left': f'{left + column}px'
        })

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
                year_button(0, 1),
                year_button(1, 2),
                year_button(2, 3),
                year_button(3, 4),
                year_button(4, 5),
                html.Button(
                    children='Año 5 1/2',
                    n_clicks=0,
                    className='year--1-2'),
                semester_button(0, 'I'),
                semester_button(1, 'II'),
                semester_button(2, 'III'),
                semester_button(3, 'IV'),
                semester_button(4, 'V'),
                semester_button(5, 'VI'),
                semester_button(6, 'VII'),
                semester_button(7, 'VIII'),
                semester_button(8, 'IX'),
                semester_button(9, 'X'),
                semester_button(10, 'XI'),
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
                subject(name='Electro - magnetismo Aplicado', color='#A51C30', column=3, row=2),
                subject(name='Programación II', color='#4db848', column=3, row=3),
                subject(name='Complementario 1', color='#609B89', column=3, row=4),

                # Semestre V
                subject(name='Estadística', color='#4e88c7', column=4, row=0),
                subject(name='Mecánica y Termodinámica', color='#A51C30', column=4, row=1),
                subject(name='Estructuras de datos', color='#4db848', column=4, row=2),
                subject(name='Electivo 1', color='#609B89', column=4, row=3),
                subject(name='Complementario 2', color='#609B89', column=4, row=4),

                # Semestre VI
                subject('Economía', '#93a1ad', 5, 0),
                subject('Teoría de Computación', '#4db848', 5, 1),
                subject('Arquitectura de Computadores', '#4db848', 5, 2),
                subject('Bases de Datos I', '#4db848', 5, 3),
                subject('Complementaria 3', '#609B89', 5, 4),

                # Semestre VII
                subject('Formulación y Evaluación de Proyectos', '#609B89', 6, 0),
                subject('Sistemas Operativos', '#4db848', 6, 1),
                subject('Análisis de Algoritmos', '#4db848', 6, 2),
                subject('Electivo 2', '#609B89', 6, 3),
                subject('Complementario 4', '#609B89', 6, 4),

                # Semestre VIII
                subject('Gestión de Empresas', '#93a1ad', 7, 0),
                subject('Optimización I', '#4e88c7', 7, 1),
                subject('Redes de Computadores', '#4db848', 7, 2),
                subject('Ingeniería de Software I', '#4db848', 7, 3),
                subject('Electivo 3', '#609B89', 7, 4),

                # Semestre IX
                subject('Ingeniería de Software II', '#4db848', 8, 0),
                subject('Inteligencia Artificial', '#4db848', 8, 1),
                subject('Informática y Sociedad', '#4db848', 8, 2),
                subject('Gestión Informática', '#4db848', 8, 3),
                subject('Electivo 4', '#609B89', 8, 4),

                # Semestre X
                subject('Proyecto Informático', '#000000', 9, 0),
                subject('Memoria de Título', '#000000', 9, 1),
                subject('Electivo 5', '#609B89', 9, 2),
                subject('Electivo 6', '#609B89', 9, 3),

                # Semestre XI
                subject('Electivo 7', '#609B89', 10, 0),
                subject('Electivo 8', '#609B89', 10, 1)
            ]),
        ], className='canvas'),
    ], className='col'),
], className='container-fluid')
