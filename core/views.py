from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto

def index(request):
    print(dir(request))
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é top!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #pro = Produto.objects.get(id=pk)
    pro = get_object_or_404(Produto, id=pk)

    context = {
        'produto': pro
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)

