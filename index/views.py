from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Index
from .forms import TicketForm
# Create your views here.

def index(request):
    return HttpResponse('Hello world')



def home(request):
    return render(request, 'front/index.html')

def login(request):
    return render(request, 'front/login.html')

def register(request):
    return render(request, 'front/register.html')

def chamados(request):
    tickets = Index.objects.all().order_by('-created_at')
    form = TicketForm()
    
    if request.method == 'POST':
        form = TicketForm(request.POST)
        
        if form.is_valid():
            ticket = form.save()
            
            return redirect('/chamados')
        
    else:
        return render(request, 'front/chamados.html', {'tickets':tickets, 'form':form})