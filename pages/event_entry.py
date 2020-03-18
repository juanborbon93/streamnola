import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from datetime import datetime, timedelta


event_name = dbc.Input(id='artist',placeholder='artists name',type='text',bs_size='lg')

def date_input():
    min_date = datetime.now()-timedelta(days=1)
    max_date = min_date+timedelta(days=90)
    date_input_field = dcc.DatePickerSingle(
        id='date',
        min_date_allowed=min_date,
        max_date_allowed=max_date,
        initial_visible_month=min_date
    )
    return date_input_field

hours = list(range(1,13))
hours = hours[-1:]+hours[:-1]
times_map = {}
for i in ['AM','PM']:
    for j in hours:
        for k in ['00','30']:
            key = f'{j}:{k} {i}'
            if i == 'PM' and j!=12:
                h = j+12
            elif i == 'AM' and j==12:
                h = 0
            else:
                h = j
            value = {
                'hour':h,
                'minute':int(k)
            }
            times_map[key]=value

start_time_select = dbc.Select(
    id='start-time-select',
    options=[
        {'label':time,'value':time}
        for time in times_map.keys()
    ],
    bs_size='lg'
)
event_link = dbc.Input(id='link',placeholder='stream link',type='text',bs_size='lg')

description = dbc.Textarea(id='description',placeholder='description of event',bs_size='lg')

duration = dbc.Input(id='duration',type='number',min=0.25,max=6,step=0.01,bs_size='lg')
def event_entry():
    form = dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label('Artist Name'),
                        event_name
                    ]
                ),
                width=6
            ),
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label('Link to Stream'),
                        event_link,
                    ]
                ),
                width=6
            ),
            dbc.Col(
                description,
                width=12
            ),
            dbc.Col(
                [
                    dbc.Label('Date',style={'display':'block'}),
                    date_input(),
                ],
                width = 'auto'
            ),
            # dbc.Col(
            #     date_input(),
            #     width='auto'
            # ),
            dbc.Col(
                [
                    dbc.Label('Start Time'),
                    start_time_select
                ],
                width='auto'
            ),
            dbc.Col(
                [
                    dbc.Label('Duration in Hours'),
                    duration
                ],
                width='auto'
            ),
            dbc.Col(
                dbc.Button('SUBMIT',id='event-submit',style={'margin-top':'1rem'}),
                width=12
            ),
            html.Div(id='submit-message')
        ],
    )
    form_card = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H3('Event submision form:'),
                    form
                ]
            )
        ]
    )
    return form_card

