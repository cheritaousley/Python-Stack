# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.


def index(request):
    print "MADE IT TO INDEX"
    return render(request, "index.html")

def process(request):
    print "MADE IT TO PROCESS"
    print request.POST
    print request.POST['name']
    print request.POST['location']
    print request.POST['language']
    print request.POST['comment']
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST["location"]
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    # context= {
    #     'name': request.POST['name'],
    #     'location': request.POST['location'],
    #     'language': request.POST['language'],
    #     'comment': request.POST['comment']
    # }
    return redirect ('/survey/results')

def results(request):
    return render(request, "results.html")
