from sqlalchemy.orm import declarative_base,sessionmaker

from sqlalchemy import create_engine



DBNAME="mini_project"

engine=create_engine("postgresql://postgres:123456789@localhost/mini_project")
class SessionClass(object):
    def __init__(self):
        Session=sessionmaker(bind=engine)
        self.instance=Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SessionClass, cls).__new__(cls)
        return cls.instance
    
    def get_session(self):
        return self.instance

Base=declarative_base()



