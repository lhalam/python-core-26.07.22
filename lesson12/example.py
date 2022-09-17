from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:root@localhost:5432/lesson12', echo=False)
print(engine)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

metadata = MetaData()

authors_table = Table('authors',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))

books_table = Table('books',
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))


metadata.create_all(engine)

# insert_stmt = authors_table.insert(bind=engine)
# print(insert_stmt)
# insert_stmt.execute(name='Alexandre Dumas')
# insert_stmt.execute(name='Lhalam Dumas')
# insert_stmt.execute(name='')
# insert_stmt.execute(name=1111)
# insert_stmt.execute([{'name': 'Mr X'},
#                      {'name': 'Mr Y'}])

metadata.bind = engine
# select_stmt = authors_table.select(authors_table.c.id==2)
# result = select_stmt.execute()
# # result.fetchall()
# print(result.fetchall())
# del_stmt = authors_table.delete(authors_table.c.name=='Mr Y')
# print(del_stmt)
# result = del_stmt.execute()
# del_stmt.execute(whereclause=text("name='Mr EE'"))

# del_stmt = authors_table.delete()
# del_stmt.execute()# delete allSQLAlchemy VI

from sqlalchemy.orm import mapper, relation
from sqlalchemy.orm import relationship, backref


class Author(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(object):
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title


mapper(Book, books_table)
mapper(Author,
       authors_table,
       properties={
           'books': relation(Book, backref='author')})


select_stmt = authors_table.select(authors_table.c.id==127)
result = select_stmt.execute()
# result.fetchall()
print(result.fetchall())
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

a = session.query(Author).all()
print(a)