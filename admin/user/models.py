# models_mysql.py

from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store encrypted password
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # Add this property to return the user's identifier
    @property
    def id(self):
        return self.user_id

    def __str__(self):
        return self.user_name

