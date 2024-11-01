
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


function showForm(formId) {
    // Oculta todos los formularios
    document.querySelectorAll('.form-content').forEach(form => {
        form.style.display = 'none';
    });

    // Muestra el formulario específico
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
    hideAllSections(); // Ocultar todas las pestañas
    document.getElementById(tabName).style.display = "block"; // Mostrar la pestaña activa
    evt.currentTarget.className += " active"; // Añadir clase activa
}

function toggleRegisterMenu(event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del enlace
    var registerMenu = document.getElementById("register-menu");
    registerMenu.style.display = registerMenu.style.display === "none" ? "block" : "none"; // Mostrar/ocultar el menú de registro
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
    });
});


    