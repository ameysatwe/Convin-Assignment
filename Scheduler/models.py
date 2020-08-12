from django.db import models
from django.core.exceptions import ValidationError 

# Create your models here.
def validateTask(value):
    if (value>4 or value<0):
        raise ValidationError("This Field only accepts type less than 4 and greater than 0")
    return value 
class Task(models.Model):
    ##fields will go here
    task_type=models.IntegerField(help_text="Enter Task Type",blank=False,validators=[validateTask])
    task_desc=models.CharField(max_length=100,help_text="Enter Task Description",blank=False)
    
    
    def __str__(self):
        return f"Task type is {self.task_type}"



class TaskTracker(models.Model):
    Update_Types=[
        ('daily','per-day'),
        ('weekly','Weekly'),
        ('monthly','Monthly')
    ]
    task_type=models.ForeignKey(Task,on_delete=models.CASCADE)
    update_type=models.CharField(max_length=10,choices=Update_Types,default='daily')
    email=models.EmailField(help_text="Enter Email for updates",blank=False,unique=True)
 
    def __str__(self):
        return f"Task type is {self.task_type}"