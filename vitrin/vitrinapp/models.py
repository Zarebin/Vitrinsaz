from django.db import models



class News(models.Model):
    CATEGORY_CHOICES=(
        ('S', 'Sport'),
        ('C', 'Social'),
        ('B', 'Biology'),
        ('E', 'Economy'),
        ('P', 'Politic'),
    )
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    image_url = models.ImageField(blank=True, null= True, upload_to='images/')
    news_text = models.TextField()

    def __str__(self) -> str:
        return "title:" + f"{self.title}"




class Animation(models.Model):
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

    def __str__(self) -> str:
        return "animation name:" + f"{self.animation_name}"





class Education(models.Model):
    order = models.SmallIntegerField(unique=True)
    title = models.CharField(max_length=20)
    image_url = models.ImageField(blank=True, null=True, upload_to='images/')



    def __str__(self) -> str:
        return f"{self.title}"


