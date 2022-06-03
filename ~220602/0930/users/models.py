from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user_name = models.OneToOneField(User, related_name='user_name', on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='user_img', blank=True)
    nickname = models.CharField(max_length=20, blank=True)
    intro = models.TextField(blank=True)