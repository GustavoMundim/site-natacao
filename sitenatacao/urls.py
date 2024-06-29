from django.urls import path, include
from . import views
from django.shortcuts import redirect

app_name = 'site-natacao'

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('portfolio/', views.PortFolio.as_view(), name='portfolio'),
    path('inscricao/', views.Inscricao.as_view(), name='inscricao'),
    path('gerar/', views.gerar_planilha, name='planilha'),
    # path('inscricao/', views.inscricao, name='inscricao'),
    # path('verificar_inscricao/', views.verificar_inscricao, name='verificar_inscricao'),
    path('fotos/<int:id>', views.fotos, name='picture')
    
]
