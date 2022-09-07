from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

engine = create_engine('mysql+pymysql://root@localhost/test')
meta = MetaData()
conn = engine.connect()
