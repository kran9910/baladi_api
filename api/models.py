from django.db import models

class Citizen(models.Model):
    citizen_id = models.CharField(max_length= 15)
    phone_number = models.CharField(max_length= 15)
    first_name = models.CharField(max_length= 511)
    last_name = models.CharField(max_length= 511)
    email = models.CharField(max_length= 511)
    address = models.CharField(max_length= 16000)
    birthdate = models.DateField()
    authenticated = models.BooleanField(default= False)
    profile_pic = models.URLField(max_length= 16000, blank= True)

    def __str__(self):
        return self.first_name


