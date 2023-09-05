from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from MoFome import models as modelsMoFome
from django.db.models import Avg

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    modo_privacidade = models.IntegerField(default=0)
    receitas_avaliadas = models.ManyToManyField(modelsMoFome.Receita, related_name='avaliadores', blank=True)
    receitas_favoritas = models.ManyToManyField(modelsMoFome.Receita, related_name='favoritas', blank=True)
    
    
    def quantidade_de_receitas_postadas(self):
        return modelsMoFome.Receita.objects.filter(autor=self.user).count()
    
    def quantidade_de_comentarios(self):
        return modelsMoFome.Comentario.objects.filter(autor=self.user).count()
    
    def quantidade_de_topicos_postados(self):
        return modelsMoFome.Topico.objects.filter(autor=self.user).count()
    
    


    def __str__(self):
        return f'{self.user.username} Profile'
    