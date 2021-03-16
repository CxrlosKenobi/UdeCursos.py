import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

from server import app
from data import subjects, semesters, table

layout = html.Div([
    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{'name': day, 'id': day} for day in table],
            style_header={
                'backgroundColor': '#28242e',
                'fontWeight': 'lighter',
                'color': 'white',
            },
            style_cell_conditional=[{
                'textAlign': 'center'
            }],
            style_table={
                'height': '300px'
            }
        )
    ])
])
