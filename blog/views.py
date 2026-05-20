from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Adventure

def home(request):
    return render(request, 'blog/index.html')

def characters(request):
    return render(request, 'blog/characters.html')

def contact(request):
    if request.method == 'POST':
        return render(request, 'blog/contact.html', {'success': True})
    return render(request, 'blog/contact.html')

def story_list(request):
    adventures = Adventure.objects.all()
    return render(request, 'blog/story.html', {'adventures': adventures})

def story_detail(request, slug):
    adventure = get_object_or_404(Adventure, slug=slug)
    blocks = adventure.blocks.all()
    all_adventures = list(Adventure.objects.all())
    next_adventure = None
    try:
        current_index = all_adventures.index(adventure)
        # Check if there is another adventure lower down the list
        if current_index + 1 < len(all_adventures):
            next_adventure = all_adventures[current_index + 1]
    except ValueError:
        pass

    context = {
        'adventure': adventure,
        'blocks': blocks,
        'next_adventure': next_adventure,
    }
    # FIXED: Added exactly 4 spaces to align perfectly with the rest of the function!
    return render(request, 'blog/story_detail.html', context)
