from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SubscribeForm


# Create your views here.
def EmailSend(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Clower World'
            message = 'Thankyou for your Support,Have a Nice Day!'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('emailsend')
    return render(request, 'mailsend.html', {'form': form})
    # return render(request,'mail_send.html')