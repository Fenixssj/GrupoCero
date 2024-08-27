document.addEventListener('DOMContentLoaded', (event) => {
    'use strict';
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            } else {
                event.preventDefault();
                const formData = new FormData(form);
                fetch(window.location.href, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    },
                })
                .then(response => response.text())
                .then(response => {
                    $('#mensajeEnviadoModal').modal('show');
                    form.reset();
                    form.classList.remove('was-validated');
                })
                .catch(error => console.error('Error al enviar formulario:', error));
            }
            form.classList.add('was-validated');
        }, false);
    });

    if (document.querySelector('#mensajeEnviadoModal').dataset.success === "true") {
        $('#mensajeEnviadoModal').modal('show');
    }
});
