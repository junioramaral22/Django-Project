from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Index(models.Model):

    
            
    nome = models.CharField(max_length=10, default='')
    
    localizacao = models.TextField(default='', max_length=10)
    
    patrimonio = models.TextField(default='', max_length=10)    
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.nome