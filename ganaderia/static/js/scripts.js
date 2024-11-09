function hideAllForms() {
    var forms = document.getElementsByClassName("form-content");
    for (var i = 0; i < forms.length; i++) {
        forms[i].style.display = "none"; // Ocultar todos los formularios
    }
    document.getElementById("dashboard-content").style.display = "none"; // Ocultar el contenido del dashboard
}

function showDashboard(event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del enlace
    hideAllForms(); // Ocultar todos los formularios
    document.getElementById("dashboard-content").style.display = "block"; // Mostrar el contenido del dashboard
}

// Muestra el formulario específico
function showForm(formId) {
    hideAllForms(); // Ocultar todos los formularios
    const form = document.getElementById(formId);
    if (form) {
        form.style.display = 'block'; // Mostrar el formulario seleccionado
    } else {
        console.error("No se encontró el formulario con el ID: " + formId);
    }
}

// Mostrar la primera pestaña por defecto
document.addEventListener("DOMContentLoaded", function() {
    const defaultTab = document.querySelector('.tablinks.active');
    if (defaultTab) {
        defaultTab.click();
    } else {
        showDashboard(); // Mostrar el dashboard por defecto
    }
});

// Manejo de clic en las pestañas
function openTab(evt, tabName) {
    hideAllForms(); // Ocultar todas las pestañas
    document.getElementById(tabName).style.display = "block"; // Mostrar la pestaña activa
    evt.currentTarget.className += " active"; // Añadir clase activa
}

function toggleMenu(event, menuId) {
    event.preventDefault(); // Evita que el enlace recargue la página
    var menu = document.getElementById(menuId);
    if (menu) {
        // Alterna la visibilidad del submenú
        menu.style.display = (menu.style.display === 'none' || menu.style.display === '') ? 'block' : 'none';
        
        console.log('Toggling menu:', menuId);  // Esto te ayudará a verificar si el ID del menú es correcto.

    }
}


// Manejo de clic en los enlaces del menú
document.querySelectorAll('.sidebar-menu a').forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Evitar que el enlace recargue la página
        const target = this.getAttribute('data-target'); // Obtener el ID del destino

        if (target === 'register-menu') {
            toggleMenu(event, 'register-menu'); // Alternar el submenú de registro
        } else if (target === 'inventory-menu') {
            toggleMenu(event, 'inventory-menu'); // Alternar el submenú de inventario
        } else {
            showForm(target); // Mostrar el formulario correspondiente
        }
    });
});

// Obtener el token CSRF desde las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Manejo de envío de formularios
function handleFormSubmit(formId, url, event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del formulario

    const form = document.getElementById(formId); // El formulario que está siendo enviado
    const formData = new FormData(form); // FormData para enviar los datos del formulario

    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Obtener el token CSRF desde las cookies
        }
    })
    .then(response => response.json())
    .then(data => {
        const messageContainer = document.getElementById('message-container');
        messageContainer.innerHTML = ''; // Limpiar mensajes anteriores
        
        // Mostrar mensaje de éxito o errores
        if (data.message) {
            messageContainer.innerHTML = `<div>${data.message}</div>`;
            messageContainer.style.display = 'block';
        }
        if (data.errors) {
            for (const error of data.errors) {
                messageContainer.innerHTML += `<div>${error}</div>`;
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}



// Selecciona todos los mensajes de alerta para aplicar el efecto de desvanecimiento
document.addEventListener('DOMContentLoaded', function () {
    const messages = document.querySelectorAll('.fade-message');
    messages.forEach((message) => {
        // Espera 3 segundos y luego aplica la clase 'fade-out'
        setTimeout(() => {
            message.classList.add('fade-out');
        }, 2000);

        // Elimina el mensaje del DOM cuando la animación finalice
        message.addEventListener('animationend', () => {
            message.remove();
        });
    });
});


function toggleRegisterMenu(event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del enlace
    var menu = document.getElementById('register-menu');
    if (menu) {
        // Alternar la visibilidad del submenú
        menu.style.display = (menu.style.display === 'block') ? 'none' : 'block';
    }
}

