# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.


def index(request):
    print "MADE IT TO INDEX"
    if request.session.has_key('count') == False:
        request.session['count'] = 1
    # else:
    #     request.session['count'] += 0

    context = {
        "random_string": get_random_string(length=14),
        "count": request.session['count']
    }
    print get_random_string(length=14)
    return render(request, "index.html", context)


def increment(request):
   print "MADE IT TO INCREMENT"
   request.session['count'] += 1
   return redirect('/randomnumgen')

def clear(request):
   print "MADE IT TO CLEAR"
   for key in request.session.keys():
       del request.session['count'] 
   return redirect('/')
