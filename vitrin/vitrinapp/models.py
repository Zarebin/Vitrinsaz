from django.db import models
from decimal import Decimal


class Vitrin(models.Model):

    name = models.CharField(max_length=30)
    background = models.ImageField(blank=True, null= True, upload_to="static/images/")
    vertical_margin = models.PositiveSmallIntegerField(default=100)
    horizontal_margin = models.PositiveSmallIntegerField(default=100)
    style = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "background": self.background.url,
            "vertical_margin": self.vertical_margin,
            "horizontal_margin": self.horizontal_margin,
            "rows": list(map(lambda row: row.serialize(), Row.objects.filter(vitrin_id=self.id)))
        }



class Row(models.Model):
    ARRANGE_CHOICES = (
        ("H", "fixed_height"),
        ("W", "fixed_width"),
    )
    title = models.CharField(max_length=30)
    arrange_type = models.CharField(max_length=1, choices=ARRANGE_CHOICES)
    radius = models.PositiveSmallIntegerField(default=20)
    height = models.PositiveSmallIntegerField(default=100)
    ratio = models.DecimalField(max_digits=2, max_length=2, decimal_places=1, default=Decimal('0.0'))
    vitrin = models.ForeignKey(Vitrin, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"

    def serialize(self) -> dict:
        return {
            "title": self.title,
            "arrange_type": self.arrange_type,
            "radius": self.radius,
            "height": self.height,
            "ratio": f"{self.ratio}",
            "items": list(map(lambda item: item.serialize(), Item.objects.filter(row_id=self.id)))
        }



class Item(models.Model):
    order = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    image_url = models.ImageField(blank=True, null=True, upload_to='static/images/')
    row = models.ForeignKey(Row, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.order}:{self.title}"
    
    def serialize(self):
        return {
            "title" : self.title,
            "order" : self.order,
            "image_url" : self.image_url.url,
        }

