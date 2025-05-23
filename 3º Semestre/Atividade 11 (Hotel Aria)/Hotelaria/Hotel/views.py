from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import *
from .forms import *

def is_gerente(user):
    return user.groups.filter(name="Gerente").exists()

def Homepage(request):
    context = {}
    dados_home = homepage.objects.all()
    context['dados_home'] = dados_home
    return render(request, 'homepage.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Login realizado com sucesso! Bem-vindo, {user.username}. ✅")
            return redirect('homepage')
        else:
            messages.error(request, "Usuário ou senha inválida. ❌")
            return render(request, 'Login.html')
    return render(request, 'Login.html')

@login_required
def alt_status(request, quarto_id, novo_status):
    try:
        q = quarto.objects.get(id=quarto_id)
        q.status = bool(int(novo_status))
        q.save()
        messages.success(request, "Status do quarto atualizado com sucesso! ✅")
    except quarto.DoesNotExist:
        messages.error(request, "Quarto não encontrado. ❌")
    return redirect('quartos')

@login_required
@user_passes_test(is_gerente, login_url='homepage')
def addQuarto(request):
    if request.method == 'POST':
        form = quartoForms(request.POST, request.FILES)        
        if form.is_valid():
            form.save()
            messages.success(request, "Quarto cadastrado com sucesso! ✅")
            return redirect('addQuarto')
        else:
            messages.error(request, "Erro ao cadastrar quarto. Verifique os dados e tente novamente. ❌")
    else:    
        form = quartoForms()
    context = {'form': form}
    return render(request, 'addQuartos.html', context)

@login_required
def verQuartos(request):
    quartos = quarto.objects.all()
    context = {'quartos': quartos}
    return render(request, 'quartos.html', context)

@login_required
def reservas(request):
    quartos = quarto.objects.all()
    context = {'quartos': quartos}
    return render(request, 'reservas.html', context)

@login_required
@user_passes_test(is_gerente, login_url='homepage')
def removerQuarto(request):
    if request.method == 'POST':
        quarto_id = request.POST.get('id')
        try:
            q = quarto.objects.get(id=quarto_id)
            q.delete()
            messages.success(request, f"Quarto {q.num_Quarto} removido com sucesso! 🗑️")
        except quarto.DoesNotExist:
            messages.error(request, "Quarto não encontrado. ❌")
        return redirect('removerQuarto')
    quartos = quarto.objects.all()
    context = {'quartos': quartos}
    return render(request, 'rmvQuartos.html', context)

def Sair(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso! 👋")
    return redirect('homepage')