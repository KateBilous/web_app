from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
# def homePageView(request):
#     return HttpResponse("Hello World!")


def main(request):
    return render(request, 'pages/base.html')


def home(request):
    return render(request, 'pages/home.html')

def features(request):
    return render(request,'pages/features.html')