from peewee import (
    SqliteDatabase , 
    CharField , 
    ForeignKeyField,
    Model,
    TextField
)

db = SqliteDatabase("mydb.db")

class User(Model):
    username = CharField()
    email = CharField()
    password = CharField()
    admin = TextField(null=True)
    

    class Meta:
        database = db

class File(Model):
    user = TextField(ForeignKeyField(User))
    path = CharField()

    class Meta:
        database = db

User.create_table()
File.create_table()

