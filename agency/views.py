from django.shortcuts import render_to_response,Http404,redirect
from work.models import contact,CampusAmb,Registration
from django.http import HttpResponseRedirect
from django.contrib import messages
from work.form import *
import os
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.static import serve
from django.core.mail import send_mail

def index(request):
    templates = 'work/index.html'
    context = {}
    return render_to_response(templates,context)

def caform(request):
    templates = 'work/caform.html'
    context = {}
    return  render_to_response(templates,context)

def eventregistration(request):
    templates = 'work/eventregistration.html'
    context = {}
    return render_to_response(templates,context)

@csrf_exempt
def capost(request):
    try:
        if request.method == "POST":
            post = request.POST
            email = post.get('email')
            number = post.get('phone')
            name = post.get('name')
            year = post.get('year')
            branch = post.get('branch')
            wat = post.get('wat')
            college = post.get('college')
            CampusAmb.objects.create(name=name,email=email,number=number,year=year,branch=branch,wat=wat,college=college)
            subject = 'Campus Ambassdor Registration'
            body = 'Congratulations '+name+''',

    We are ecstatic that you have shown interest in the annual festival of India's oldest and the most acclaimed Mining Engineering department,i.e.Minovation2018. You are selected as the Campus Ambassador of MINOVATION 2018 from your institute.

    This email is just a symbol of our gratitude towards your valuable effort of registering for Campus Ambassador on the website of MINOVATION 2018.

    The holy city of Kashi awaits you and so do we all Minovators at IIT(BHU), Varanasi.

    Just a reminder about the date-28-30 September 2018.

    Come be a part of us. Become a Minovator!!

    Regards

    Team

    MINOVATION 2018

    IIT(BHU), Varanasi.'''
            mail_sending(request,subject,body,email)
            context = {'messages':'Congratulation!, You have sucessfully registered'}
            return render_to_response('work/index.html',context)
    except:
        Http404('<h4>"Check the fields again"</h4>')
        return render_to_response('work/caform.html', {})
    else:
        return render_to_response('work/caform.html', {})

def mail_sending(request,subject,body,email):
    send_mail(subject, body, 'as57807@gmail.com', [email],fail_silently=False,)
    return True

@csrf_exempt
def eventpost(request):
    try:
        if request.method == "POST":
            post = request.POST
            email = post.get('email')
            number = post.get('phone')
            name = post.get('name')
            year = post.get('year')
            branch = post.get('branch')
            wat = post.get('wat')
            college = post.get('college')
            event = post.get('selector2')
            Registration.objects.create(name=name,email=email,number=number,year=year,branch=branch,wat=wat,college=college,event=event)
            subject = 'Event Registration'
            body ='Congrats '+name+''',
            We are ecstatic that you have shown interest in the annual festival of India's oldest and the most acclaimed Mining Engineering department,i.e.Minovation2018.Now you are officially registered for MINOVATION 2018.
            This email is just a symbol of our gratitude towards your valuable effort of registering for MINOVATION 2018.'''
            mail_sending(request, subject, body, email)
            context = {'messages':'Congratulation!, You have sucessfully registered'}
            return render_to_response('work/index.html',context)
    except:
        Http404('<h4>"Check the fields again"</h4>')
        return render_to_response('work/eventregistration.html',{})

    else:
        return render_to_response('work/eventregistration.html',{})

@csrf_exempt
def contacts(request):
    if request.method == "POST":
        post = request.POST
        email = post.get('email')
        number = post.get('number')
        name = post.get('name')
        message = post.get('msg')
        contact.objects.create(name=name,email=email,number=number,message=message)
        mail_sending(request)
        messages.success(request, "Message recorded!, we'll contact you soon", fail_silently=True)
        response_data = {}
    else:
        return Http404('not allowed')

def infobro(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(BASE_DIR, 'PDFs/brochure.pdf')
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
