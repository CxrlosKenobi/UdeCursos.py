# index page
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from server import app, server
from views import main, horario

# header = html.Div(
#     className='header',
#     children=html.Div(
#         className='container-width',
#         style={'height':'100%'},
#         children=[
#             html.H1(''),
#             html.Div(
#                 className='links',
#                 children=[
#                     html.P('')
#                 ]
#             )
#         ]
#     )
# )
app.layout = html.Div([
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
