from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

# class Profile(models.Model):
#     profile_photo = models.ImageField(upload_to='profile_pictures/')
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=200, blank=True)
#     email = models.CharField(max_length=100, null=True, blank=True)
#     status = models.CharField(max_length=100, blank=True)
#     following = models.ManyToManyField(User, related_name="follows", blank=True)
#     followers = models.ManyToManyField(User, related_name="followed_by", blank=True)





class Categories(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

class Project(models.Model):
    title = models.CharField(max_length=100, blank=True)
    title_image = models.ImageField(upload_to='title_images/')
    description = models.TextField(max_length=200, blank=True)
    github_link = models.CharField(max_length=300, blank=True)
    live_link = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, related_name="belongs_to", null=True, blank=True)




class Profile(models.Model):

    profile_photo = models.ImageField(upload_to='profile_pictures/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_for", blank=True, null=True)





class Rating(models.Model):
    design = models.IntegerField(null=True, blank=True)
    usablity = models.IntegerField(null=True, blank=True)
    content = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="rating_for", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_by", blank=True, null=True)
