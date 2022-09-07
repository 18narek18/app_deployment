from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db_connection import meta

users = Table("users", meta, 
    Column("id", Integer, primery_key = True),
    Column("name", String),
    Column("email", String),
    Column("age", Integer)
    )