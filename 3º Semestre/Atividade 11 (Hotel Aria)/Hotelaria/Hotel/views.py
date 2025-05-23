from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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
def alt_status(request):
    if request.method == 'POST':
        quarto_id = request.POST.get('id')
        novo_status = request.POST.get('status')

        if not quarto_id or not novo_status:
            return JsonResponse({'success': False, 'error': 'Parâmetros ausentes'})

        try:
            quarto_obj = quarto.objects.get(id=quarto_id)
            quarto_obj.status = True if novo_status == '1' else False
            quarto_obj.save()
            return JsonResponse({'success': True})
        except quarto.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Quarto não encontrado'})
    return JsonResponse({'success': False, 'error': 'Método inválido'})

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
    quartos_reservados = quarto.objects.filter(status=False)  # False = Reservado
    context = {'quartos': quartos_reservados}
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

@login_required
@user_passes_test(is_gerente, login_url='homepage')
def add_colaborador(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe. ❌')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            funcionario_group, created = Group.objects.get_or_create(name='Funcionario')
            user.groups.add(funcionario_group)
            user.save()
            messages.success(request, f'Colaborador {username} cadastrado com sucesso! ✅')
            return redirect('addColaborador')

    return render(request, 'addColaborador.html')

def Sair(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso! 👋")
    return redirect('homepage')