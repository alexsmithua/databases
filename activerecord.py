import sqlite3
from init import init_db


class Author(object):

    db_name = None

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return 'Author <id: %i, name: %s>' % (self.id, self.name)

    @classmethod
    def get(cls, id):
        with sqlite3.connect(cls.db_name) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM author WHERE id=?', (id,))
            id, name = cur.fetchone()
            return Author(id, name)

    @classmethod
    def find(cls, name):
        raise Exception('Implement me')

    def update(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('UPDATE author SET name=? WHERE id=?', (self.name, self.id))

    def save(self):
        raise Exception('Implement me')

    def delete(self):
        # and delete all books
        raise Exception('Implement me')

    def get_books(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT book.id, book.title FROM book
                LEFT JOIN author_book
                ON book.id == author_book.book_id
                WHERE author_book.author_id=?''', (self.id,))
            return cur.fetchall()


if __name__ == '__main__':
    db_name = "myLibrary.db"
    init_db(db_name)

    Author.db_name = db_name

    a = Author.get(id=1)
    print(a)

    a.name = 'David Copperfield'
    a.update()
    print(a)

    books = a.get_books()
    print(books)