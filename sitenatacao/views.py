from django.shortcuts import render, redirect
from . import views
from .models import Inicio, Inscrito, Foto
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, View


# Create your views here.

class HomePage(ListView):
    model = Inicio
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'homepage' 
        return context



    

class PortFolio(ListView):
    model = Foto
    template_name = 'portfolio.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'portfolio'
        return context




def inscricao(request):
    dados = request.GET.dict()
    verificar_aluno = dados.get('auth')
    active_page = 'inscricao'
    return render(request, 'inscricao.html', {'active_page': active_page, 'verificar_aluno': verificar_aluno})


class Inscricao(TemplateView):
    template_name = 'inscricao.html'

    @staticmethod
    def get_age():
        return ['20-30', '30-40', '40-50', '60-70']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = self.request.GET.dict()
        context['active_page'] = 'inscricao'
        context['modalidades'] = self.get_modalidades()
        context['idades'] = self.get_age()
        return context

    def post(self, request):
        self.nome = request.POST.get('firstname')
        self.sobrenome = request.POST.get('lastname')
        self.idade = request.POST.get('idade')
        return self.verificar_nome()
    

    def get_modalidades(self):
        MODALIDADES = ['Livre 100m - Borboleta 100m', 'Borboleta 100m - Peito 50m', 'Peito 200m - Medley 100m']
        return MODALIDADES

            

    def metros(self):
        return ['25', '50', '200', '400']
    
    def verificar_nome(self):   
        self.verificar_candidato = Inscrito.objects.filter(nome = self.nome).filter(sobrenome = self.sobrenome)
        if self.verificar_candidato.exists():
            self.verificar_candidato.delete()
            self.cadastrar_candidato()
            return redirect(reverse('site-natacao:inscricao') + '?status=0')
        else:
            return self.verificar_formulario()

        

        
    def remover_candidato(self):
        self.verificar_candidato.delete()
        
    def verificar_formulario(self):
        if len(self.nome.strip())  == 0 or len(self.sobrenome.strip()) == 0:
            return redirect(reverse('site-natacao:inscricao') + '?status=2')
        else:
            self.cadastrar_candidato()
            return redirect(reverse('site-natacao:inscricao') + '?status=1')
        
    def cadastrar_candidato(self):
        cadastro = Inscrito(nome = self.nome, sobrenome = self.sobrenome, idade = self.idade)
        cadastro.save()




def fotos(request, id):
    active_page = 'portfolio'
    foto = Foto.objects.get(id=id)
    return render(request, 'fotos.html', {'foto': foto, 'active_page': active_page})


def gerar_planilha(self):
    return redirect('site-natacao:homepage')