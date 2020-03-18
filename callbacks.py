from db import *
import datetime
from datetime import datetime,timedelta
from dash.dependencies import Input, Output, State
from app import app,server
import requests
from pages.event_entry import times_map
from pages import schedule

def link_valid(link):
    try:
        request = requests.get(link)
    except:
        return False
    return request.status_code == 200 

def time_parser(date,time,duration):
    '''
    returns a start and end datetime objects
    '''
    year,month,day = [int(i) for i in date.split('-')]
    hour = times_map[time]['hour']
    minute = times_map[time]['minute']
    start_time = datetime(year=year,month=month,day=day,hour=hour,minute=minute)
    end_time = start_time+timedelta(hours=duration)
    return start_time,end_time


@app.callback(
    [Output('submit-message','children')],
    [Input('event-submit','n_clicks')],
    [
        State('artist','value'),
        State('link','value'),
        State('description','value'),
        State('date','date'),
        State('start-time-select','value'),
        State('duration','value')
    ]
)
@db_session
def store_event(n_clicks,artist,link,description,date,time,duration):
    print(n_clicks)
    if n_clicks is not None:
        print(artist,link,description,date,time,duration)
        #check inputs:
        if artist is None or artist=='':
            return(['Artist name field can not be empty'])
        if not link_valid(link):
            return(['Provided event link is not valid'])
        if description is None or description=='':
            return(['Description cannot be blank'])
        if time is None:
            return(['Select start time from the dropdown menu'])
        if date is None:
            return(['select a valid date'])
        if duration is None or duration==0:
            return(['enter valid event duration'])
        start_time,end_time = time_parser(date,time,duration)
        new_event = Event(
            eventname=artist,
            streamlink=link,
            description=description,
            starttime = start_time,
            endtime = end_time
        )
        db.commit()
        return(['Event submitted!'])

@app.callback(Output('event-schedule', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_schedule(n):
    return schedule.schedule()