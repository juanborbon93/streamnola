from pony.orm import *
import datetime
from datetime import datetime


db = Database()

class Event(db.Entity):
    index = PrimaryKey(int,auto=True,column='id')
    eventname = Required(str,column='eventname')
    description = Required(str,column='description')
    streamlink = Required(str,column='streamlink')
    starttime = Required(datetime,column='time')
    endtime = Required(datetime,column='endtime')





    
