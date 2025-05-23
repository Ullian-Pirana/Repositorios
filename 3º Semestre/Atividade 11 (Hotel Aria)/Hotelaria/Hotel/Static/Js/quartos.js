function toggleExpand(element) {
    element.classList.toggle('expanded');
}

function mudarStatus(quartoId, novoStatus) {
    const confirmar = confirm("Deseja realmente alterar o status deste quarto?");
    if (!confirmar) return;

    fetch("/alterar-status-quarto/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: `id=${quartoId}&status=${novoStatus}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Status alterado com sucesso!");
            location.reload();
        } else {
            alert("Erro ao alterar status: " + data.error);
        }
    })
    .catch(error => {
        alert("Erro na requisição.");
    });
}

// Função para obter o CSRF Token dos cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome que queremos
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}