from peewee import *
from dotenv import load_dotenv
from os import environ

load_dotenv()

db = MySQLDatabase(
    environ["DATABASE_NAME"],
    user=environ["DATABASE_USER"],
    password=environ["DATABASE_PASSWORD"],
    host=environ["DATABASE_HOST"],
    port=int(environ["DATABASE_PORT"]),
)


# Définir un modèle d'exemple
class Url(Model):
    id = AutoField()
    long_url = TextField()
    short_url = TextField()
    redirection_count = IntegerField(default=0)

    class Meta:
        database = db


db.connect()
db.create_tables([Url])
