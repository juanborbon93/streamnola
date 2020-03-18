# from db import *
from app import app
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from pages import schedule,event_entry,messages

# from modules.utils import *
# from event import event

jumbo_header = dbc.Jumbotron(
    [
        html.H1('STREAM NOLA'),
        # html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus rutrum mattis mattis.' 
        #         'Vestibulum auctor vulputate ex, in ultricies odio pretium id. Vestibulum sodales, odio at interdum ultrices,' 
        #         'purus ante maximus tellus, vel semper eros felis porta turpis. Suspendisse condimentum dui ligula,' 
        #         'a lobortis diam mattis eu. Donec quis nulla elementum, porta dui at, congue odio. Cras pellentesque consectetur magna, ac pulvinar nisi auctor vel.'
        #         'Vestibulum eget ante id neque tristique elementum. Sed fringilla posuere odio, vel luctus nulla dignissim vel. Pellentesque sit amet porta nibh. '
        #         'Donec facilisis augue a mi pellentesque, at iaculis ex varius. Nam at dignissim neque. Phasellus elementum lacus id magna vulputate, '
        #         'feugiat pulvinar sapien rutrum. Quisque lobortis ultrices sapien, malesuada euismod tortor mollis eget. Vivamus in egestas erat. '
        #         'Maecenas efficitur, mi id pellentesque facilisis, arcu risus sagittis ante, sit amet porttitor urna metus in metus.')
        messages.welcome_message
    ],
)

# schedule = html.Div()
# add_event = html.Div()

content = dcc.Tabs(
    children = [
        dcc.Tab(label='STREAM SCHEDULE', value='schedule',children = html.Div(schedule.schedule()),id='event-schedule'),
        dcc.Tab(label='ADD EVENT',value='add',children=[messages.event_instructions]+[event_entry.event_entry()])
    ],
    value = 'schedule'
)


layout = html.Div(
    [
        dbc.Row(jumbo_header),
        content,
        dcc.Store(id='calendar-data'),
        dcc.Interval(
            id='interval-component',
            interval=60*1000,
            n_intervals=0
        )
    ]
)