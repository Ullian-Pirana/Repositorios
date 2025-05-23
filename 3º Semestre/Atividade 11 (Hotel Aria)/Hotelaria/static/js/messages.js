const alerts = document.querySelectorAll('.alert');

alerts.forEach(alert => {
    // Tempo que a mensagem ficará visível (em ms)
    setTimeout(() => {
        alert.style.opacity = '0';
        alert.style.transform = 'translateX(50px)';
        setTimeout(() => {
            alert.remove();
        }, 500); 
    }, 3500); 
});
