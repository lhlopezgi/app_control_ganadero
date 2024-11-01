function openTab(evt, tabName) {
    // Ocultar todos los contenidos de las pestañas
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";  
    }

    // Remover la clase 'active' de todos los enlaces de pestaña
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Mostrar el contenido de la pestaña activa
    document.getElementById(tabName).style.display = "block";  
    evt.currentTarget.className += " active";  // Añadir la clase 'active' al botón de pestaña
}

// Mostrar la primera pestaña de inicio por defecto
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".tablinks.active").click();
});



    // Remover la clase 'active' de todos los enlaces de pestaña
    tablinks = document.querySelectorAll('.sidebar ul li a');
    tablinks.forEach(link => {
        link.classList.remove('active');
    });

    // Mostrar el contenido de la pestaña activa
    document.getElementById(tabName).style.display = "block";  
    evt.currentTarget.classList.add('active');  // Añadir la clase 'active' al botón de pestaña


// Asegúrate de que el evento de DOMContentLoaded llame a showTab correctamente
document.addEventListener("DOMContentLoaded", function() {
    var defaultTab = document.querySelector('.sidebar-menu a');
    if (defaultTab) {
        defaultTab.click(); // Llama al primer enlace del menú al cargar
    }
});


function toggleRegistro() {
    const submenu = document.getElementById('register-menu');
    submenu.classList.toggle('show');
}


    function openForm(evt, formId) {
        // Ocultar todos los contenidos de las pestañas
        var tabcontent = document.getElementsByClassName("tabcontent");
        for (var i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }

        // Ocultar todos los formularios
        hideAllForms();

        // Mostrar el formulario seleccionado
        document.getElementById(formId).style.display = "block";
    }

    function hideAllForms() {
        const forms = document.querySelectorAll('.form-content');
        forms.forEach(form => {
            form.style.display = 'none';
        });
    }

    function showRegisterMenu() {
        var registerMenu = document.getElementById("register-menu");
        registerMenu.style.display = registerMenu.style.display === "none" ? "block" : "none";
    }
    
    function showForm(formId) {
        hideAllSections(); // Ocultar todos los formularios y el Dashboard
        document.getElementById(formId).style.display = 'block'; // Mostrar el formulario seleccionado
    }
    

    function hideDashboard() {
        const dashboardContent = document.getElementById('dashboard-content');
        if (dashboardContent) {
            dashboardContent.style.display = 'none'; // Ocultar el contenido del dashboard
        }
    }
    

    function showTab(event, tabId) {
        hideAllForms(); // Ocultar todos los formularios
        hideAllSections(); // Ocultar todas las secciones
        const tabs = document.querySelectorAll('.tabcontent');
        tabs.forEach(tab => {
            tab.style.display = 'none'; // Ocultar contenido de cada pestaña
        });
        document.getElementById(tabId).style.display = 'block'; // Mostrar la pestaña seleccionada
    }
    
    
    
   function toggleInventario() {
        const submenu = document.getElementById('inventario-submenu');
        submenu.classList.toggle('show');
    }
    
    function showVacas() {
        hideAllSections(); // Ocultar todas las secciones
        document.getElementById('vacas').style.display = 'block'; // Mostrar sección de Vacas
    }
    
    function showTerneros() {
        hideAllSections(); // Ocultar todas las secciones
        document.getElementById('terneros').style.display = 'block'; // Mostrar sección de Terneros
    }
    
    function hideAllSections() {
        document.getElementById('dashboard-content').style.display = 'none'; // Ocultar Dashboard
        document.getElementById('vacas').style.display = 'none';
        document.getElementById('terneros').style.display = 'none';
        const forms = document.querySelectorAll('.form-content');
        forms.forEach(form => {
            form.style.display = 'none'; // Ocultar cada formulario
        });
    }

    function showDashboard() {
        hideAllSections();
        document.getElementById('dashboard-content').style.display = 'block';
    }


    

   
    
    
    
    
    
    function showSection(sectionId) {
        hideAllSections();
        document.getElementById(sectionId).classList.add('show');
    }
    
    function hideAllSections() {
        const sections = document.querySelectorAll('.tabcontent, .form-content');
        sections.forEach(section => section.classList.remove('show'));
    }
    