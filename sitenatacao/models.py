from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Inicio(models.Model):
    imagem_fundo = models.ImageField(upload_to='thumb-site')
    titulo = models.CharField(max_length=100)
    subtitulo = models.TextField(max_length=5000)

    class Meta:
        verbose_name = 'Configuração de Início Ajuste'

    def __str__(self):
        return self.titulo
    
    @mark_safe
    def imagem_wallpaper(self):
     return f'<img width="300px" src="/media/{self.imagem_fundo}">'


class Inscrito(models.Model):
     nome = models.CharField(max_length=100)
     sobrenome = models.CharField(max_length=100)
     idade = models.CharField(max_length=10)

     class Meta:
        verbose_name = 'Configuração de Inscritos Ajuste'

     def __str__(self):
         return "Aluno {} {}".format(self.nome, self.sobrenome)


class Foto(models.Model):
     foto = models.ImageField(upload_to='fotos')
     descricao = models.TextField(max_length=3000)
     data = models.DateTimeField(default=timezone.now)


     class Meta:
        verbose_name = 'Configuração de Portfolio Ajuste'

     def __str__(self):
          return "Imagem: {}".format(self.id)
 

     @mark_safe
     def icone(self):
          return f'<img width="80px" src="/media/{self.foto}">'






