# SqlAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine("mysql+pymysql://<youruser>:<yourpassword>@localhost/expensetracker")
Session = sessionmaker(bind=engine)


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
