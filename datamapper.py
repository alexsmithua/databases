from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:') #, echo=True)


metadata = MetaData()

user = Table('user', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('fullname', String(50)),
            Column('password', String(12))
        )
user.create(engine)

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __str__(self):
        return 'User <name=%s; fullname=%s; password=%s>' % (self.name, self.fullname, self.password)


mapper(User, user)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
print(ed_user)

session.add(ed_user)

ed_user.password = 'f8s7ccs'
ed_user.fullname = 'FF'

print('is_modified', session.is_modified(ed_user))

session.commit()

our_user = session.query(User).filter_by(name='ed').first()

print(our_user)