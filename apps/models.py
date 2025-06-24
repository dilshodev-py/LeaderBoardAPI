from django.db.models import Model, CharField, SmallIntegerField



class Student(Model):
    name = CharField(max_length=50)
    rank = SmallIntegerField(default=0)

