from django.shortcuts import render
from app_cad_usuarios.models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
def home(request):
    produtos = Produto.objects.all()
    
    
    context = {
        'curso': 'programação web com Django Framework',
        'outro': 'Teste Django.',
        'produtos': produtos
    }
    return render(request, 'home.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404 )

def error500(request, *args, **argv):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), status=500)
    
