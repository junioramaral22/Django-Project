from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Index
from .forms import TicketForm
from .forms import NewUserForm
# Create your views here.


def index(request):
    return HttpResponse('Hello world')


def home(request):
    return render(request, 'front/index.html')


def login(request):
    return render(request, 'front/login.html')


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/accounts/login")
    form = NewUserForm()
    return render(request=request, template_name="front/register.html", context={"register_form": form})


@login_required
def chamados(request):
    if request.user.is_superuser:
        tickets = Index.objects.all().order_by('-created_at')
        form = TicketForm()
    else:
        tickets = Index.objects.all().order_by('-created_at').filter(user=request.user)
        form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('/chamados')

    else:
        return render(request, 'front/chamados.html', {'tickets': tickets, 'form': form})


@login_required
def editChamados(request, id):
    ticket = get_object_or_404(Index, pk=id)
    form = TicketForm(instance=ticket)

    if (request.method == 'POST'):
        form = TicketForm(request.POST, instance=ticket)

        if (form.is_valid()):
            ticket.save()
            return redirect('/chamados')
        else:
            return render(request, 'front/edit.html', {'form': form, 'ticket': ticket})

    else:
        return render(request, 'front/edit.html', {'form': form, 'ticket': ticket})


@login_required
def deleteChamados(request, id):
    ticket = get_object_or_404(Index, pk=id)
    ticket.delete()
    return redirect('/chamados')
