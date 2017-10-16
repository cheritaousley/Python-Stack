# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from time import strftime
# Create your views here.


def index(request):
    print "MADE IT TO INDEX"
    context = {
      "time": strftime("%Y-%m-%d %H:%M:%S")
    }
    print strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "index.html", context)
