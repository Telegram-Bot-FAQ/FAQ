from peewee import *

db = SqliteDatabase('users.db')


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = IntegerField(unique=True)
    ref = IntegerField(default=0)

    @classmethod
    def get_user(cls, user_id):
        return cls.get(user_id = user_id)

    @classmethod
    def get_ref_count(cls, user_id):
        return cls.get_user(user_id).ref

    @classmethod
    def increase_ref_count(cls, user_id):
        user = cls.get_user(user_id)
        user.ref += 1
        user.save()

    @classmethod
    def user_exists(cls, user_id):
        query = cls().select().where(cls.user_id == user_id)
        return query.exists()

    @classmethod
    def create_user(cls, user_id):
        user, created = cls.get_or_create(user_id=user_id)

# создаём таблицы, запустить 1 раз и закомментировать
# db.create_tables([Users])
