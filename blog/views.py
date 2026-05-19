from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from mysite.secret import RECIPIENT_EMAIL
from .models import Adventure

def home(request):
    return render(request, 'blog/index.html')

def mrbee_story(request):
    return render(request, 'blog/story.html')

def characters(request):
    return render(request, 'blog/characters.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject=f'Message from {name} via Mr. Bee website',
            message=f'From: {name}\nEmail: {email}\n\n{message}',
            from_email=email,
            recipient_list=[RECIPIENT_EMAIL],
        )
        messages.success(request, 'Your message was sent! 🐝')
        return redirect('/contact/')

    return render(request, 'blog/contact.html') 


#for story posts
def story_list(request):
    adventures = Adventure.objects.all()
    return render(request, 'blog/story.html', {'adventures': adventures})

def story_detail(request, slug):
    adventure = get_object_or_404(Adventure, slug=slug)
    blocks = adventure.blocks.all()  # gets all blocks in order
    return render(request, 'blog/story_detail.html', {'adventure': adventure, 'blocks': blocks})