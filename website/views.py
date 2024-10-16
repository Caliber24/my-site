from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from blog.models import Post


# def http_test(request):
#   return HttpResponse('<h1>http-test</h1>')

# def json_test(request):
#   return JsonResponse({
#     'name': 'Amir',
    
#   })

def index_view(request):
  return render(request, 'website/index.html')

def about_view(request):
  return render(request, 'website/about.html',{})
def contact_view(request):
  return render(request, 'website/contact.html',{})

