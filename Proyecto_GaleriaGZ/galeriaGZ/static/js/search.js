function BuscadorHtml(event) {
    event.preventDefault(); // Previene el envío del formulario

    // Obtiene el input de búsqueda
    const searchInput = document.querySelector('input[type="search"]');
    // Obtiene el valor de búsqueda del input
    const query = searchInput.value.trim().toLowerCase();

    // Redirección basada en el valor de búsqueda
    switch (query) {
        case "inicio":
            window.location.href = "inicio.html";
            break;
        case "nosotros":
            window.location.href = "nosotros.html";
            break;
        case "contacto":
            window.location.href = "contacto.html";
            break;
        case "categoria":
            window.location.href = "categoria.html";
            break;
        case "nueva obra":
            window.location.href = "ingresar_obra.html";
            break;
        default:
            // Mostrar mensaje en el placeholder si no se encuentra la categoría
            searchInput.value = '';
            searchInput.placeholder = "No existe categoría";
    }
}