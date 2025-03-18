from django.db import models

from django.contrib.auth.models import User

from django.utils.timezone import now

# Create your models here.


class TaskModel(models.Model):

    task_name = models.CharField(max_length=100)

    task_description = models.TextField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)

    due_date = models.DateTimeField()

    priority_level = [
        ("low","low"),
        ("medium","medium"),
        ("high","high")
    ]

    priority = models.CharField(max_length=10,choices=priority_level)

    point = models.IntegerField(default=0)

    status =models.BooleanField(default=False)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
    
    def complete(self):

        if self.status == False:

            if now() < self.due_date:

                self.point +=10

            self.status = True

            self.save()