from django.shortcuts import render, redirect
from pyparsing import html_comment
from .forms import ContactForm
from django.views import View
from .task import mail_sender
from django.http import HttpResponse

class SuccessView(View):
    def get(self, request):
        return render(request, 'mail_sender/success.html')

class ContactView(View):

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "Regarding Implementation of Celery in Django" 
            body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
            
            result = mail_sender.delay(subject,body)

            
            return render(request, 'mail_sender/success.html')


           
            
    def get(self, request):
        form = ContactForm()
        return render(request, "mail_sender/contact.html", {'form':form})
        

