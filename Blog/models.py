from django.db import models

# Create your models here.
class visitor(models.Model):
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    def __str__(self):
        return self.first_name

class contact(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    subject=models.CharField(max_length=256)
    message=models.TextField(max_length=256)
    class Meta():
        ordering=('name',)
        verbose_name_plural='Contacts'
    def __str__(self):
        return self.email

class Blogs(models.Model):
    title=models.CharField(max_length=256)
    body=models.TextField()
    pub_date=models.DateTimeField()

    class Meta():
        ordering=('title',)
        verbose_name_plural='Blogs'

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
