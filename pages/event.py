import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from datetime import datetime


def event_element(name,time,link,description):
    # event_name = 'event name'
    # start_time = 'start time'
    # event_link = 'https://www.google.com'
    # description = 'blah blah blah'
    # stream_link = 'https://www.google.com'
    event = dbc.Card(
        dbc.CardBody(
            [
                html.H3(f'{name}    {time}',className='card-title'),
                html.P(description,className='card-text'),
                dbc.CardLink('Stream',href=link),
                # dbc.CardLink('Add to Calendar')
            ]
        )
    )
    return event

