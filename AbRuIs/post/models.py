from django.db import models

# Create your models here.


class Post(models.Model):
    objects = None
    image = models.ImageField()
    title = models.CharField(max_length=222)
    text = models.CharField(max_length=500)
    # vaqt = models.CharField(max_length=100)
    # matn = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
