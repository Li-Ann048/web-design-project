# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#adventures posts modelss
class Adventure(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    cover_image = models.ImageField(upload_to='adventures/')
    slug = models.SlugField(unique=True)  # e.g. "picnic-in-paris" for the URL

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']  # newest first


class AdventureBlock(models.Model):
    BLOCK_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
    ]

    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name='blocks')
    order = models.PositiveIntegerField()
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPES)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='adventures/blocks/', blank=True)

    def __str__(self):
        return f"{self.adventure.title} — block {self.order}"

    class Meta:
        ordering = ['order']  # always in sequence