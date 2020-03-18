import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from waitress import serve
from pony import orm
from app import app,server
from db import *
from pages import main_page
from callbacks import *

app.title='stream nola'


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='main-page',style={'margin-bottom':'2em'})
])

@app.callback(
    Output('main-page','children'),
    [Input('url','pathname')]
)
def show_page(pathname):
    if pathname ==None:
        return None
    if pathname == '/':
        return main_page.layout
    print(pathname)
    pathname = pathname.split('/')
    return html.H1('404')


if __name__ == '__main__':
    # app.server.run(host='0.0.0.0', port=5000,debug=True) 
    # app.run_server(host='0.0.0.0', port=5000)
    app.run_server()
    # serve(server,host='0.0.0.0', port=5000)
