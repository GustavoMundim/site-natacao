const barra_navegacao = document.querySelector('header');
let ultimoScroll = 0;

window.addEventListener('scroll', function() {
    const scrollAtual = window.scrollY;

    if (scrollAtual > ultimoScroll) {
        barra_navegacao.style.transform = 'translateY(-100%)';
    } else {
        barra_navegacao.style.transform = 'translateY(0)';
    }

    ultimoScroll = scrollAtual <= 0 ? 0 : scrollAtual;
});
