from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email=models.EmailField()
    Message=models.TextField()

    def __str__(self):
        return self.fname+" "+self.lname

class Sign_up(models.Model):
    upemail = models.EmailField()
    sname = models.CharField(max_length=30)
    password = models.TextField()

    def __str__(self):
        return self.sname
