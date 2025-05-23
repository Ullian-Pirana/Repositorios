from django import forms
from .models import quarto

from django import forms
from .models import quarto

class quartoForms(forms.ModelForm):
    status_escolha = [
        (True, 'Disponível'),
        (False, 'Reservado'),
    ]

    status = forms.ChoiceField(choices=status_escolha, widget=forms.Select())

    class Meta:
        model = quarto
        fields = ['num_Quarto', 'qtd_Hospedes', 'estilo', 'tipo', 'valor', 'descricao', 'status', 'img']