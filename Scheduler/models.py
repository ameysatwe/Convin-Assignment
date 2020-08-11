from django.db import models
from django.core.exceptions import ValidationError 

# Create your models here.
def validateTask(value):
    if value>4:
        raise ValidationError("This Field only accepts tpe <4")
    return value 
class Task(models.Model):
    ##fields will go here
    task_type=models.IntegerField(validators=[validateTask],unique=True)
    task_desc=models.CharField(max_length=100)
    def __str__(self):
        return f"Task type is {self.task_type}"



class TaskTracker(models.Model):
    Update_Types=[
        ('da','per-day'),
        ('we','Weekly'),
        ('mo','Monthly')
    ]
    task_type=models.ForeignKey(Task,to_field='task_type',on_delete=models.CASCADE)
    update_type=models.CharField(max_length=10,choices=Update_Types,default='da')
    email=models.EmailField()
    def __str__(self):
        return f"email is {self.email}"