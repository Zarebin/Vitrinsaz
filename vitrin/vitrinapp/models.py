from django.db import models



class Vitrin(models.Model):

    name = models.CharField(max_length=30)
    theme = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "theme": self.theme,
            "rows": list(map(lambda row: row.serialize(), Row.objects.filter(vitrin_id=self.id)))
        }



class Row(models.Model):

    title = models.CharField(max_length=30)
    arrange_type = models.CharField(max_length=20)
    vitrin = models.ForeignKey(Vitrin, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"

    def serialize(self) -> dict:
        return {
            "title": self.title,
            "arrange_type": self.arrange_type,
            "items": list(map(lambda item: item.serialize(), Item.objects.filter(row_id=self.id)))
        }



class Item(models.Model):
    order = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    image_url = models.ImageField(blank=True, null=True, upload_to='images/')
    row = models.ForeignKey(Row, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.order}:{self.title}"
    
    def serialize(self):
        return {
            "title" : self.title,
            "order" : self.order,
            # "image_url" : self.image_url,
        }

