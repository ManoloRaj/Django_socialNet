from django.db import models

# Create your models here.
class user(models.Model):
    photo =         models.ImageField(upload_to = 'images/')

    first_name =    models.CharField(max_length = 100)
    family_name =   models.CharField(max_length = 100)
    user_name =     models.CharField(max_length = 100)

    password =      models.CharField(max_length = 100)
    date_of_birth = models.DateField()

    description =   models.TextField()

