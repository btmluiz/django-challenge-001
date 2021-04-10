import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Author(User):
    picture = models.URLField()

    class Meta:
        verbose_name = "Author"


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    firstParagraph = models.TextField()
    body = models.TextField()
