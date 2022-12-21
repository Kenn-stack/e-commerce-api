# from django.db import models
from djongo import models
from django.conf import settings


class Profile(models.Model):
    _id = models.ObjectIdField()
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name= 'profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    objects = models.DjongoManager()


    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in-between
        """
        full_name = '%s %s' %(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the first_name of the user
        """
        return self.first_name


