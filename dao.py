import sqlite3


class AuthorDTO(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return 'Author <id: %i, name: %s>' % (self.id, self.name)


class AuthorDAO(object):
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def find(self, id):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM author WHERE id=?', (id,))
            id, name = cur.fetchone()
            return AuthorDTO(id, name)

    def update(self, id, name):
        raise Exception('Implement me')

    def insert(self, name):
        raise Exception('Implement me')

    def delete(self, id):
        raise Exception('Implement me')


if __name__ == '__main__':
    dao = AuthorDAO('myLibrary.db')
    a1 = dao.find(2)
    print (a1)
    # dao.update(2, 'new name')