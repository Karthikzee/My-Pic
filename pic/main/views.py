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
    contents = ["firstname", "lastname", "gender", "courses", "points", "phone", "email"]
    text = "Registration for\n"
    for i in contents:
        text += i +": "+ str(request.POST[i])
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    sender = 'karthikzee0@gmail.com' #add sender email id here inside quotes
    reciever = 'karthik.18bcs@cmr.edu.in' #add reciever email id here inside quotes
    message = text
    password = "" #add sender password inside quotes, this is not at all recommended. But thing works so why fix it :)
    s.login(sender, password)
    s.sendmail(sender, reciever, message)
    return render(request=request,
				  template_name="main/thanks.html"
				 )
