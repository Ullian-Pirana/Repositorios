from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Homepage, name='homepage'),
    path('login', views.Login, name='login'),
    path('logout', views.Sair, name='logout'),
    path('addQuarto', views.addQuarto, name="addQuarto"),
    path('quartos', views.verQuartos, name="quartos"),
    path('reservas', views.reservas, name="reservas"),
    path('removerQuarto', views.removerQuarto, name="removerQuarto"),
    path('alterarStatus/<int:quarto_id>/<int:novo_status>/', views.alt_status, name='alterarStatus')
]