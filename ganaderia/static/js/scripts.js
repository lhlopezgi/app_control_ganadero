function hideAllForms() {
    var forms = document.getElementsByClassName("form-content");
    for (var i = 0; i < forms.length; i++) {
        forms[i].style.display = "none"; // Ocultar todos los formularios
    }

    // Ocultar el contenido del dashboard
    document.getElementById("dashboard-content").style.display = "none"; 

    // Limpiar las tarjetas de vacas o terneros (cuando se hace clic en otros enlaces)
    document.getElementById('cards-container').innerHTML = ''; 
    document.getElementById('cards-container').style.display = "none";  // Asegúrate de ocultar el contenedor de tarjetas
}


// Función para mostrar el dashboard y ocultar las tarjetas y formularios
function showDashboard() {
    // Ocultar cualquier formulario o tarjeta
    hideAllForms(); 

    // Mostrar el dashboard
    document.getElementById("dashboard-content").style.display = "block";
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
            // Cuando se hace clic en otro enlace, volvemos al dashboard y ocultamos las tarjetas
            showDashboard(); // Volver al dashboard
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
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Procesar datos...
    })
    .catch(error => {
        console.error('Error:', error);
        showToast('Hubo un error al procesar la solicitud', 'error');
    });

}






document.addEventListener("DOMContentLoaded", function () {
    // Se inyectan los valores de Django aquí
    const lecheHoy = parseFloat(document.getElementById('leche-hoy').textContent) || 0;
    const lecheUltimos30Dias = parseFloat(document.getElementById('leche-ultimos-30-dias').textContent) || 0;

    const ternerosMachos = parseInt(document.getElementById('terneros-machos').textContent) || 0;
    const ternerosHembras = parseInt(document.getElementById('terneros-hembras').textContent) || 0;

    // Gráfico de barras para la leche producida
    const ctxLeche = document.getElementById('leche-chart').getContext('2d');
    const lecheChart = new Chart(ctxLeche, {
        type: 'bar',
        data: {
            labels: ['Leche Producida Hoy', 'Leche Últimos 30 Días'],
            datasets: [{
                label: 'Litros de Leche',
                data: [lecheHoy, lecheUltimos30Dias],
                backgroundColor: '#c76565',
                borderColor: '#6d0a0a',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Gráfico Donut para los Terneros
    const ctxTerneros = document.getElementById('donut-chart').getContext('2d');
    const donutChart = new Chart(ctxTerneros, {
        type: 'doughnut',
        data: {
            labels: ['Machos', 'Hembras'],
            datasets: [{
                label: 'Sexo de los Terneros',
                data: [ternerosMachos, ternerosHembras],
                backgroundColor: ['#076945', '#c59417'],
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top'
                }
            }
        }
    });
});


function showToast(message, type) {
    var toast = document.createElement("div");
    toast.classList.add("toast");

    // Asegúrate de que se aplica la clase .toast-error si el tipo es "error"
    if (type === "error") {
        toast.classList.add("toast-error");  // Clase con fondo rojo
    }

    toast.innerText = message;

    // Añadir el toast al body
    document.body.appendChild(toast);

    // Eliminar el toast después de unos segundos
    setTimeout(function() {
        toast.classList.add("toast-hide");
        setTimeout(function() {
            toast.remove();
        }, 500);
    }, 3000);  // Desaparece después de 3 segundos
}












// Datos de las vacas y terneros (mantenemos los mismos que ya habías definido)
const vacas = [
    {
      nombre: "Vaca 1",
      edad: "5 años",
      raza: "Holstein",
      produccionPromedio: "25 L/día",
      color: "Blanco y negro",
      imagen: "/static/img/imagen1vaca.jpg"


    },
    {
      nombre: "Vaca 2",
      edad: "4 años",
      raza: "Gyr",
      produccionPromedio: "18 L/día",
      color: "Marrón claro",
      imagen: "/static/img/imagen2vaca.jpg"

    },
    {
        nombre: "Vaca 3",
        edad: "2 años",
        raza: "Normando",
        produccionPromedio: "15 L/día",
        color: "Blanco y Cafe",
        imagen: "/static/img/imagen3vaca.jpg"

      },
      {
        nombre: "Vaca 4",
        edad: "3 años",
        raza: "Jersey",
        produccionPromedio: "10 L/día",
        color: "Marrón Oscuro",
        imagen: "/static/img/imagen4vaca.jpg"

      },
    // Añadir más vacas aquí...
  ];
  
  const terneros = [
    {
      nombre: "Ternero 1",
      edad: "6 meses",
      raza: "Charolais",
      produccionPromedio: "N/A",
      color: "Blanco",
      imagen: "/static/img/imagen5vaca.jpg"

    },
    {
      nombre: "Ternero 2",
      edad: "4 meses",
      raza: "Limousin",
      produccionPromedio: "N/A",
      color: "Marrón",
      imagen: "/static/img/imagen6vaca.jpg"

    },
    {
        nombre: "Ternero 3",
        edad: "3 meses",
        raza: "Normando",
        produccionPromedio: "N/A",
        color: "Blanco",
        imagen: "/static/img/imagen7vaca.jpg"

      },
      {
        nombre: "Ternero 4",
        edad: "4 meses",
        raza: "Gyr",
        produccionPromedio: "N/A",
        color: "Marrón Claro",
        imagen: "/static/img/imagen8vaca.jpg"

      },
    // Añadir más terneros aquí...
  ];
  
 

  function generarTarjetasGenericas(animales) {
    const container = document.getElementById('cards-container');
    container.innerHTML = ''; // Limpiar las tarjetas previas

    animales.slice(0, 4).forEach(animal => {
        const card = document.createElement('div');
        card.classList.add('card');
        
        card.innerHTML = `
            <img src="${animal.imagen}" alt="${animal.nombre}">
            <div class="card-content">
                <h3>${animal.nombre}</h3>
                <p><strong>Edad:</strong> ${animal.edad}</p>
                <p><strong>Raza:</strong> ${animal.raza}</p>
                <p><strong>Producción promedio:</strong> ${animal.produccionPromedio}</p>
                <p><strong>Color:</strong> ${animal.color}</p>
            </div>
        `;
        
        container.appendChild(card);
    });
}



function showInfo(type) {
    // Primero ocultar cualquier formulario activo
    hideAllForms();

    // Mostrar el contenedor de tarjetas
    const cardsContainer = document.getElementById('cards-container');
    cardsContainer.style.display = 'block'; // Asegúrate de que el contenedor esté visible

    if (type === "vacas") {
        generarTarjetasGenericas(vacas);
    } else if (type === "terneros") {
        generarTarjetasGenericas(terneros);
    }
}





