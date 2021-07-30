from django.shortcuts import render
from django.http import HttpResponse

# returning html templates on user request
def say_hello(request):
    return render(request, 'hello.html')
