from django.shortcuts import render
from django.http import HttpResponseRedirect
import smtplib

# Create your views here.
def homepage(request):
	return render(request=request,
				  template_name="main/Home.html"
				 )

def workshop(request):
	return render(request=request,
				  template_name="main/Workshop.html"
				 )

def portfolio(request):
	return render(request=request,
				  template_name="main/Portfolio.html"
				 )

def registration(request):
	return render(request=request,
				  template_name="main/Registration.html"
				 )

def contact(request):
	return render(request=request,
				  template_name="main/Contact.html"
				 )


def submit(request):
    firstname=request.POST['firstname']
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    sender = 'karthikzee0@gmail.com'
    reciever = 'karthik.18bcs@cmr.edu.in'
    message = firstname
    password = ""
    s.login(sender, password)
    s.sendmail(sender, reciever, message)
    return HttpResponseRedirect('/')