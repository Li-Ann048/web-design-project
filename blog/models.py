# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
import os
from PIL import Image
from django.utils.text import slugify


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
    

# Helper function to rename image blocks automatically based on story slug and order number
def get_block_image_path(instance, filename):
    ext = filename.split('.')[-1]
    name = os.path.splitext(filename)[0]
    clean_name = slugify(name) 
    return f'adventures/blocks/{clean_name}.{ext}'

class Adventure(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    cover_image = models.ImageField(upload_to='adventures/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    # Automatic resize for main cover image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cover_image:
            img = Image.open(self.cover_image.path)
            max_size = (1200, 1200)
            if img.width > 1200 or img.height > 1200:
                img.thumbnail(max_size)
                img.save(self.cover_image.path)

    class Meta:
        ordering = ['-date']


class AdventureBlock(models.Model):
    BLOCK_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
    ]

    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name='blocks')
    order = models.PositiveIntegerField()
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPES)
    text = models.TextField(blank=True)
    
    # Updated upload_to to call our automated file-renaming function
    image = models.ImageField(upload_to=get_block_image_path, blank=True)

    def __str__(self):
        return f"{self.adventure.title} — block {self.order}"

    # Automated alt text generator using the cleaned up image file name
    @property
    def image_alt_text(self):
        if self.image:
            base_name = os.path.basename(self.image.name)
            filename_without_ext = os.path.splitext(base_name)[0]  # Extracts just the name string
            # Replaces hyphens/underscores with spaces and makes it Title Case
            return filename_without_ext.replace('-', ' ').replace('_', ' ').title()
        return "Adventure Image"

    # Automatic resize for content block images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            max_size = (800, 800)
            if img.width > 800 or img.height > 800:
                img.thumbnail(max_size)
                img.save(self.image.path)

    class Meta:
        ordering = ['order']
