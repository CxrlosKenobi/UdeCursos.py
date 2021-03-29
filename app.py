#

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
        'UdeCursos.py',
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
                'Malla Interactiva',
                href='/malla',
                active='exact',
                className='banner-button-m'
            ),
        ],
        pills=False
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

footer = html.Div([
    dbc.NavLink([
        html.I(className='fas fa-envelope mr-2'),
        html.A('Contacto'),
    ],
        href='/',
        target='_blank',
        active='exact',
        className='footer-p1'
    ),
    dbc.NavLink([
        html.A(
            'with ',
            style={
                'font-size': '12px'
            }),
        html.I(className='fas fa-heart mr-1'),
        html.A(
            'by Kenobi',
            style={
                'font-size': '12px',
            }),
        html.Br(),
        html.I(className='fab fa-github mr-2'),
        html.Span('Código fuente')
    ],
        href='https://github.com/CxrlosKenobi/',
        target='_blank',
        active='exact',
        className='footer-p2'
    ),
    dbc.NavLink([
        html.Span('Última actualización:'),
        html.Br(),
        html.A('27 Marzo 2021')
    ],
        href='/',
        target='_blank',
        active='exact', 
        className='footer-p3')
], className='footer')

app.layout = html.Div([
	header,
	html.Div(id='page-content', className='content'),
    footer,
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
    app.run_server(port=2022, dev_tools_ui=False, debug=True)
