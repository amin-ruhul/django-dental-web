from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.method == 'POST':

        name = request.POST['your-name']
        email = request.POST['your-email']
        phone = request.POST['your-phone']
        address = request.POST['your-address']
        schedule = request.POST['your-schedule']
        time = request.POST['your-time']
        message = request.POST['your-message']

        return render(request,'dental/appointmen.html',{'name':name})
    else:
        return render(request,'dental/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['message-name']
        email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'Message ' + name,
            'there has been inquiry for '+ message,
            email,
            ['ruhulinfo@gmail.com'],
            fail_silently=False
        )
        return render(request,'dental/contact.html',{'sender_name':name})
    else:
        return render(request,'dental/contact.html')


def about(request):
    return render(request,'dental/about.html')

def blog(request):
    return render(request,'dental/blog.html')

def service(request):
    return render(request,'dental/service.html')

def pricing(request):
    return render(request,'dental/pricing.html')