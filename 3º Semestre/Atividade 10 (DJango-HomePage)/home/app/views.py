from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Substitua com o nome do seu template