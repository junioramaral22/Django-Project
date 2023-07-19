from django import forms 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Index

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Index
        fields = ('nome', 'localizacao', 'patrimonio')
        
        

class NewUserForm(UserCreationForm):
	username = forms.CharField(required=True)
	
	
	class Meta:	
		model = User

		fields = ("username", "password1")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		
		if commit:
			user.save()
		return user