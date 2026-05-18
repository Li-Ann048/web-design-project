from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'blog/index.html')

def mrbee_story(request):
    return render(request, 'blog/mrbee_story.html')

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
            recipient_list=['YOUR_EMAIL@gmail.com'],
        )
        messages.success(request, 'Your message was sent! 🐝')
        return redirect('/contact/')

    return render(request, 'blog/contact.html') 