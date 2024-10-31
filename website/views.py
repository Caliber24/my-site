from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm, NewsletterForm
from blog.models import Post
from django.contrib import messages


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
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request,messages.SUCCESS,'your ticket submited successfuly')
    else:
      messages.add_message(request,messages.ERROR,'your ticket didnt submited ')
  
  form = ContactForm()
  
  return render(request, 'website/contact.html',{'form': form})


def test_view(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request,messages.SUCCESS,'your ticket submited successfuly')
      return HttpResponse('Success')
    else:
      messages.add_message(request,messages.ERROR,'your ticket didnt submited ')
      return HttpResponse('not valid')
  form = ContactForm()
  
  return render(request, "blog/test.html", {'form': form})

def newsletter_view(request):
  if request.method == 'POST':
    form = NewsletterForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    return HttpResponseRedirect('/')