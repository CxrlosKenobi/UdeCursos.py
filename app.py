# index page
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from server import app, server
from views import main, horario, malla

header = html.Div([
    html.Img(
        src='assets/udeconline.png',
        className='banner-img'
    ),
    html.H2(
        'Malla Interactiva',
        className='banner-title'
    ),
    dbc.Nav(
        [
            dbc.NavLink(
                'Generador de Horario',
                href='/',
                active='exact',
                className='banner-button-h'
            ),
            dbc.NavLink(
                'Mi horario',
                href='/horario',
                className='banner-button-mh'
            ),
            dbc.NavLink(
                'Malla',
                href='/malla',
                active='exact',
                className='banner-button-m'
            ),
        ],
        pills=True
    ),
    html.H1(
        'Ingeniería Civil Informática',
        className='banner-h1'
    ),
    html.P(
        'UdeC - 2021',
        className='banner-p'
    ),
], className='banner')

app.layout = html.Div([
	header,
	html.Div(id='page-content', className='content'),
	dcc.Location(id='url', refresh=False)
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return main.layout
    elif pathname == '/horario':
        return horario.layout
    elif pathname == '/malla':
        return malla.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
