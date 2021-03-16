# index page
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from server import app, server
from views import main, horario, malla

header = html.Div(
    [
        html.Div(
            style={'height':'100%'},
            children=[
                html.Img(
                src='assets/udeconline.png',
                className='banner-img'
                ),
				html.H1(
					'Ingeniería Civil Informática',
                    className='banner-h1'
				),
				html.P(
					'UdeC - 2021',
                    className='banner-p'
                ),
                html.Div(
                    className='links',
                    children=[
                        html.P('')
                ]
            )
        ]
    )
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
