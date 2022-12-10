from django.db import models



class News(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.ImageField(blank=True, null= True, upload_to='images/')
    news_text = models.TextField()


class Animations(models.Model):
    GENRE_CHOICES = (
        ('A', 'Anime'),
        ('D', 'Adult'),
        ('C', 'Children'),
        ('M', 'Musical'),
    )
    animation_name = models.CharField(max_length=30)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    summary = models.TextField()
    image_url = models.ImageField(blank=True, null=True, upload_to='images/')


class Educations(models.Model):
    order = models.AutoField(unique=True)
    title = models.CharField(max_length=20)
    image_url = models.ImageField(blank=True, null=True, upload_to='images/')


