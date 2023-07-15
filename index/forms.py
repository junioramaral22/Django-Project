from django import forms 

from .models import Index

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Index
        fields = ('nome', 'localizacao', 'patrimonio')