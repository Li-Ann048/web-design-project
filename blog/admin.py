# Register your models here.

from django.contrib import admin
from .models import Post, Adventure, AdventureBlock

admin.site.register(Post)

class AdventureBlockInline(admin.StackedInline):
    model = AdventureBlock
    extra = 3  # shows 3 empty block forms by default
    fields = ['order', 'block_type', 'text', 'image']

@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    inlines = [AdventureBlockInline]
    list_display = ['title', 'location', 'date']
    prepopulated_fields = {'slug': ('title',)}  # auto-fills slug from title