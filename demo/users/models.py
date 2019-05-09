from django.db import models
from django.contrib.auth.models import AbstractUser

# http://docs.wagtail.io/en/v2.1.1/advanced_topics/customisation/custom_user_models.html

class User(AbstractUser):
    country = models.CharField(verbose_name='country', max_length=255)

# Create your models here.
