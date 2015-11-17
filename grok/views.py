from django.http import HttpResponse
from django.shortcuts import redirect, render
from grok.models import LinkItem


def home_page(request):
    links = LinkItem.objects.all()
    return render(request, 'home.html', {'links': links})


def new_link(request):
    link_text = request.POST.get('new_link')
    LinkItem.objects.create(url=link_text)
    return redirect('/')
