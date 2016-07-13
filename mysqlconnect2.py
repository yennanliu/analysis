# ref :  https://gist.github.com/stefanthoss/364b2a99521d5bb76d51

import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://<user>:<password>@<host>[:<port>]/<dbname>')

df = pd.read_sql_query('SELECT * FROM taxi limit 10', engine)
df.head()

