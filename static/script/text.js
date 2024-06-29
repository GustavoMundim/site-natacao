window.addEventListener('scroll', () => {
    let text = document.getElementById('text-titulo');
    let scroll = window.scrollY;
    
    if(scroll > 350){
        text.style.marginTop = scroll * 2.5 + 'px';
        text.style.display = 'none';} else{
            text.style.display = 'block'
            text.style.marginTop = scroll * 2.5 + 'px';
        }
});
