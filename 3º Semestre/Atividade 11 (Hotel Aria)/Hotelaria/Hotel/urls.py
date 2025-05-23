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
    path('alterar-status-quarto/', views.alt_status, name='alterar_Status'),
    path('addColaborador', views.add_colaborador, name='addColaborador')
]