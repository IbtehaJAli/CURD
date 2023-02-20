from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=25)
    rollNumber=models.IntegerField(null=False)
    mail=models.EmailField(null=False)
    def __str__(self):
        return f"Name: {self.name}  "