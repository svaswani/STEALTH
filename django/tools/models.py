from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.core.exceptions import ValidationError

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)

    def __str__(self):
        return str(self.name)

class BaseUser( User ):

    address = models.CharField( max_length = 300 )

    def __str__( self ):
        return self.username
