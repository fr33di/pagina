const menuToggle = document.getElementById('menuToggle');
const menuMobile = document.getElementById('menuMobile');
const menuLinks = document.querySelectorAll('.menu a, .menu-mobile a');

// Abrir/cerrar hamburguesa
menuToggle.addEventListener('click', e => {
    e.stopPropagation();
    menuMobile.classList.toggle('active');
});

// Abrir/cerrar submenús móviles
function toggleSubmenu(e){
    e.preventDefault();
    e.stopPropagation();
    const submenu = e.target.nextElementSibling;
    if(submenu) submenu.classList.toggle('active');
}

// Mostrar contenido y resaltar menú
function showContent(id, clickedLink){
    // Mostrar la sección correcta
    document.querySelectorAll('.contenido-section').forEach(sec => sec.classList.remove('active'));
    const targetSection = document.getElementById(id);
    if(targetSection) targetSection.classList.add('active');

    // Quitar clase active de todos los links
    menuLinks.forEach(link => link.classList.remove('active'));

    // Marcar el link clickeado como activo
    if(clickedLink) clickedLink.classList.add('active');

    // También resaltar el link PC que coincide
    menuLinks.forEach(link => {
        if(link.getAttribute('data-target') === id){
            link.classList.add('active');
        }
    });

    // Cerrar menú móvil
    menuMobile.classList.remove('active');
    document.querySelectorAll('.submenu-mobile').forEach(sub => sub.classList.remove('active'));
}

// Agregar evento click a todos los links con data-target
menuLinks.forEach(link => {
    const target = link.getAttribute('data-target');
    if(target){
        link.addEventListener('click', function(e){
            e.stopPropagation();
            showContent(target, this);
        });
    }
});

// Cerrar menú si se hace clic fuera
document.addEventListener('click', e => {
    if(!menuMobile.contains(e.target) && !menuToggle.contains(e.target)){
        menuMobile.classList.remove('active');
        document.querySelectorAll('.submenu-mobile').forEach(sub => sub.classList.remove('active'));
    }
});









