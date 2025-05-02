document.getElementById('cambiar-ruta').addEventListener('click', () => {
    fetch('/nueva-ruta')
        .then(response => response.json())
        .then(data => {
            const rutaElement = document.getElementById('ruta');
            rutaElement.innerHTML = '';
            data.ruta.forEach(ciudad => {
                const li = document.createElement('li');
                li.innerHTML = `<i class="fas fa-city"></i> ${ciudad}`;
                rutaElement.appendChild(li);
            });
            document.getElementById('distancia').textContent = data.distancia;
        })
        .catch(error => console.error('Error:', error));
});