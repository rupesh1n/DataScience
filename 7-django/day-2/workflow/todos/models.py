from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.name}"

class PriorityChoices(models.IntegerChoices):
    LOW =1, 'Low'
    MEDIUM=2,'Medium'
    HIGH=3,'High'

class ToDo(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    done=models.BooleanField(default=False)
    deadline=models.DateField(null=True,blank=True)
    priority=models.IntegerField(choices=PriorityChoices.choices,null=True,blank=True)

    owner=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='todos',null=True,blank=True)

def __self__(self):
    return f"{self.id} - {self.title}"