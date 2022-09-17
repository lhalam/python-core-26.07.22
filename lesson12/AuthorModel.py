from sqlalchemy.orm import mapper
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
