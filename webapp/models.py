from peewee import (
    SqliteDatabase , 
    TextField , 
    ForeignKeyField,
    Model
)

db = SqliteDatabase("mydb.db")

class User(Model):
    username = TextField()
    email = TextField()
    password = TextField()
    admin = TextField(default=None , null=True)

    class Meta:
        database = db

class File(Model):
    user = TextField(ForeignKeyField(User))
    path = TextField()

    class Meta:
        database = db

User.create_table()
File.create_table()

