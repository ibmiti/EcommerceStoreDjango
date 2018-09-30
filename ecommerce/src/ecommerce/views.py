from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    html ="""
    <!DOCTYPE html>
    return HttpResponse("<h1>Hello World</h1>")
