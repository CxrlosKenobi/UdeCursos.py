# Dash app initialization
import dash
import dash_html_components
import dash_bootstrap_components as dbc
# User management initialization
# from config import config
import os

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FA],
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
        }
    ],
    # external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server
app.title = 'UdeCursos.py'
# app.title = 'Malla INF'
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# config
# server.config.update(
#     SECRET_KEY=os.urandom(12),
#     SQLALCHEMY_DATABASE_URI=config.get('database', 'con'),
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )
