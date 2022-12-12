from django.db import models



class Vitrin(models.Model):

    name = models.CharField(max_length=30)
    theme = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"




class Row(models.Model):

    title = models.CharField(max_length=30)
    arrange_type = models.CharField(max_length=20)
    vitrin = models.ForeignKey(Vitrin, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"




class Item(models.Model):
    order = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    image_url = models.ImageField(blank=True, null=True, upload_to='images/')
    row = models.ForeignKey(Row, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.order}:{self.title}"

