from django.http import HttpResponse
from django.shortcuts import render
# import random
#
# # Create your views here.
# def hello_world(request):
#     return HttpResponse(f"Hello World!{random.randint(1, 100)}")
#
#
# def main_view(request):
#     return render(request, 'posts/main.html')


def text_response(request):
    return HttpResponse("Текстовое сообщение от приложения.")


def html_response(request):
    return render(request, 'template.html')