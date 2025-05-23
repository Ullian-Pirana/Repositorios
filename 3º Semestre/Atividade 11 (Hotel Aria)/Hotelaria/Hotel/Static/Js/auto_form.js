document.addEventListener('DOMContentLoaded', function() {
    const estiloField = document.getElementById('id_estilo');
    const tipoField = document.getElementById('id_tipo');
    const hospedesField = document.getElementById('id_qtd_Hospedes');
    const valorField = document.getElementById('id_valor');

    // Função para atualizar hóspedes automaticamente
    function atualizarHospedes() {
        const estilo = estiloField.value;
        if (estilo === 'Solteiro') {
            hospedesField.value = 1;
        } else if (estilo === 'Casal') {
            hospedesField.value = 2;
        } else if (estilo === 'Familia') {
            hospedesField.value = 4;
        }
    }

    // Função para calcular valor automaticamente
    function atualizarValor() {
        const estilo = estiloField.value;
        const tipo = tipoField.value;

        // Valores base por estilo
        const valoresBase = {
            'Solteiro': 150.00,
            'Casal': 200.00,
            'Familia': 285.00
        };

        // Porcentagem extra por tipo
        const acrescimos = {
            'Normal': 0,
            'Confort': 0.25,
            'Plus': 0.45,
            'Premium': 0.85
        };

        const valorBase = valoresBase[estilo] || 0;
        const acrescimo = acrescimos[tipo] || 0;

        const valorFinal = valorBase + (valorBase * acrescimo);
        valorField.value = valorFinal.toFixed(2);  // Define o valor com duas casas decimais
    }

    // Escuta mudança no campo estilo
    estiloField.addEventListener('change', function() {
        atualizarHospedes();
        atualizarValor();
    });

    // Escuta mudança no campo tipo
    tipoField.addEventListener('change', function() {
        atualizarValor();
    });
});