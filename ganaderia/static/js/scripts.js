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
    const form = document.getElementById(formId);
    if (form) {
        form.style.display = 'block';
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

function toggleRegisterMenu(event) {
    event.preventDefault(); // Evita que el enlace navegue
    var registerMenu = document.getElementById("register-menu");
    if (registerMenu) {
        registerMenu.style.display = registerMenu.style.display === 'none' ? 'block' : 'none';
    }
}

function toggleInventoryMenu(event) {
    event.preventDefault(); // Evita que el enlace navegue
    var inventoryMenu = document.getElementById("inventory-menu");
    if (inventoryMenu) {
        inventoryMenu.style.display = inventoryMenu.style.display === 'none' ? 'block' : 'none';
    }
}

// Manejo de clic en los enlaces del menú
document.querySelectorAll('.sidebar-menu a').forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Evitar que el enlace recargue la página
        const target = this.getAttribute('data-target'); // Obtener el ID del destino

        // Si se hace clic en el enlace de registro, alternar el submenú
        if (target === 'register-menu') {
            toggleRegisterMenu(event);
        } else {
            showForm(target); // Mostrar el formulario correspondiente
        }

        if (target === 'inventory-menu') {
            toggleInventoryMenu(event);
        } else {
            showForm(target); // Mostrar el formulario correspondiente
        }
    });
});



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

ddocument.getElementById('ternero_create' ).querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del formulario

    const form = this; // El formulario que está siendo enviado
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Obtener el token CSRF desde las cookies
        }
    })
    .then(response => response.json())
    .then(data => {
        const messageContainer = document.getElementById('message-container');
        
        // Limpiar mensajes anteriores
        messageContainer.innerHTML = '';
        
        if (data.message) {
            messageContainer.innerHTML = `<div>${data.message}</div>`;
            messageContainer.style.display = 'block';  // Mostrar el contenedor de mensajes
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
});


ddocument.getElementById('produccion_leche_create').querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del formulario

    const form = this; // El formulario que está siendo enviado
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Obtener el token CSRF desde las cookies
        }
    })
    .then(response => response.json())
    .then(data => {
        const messageContainer = document.getElementById('message-container');
        
        // Limpiar mensajes anteriores
        messageContainer.innerHTML = '';
        
        if (data.message) {
            messageContainer.innerHTML = `<div>${data.message}</div>`;
            messageContainer.style.display = 'block';  // Mostrar el contenedor de mensajes
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
});

document.getElementById('peso_vaca_create').querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del formulario

    const form = this; // El formulario que está siendo enviado
    const formData = new FormData(form);  // Asegúrate de que el formData esté enviando los campos correctos

    fetch(form.action, {
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

        if (data.message) {
            messageContainer.innerHTML = `<div>${data.message}</div>`;
            messageContainer.style.display = 'block';  // Mostrar el contenedor de mensajes
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
});

document.getElementById('peso_ternero_create').querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del formulario

    const form = this; // El formulario que está siendo enviado
    const formData = new FormData(form);  // Asegúrate de que el formData esté enviando los campos correctos

    fetch(form.action, {
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

        if (data.message) {
            messageContainer.innerHTML = `<div>${data.message}</div>`;
            messageContainer.style.display = 'block';  // Mostrar el contenedor de mensajes
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
});

