# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    print "MADE IT TO INDEX"
    return render(request, "index.html")


def new(request):
    print "MADE IT TO INDEX"
    return render(request, "new.html")


def create(request):
    print "MADE IT TO INDEX"
    return redirect('/blogs/')


def number(request,digit):
    context={
        'number':digit
    }
    print "MADE IT TO INDEX"
    return render(request, "number.html", context)


def edit(request, digit):
    context = {
         'number': digit
    }
    print "MADE IT TO INDEX"
    return render(request, "edit.html", context)


def destroy(request, digit):
    print "MADE IT TO INDEX"
    return redirect('/blogs/')
