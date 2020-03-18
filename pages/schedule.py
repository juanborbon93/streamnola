import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
# from pages.event_elem import *
from db import *
from datetime import datetime,timedelta

# schedule = html.Div(
#     [event(1) for i in range(5)]
# )
def make_event_element(name,time,link,description):
    # event_name = 'event name'
    # start_time = 'start time'
    # event_link = 'https://www.google.com'
    # description = 'blah blah blah'
    # stream_link = 'https://www.google.com'
    event = dbc.Card(
        dbc.CardBody(
            [
                html.H3(name,className='card-title'),
                html.H4(time),
                html.P(description,className='card-text'),
                dbc.CardLink('Stream',href=link),
                # dbc.CardLink('Add to Calendar')
            ]
        )
    )
    return event

@db_session
def schedule():
    events = select(i for i in Event if i.starttime>datetime.now()-timedelta(hours=2))
    event_schedule = []
    for event in events:
        start_time_string = event.starttime.strftime("%m/%d/%Y, %I:%M:%p")
        end_time_string = event.endtime.strftime("%I:%M:%p")
        event_time = f'{start_time_string} - {end_time_string}'
        event_element = make_event_element(event.eventname,event_time,event.streamlink,event.description)
        event_schedule.append((event_element,event.starttime))
    event_schedule.sort(key=lambda x:x[1])
    event_schedule = [i[0] for i in event_schedule]
    return event_schedule
    
