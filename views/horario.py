import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

from server import app
from datapy import subjects, semesters, table
import pandas as pd
import sqlite3

df = pd.read_csv('sched_data.csv')
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

df = pd.read_sql("SELECT name FROM data WHERE chosen IS TRUE", conn)

layout = html.Div([
    dcc.Location(id='horario', refresh=True),
    html.Div([
        html.H1(id='hh'),
        dash_table.DataTable(
            id='dataTable',
            columns=[{'name': day, 'id': day} for day in table],
            data=df.to_dict('records'),
            style_header={
                'backgroundColor': '#28242e',
                'fontWeight': 'lighter',
                'color': 'white',
            },
            style_cell={
                'font-size': '15px',
                'font_family': 'normal',
                'height': 'auto',
                'maxWidth': '111px',
                'textOverflow': 'ellipsis',
                'overflow': 'hidden'

            },
            style_cell_conditional=[
            {
            'if': {'column_id': 'H'},
            'width': '50px'
            },
            {
                'if': {'column_id': 'Horario'},
                    'width': '11%'
            },
            {
                'if': {'column_id': 'Lunes'},
                    'width': '110px'
            },
            {
                'if': {'column_id': 'Martes'},
                    'width': '110px'
            },
            {
                'if': {'column_id': 'Miércoles'},
                    'width': '110px'
            },
            {
                'if': {'column_id': 'Jueves'},
                    'width': '110px'
            },
            {
                'if': {'column_id': 'Viernes'},
                    'width': '110px'
            },
            {'textAlign': 'center'}
            ],
            style_table={
                'height': '300px',
                'minWidth': '100%'
            }
        ),
        html.Div(id='output')
    ]),
])

# @app.callback(
#     Output('table', 'children'),
#     [Input()]
# )

# @app.callback(
#     Output('output', 'children'),
#     [Input('hh', 'ramosValue')]
# )
# def update_data():
#     with open('ramos.csv', 'r') as file:
#         reader = csv.reader(file)
#         ramosValue = list(reader)
#     return ramosValue
