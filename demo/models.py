from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    company=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    msg=models.TextField()

    def __str__(self):
        return self.name

class Remark(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self):
        return self.name