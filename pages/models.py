from django.db import models
# Create your models here.
class Team(models.Model):
    first_name= models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    profile = models.ImageField(upload_to='photo/%y/%m/%d')
    job=models.CharField(max_length=220)
    face_link=models.URLField(max_length=220)
    twitter_link=models.URLField(max_length=220)
    google_link=models.URLField(max_length=220)
    created_date= models.DateTimeField(auto_now_add='true')
    def __str__(self):
        return self.first_name
    
