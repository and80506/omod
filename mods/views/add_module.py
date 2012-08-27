#coding: utf-8

from django.shortcuts import HttpResponse


def addModule(request):
    if request.method == "GET":
        return HttpResponse('{}')
        