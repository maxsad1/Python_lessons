from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    resp = HttpResponse('<!DOCTYPE html><html><body><h1>Hello from {}!</h1></body></html>'.format('Django'))
    return resp
