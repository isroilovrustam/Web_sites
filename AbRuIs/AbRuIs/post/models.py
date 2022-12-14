# from django.contrib.auth import get_user_model
from django.db import models
# from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=222)
    summary = models.CharField(max_length=200)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    massage = RichTextField()
    # author = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE
    # )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]

    # def get_absolute_url(self):
    #     return reverse('detail')
