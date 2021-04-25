from sqlalchemy import Table
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import engine

db = SQLAlchemy()

class Data(db.Model):
    code = db.Column(db.String(40), primary_key=True, unique=True)
    name = db.Column(db.String(40))
    credits = db.Column(db.Integer)
    teacher = db.Column(db.String(40))
    schedule = db.Column(db.String(40))
    days = db.Column(db.String(10))


Data_tbl = Table('data', Data.metadata)


def create_data_table():
    Data.metadata.create_all(engine)

def add_data(code, name, credits, teacher, schedule, days):
    ins = Data_tbl.insert().values(
        code=code,
        name=name,
        credits=credits,
        teacher=teacher,
        schedule=schedule,
        days=days)
    conn = engine.connect()
    conn.execute(ins)
    conn.close()

def del_data(code):
    delete = Data_tbl.delete().where(Data_tbl.c.code == code)
    conn = engine.connect()
    conn.execute(delete)
    conn.close()


def show_data():
    select_st = select([Data_tbl.c.code, Data_tbl.c.name, Data_tbl.c.schedule, Data_tbl.c.days])

    conn = engine.connect()
    rs = conn.execute(select_st)

    for row in rs:
        print(row)

    conn.close()
