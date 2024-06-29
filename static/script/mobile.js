
let menuMobile = document.querySelector('#menu-icon')
let navbar = document.querySelector('.navigation')

menuMobile.onclick = () => {
    menuMobile.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}
