from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Date, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# connect to db
engine = create_engine('mssql+pymssql://sa:123@localhost/lesson13', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# describe class
class Tasks(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    expiration_date = Column(Dat)
    done = Column(Boolean)

    def __init__(self, name, description, expiration_date, done):
        self.name = name
        self.description = description
        self.expiration_date = expiration_date
        self.done = done

    def __repr__(self):
        return self.name

# create table
# Base.metadata.create_all(engine)

# add data into table
session.add(Tasks('learn poem', 'learn poem for the event', '2022/09/26', False))
session.commit()

query = session.query(Tasks)
print(query.all())