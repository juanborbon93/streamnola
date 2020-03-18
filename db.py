from modules.database import *
import os

db.bind(provider='postgres', dsn=os.environ['DATABASE_URL'])
db.generate_mapping(create_tables=False)