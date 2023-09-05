from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import pytz

class Receita(models.Model):
    title = models.CharField(max_length=80)
    ingredientes = models.TextField()
    descricao = models.TextField()
    modo_de_preparo = models.TextField()
    imagem = models.ImageField(default='MoFome.jpg', upload_to='receita_pics')
    data_do_post = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    avaliacao = models.IntegerField()
    quantidade_de_avaliacoes = models.IntegerField()
    horas = models.IntegerField()
    minutos = models.IntegerField()
    custo = models.IntegerField()
    dificuldade = models.IntegerField()
    pessoas = models.IntegerField()

    media = models.DecimalField(max_digits=4,  
        decimal_places=2,  
        null=True, 
        blank=True,
    )


    
    def data_post_brasil(self):
        fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')
        data_brasil= self.data_do_post.astimezone(fuso_horario_brasil)
        return data_brasil.strftime('%d/%m/%Y às %H:%M:%S')
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('receitas-detail', kwargs={'pk': self.pk})

class Topico(models.Model):
    title = models.CharField(max_length=80)
    discussão = models.TextField()
    data_do_post = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def data_post_brasil(self):
        fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')
        data_brasil= self.data_do_post.astimezone(fuso_horario_brasil)
        return data_brasil.strftime('%d/%m/%Y às %H:%M:%S')

        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('topicos-detail', kwargs={'pk': self.pk})



class Comentario(models.Model):
    receita = models.ForeignKey(Receita, related_name="comentarios", on_delete=models.CASCADE)
    comentario = models.TextField()
    data_do_comentario = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def data_comentario_brasil(self):
        fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')
        data_brasil= self.data_do_comentario.astimezone(fuso_horario_brasil)
        return data_brasil.strftime('%d/%m/%Y às %H:%M:%S')

    def __str__(self):
        return self.receita.title
    

class ComentarioTopico(models.Model):
    topico = models.ForeignKey(Topico, related_name="comentarios_topicos", on_delete=models.CASCADE)
    comentario = models.TextField()
    data_do_comentario = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def data_comentario_brasil(self):
        fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')
        data_brasil= self.data_do_comentario.astimezone(fuso_horario_brasil)
        return data_brasil.strftime('%d/%m/%Y às %H:%M:%S')

    def __str__(self):
        return self.topico.title
    