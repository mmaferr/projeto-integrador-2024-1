function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' }); // Rola suavemente para a seção
    }
}

document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener('scroll', function() {
        var elemento = document.querySelector('.retangulo-pontos-fortes');
        var posicaoElemento = elemento.getBoundingClientRect().top;
        var alturaTela = window.innerHeight;
        
        if (posicaoElemento < alturaTela) {
            elemento.classList.add('aparecer');
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener('scroll', function() {
        var elemento = document.querySelector('.avaliacoes');
        var posicaoElemento = elemento.getBoundingClientRect().top;
        var alturaTela = window.innerHeight;
        
        if (posicaoElemento < alturaTela) {
            elemento.classList.add('aparecer');
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener('scroll', function() {
        var elemento1 = document.querySelector('.cursos-cabecalho-container');
        var posicaoElemento1 = elemento1.getBoundingClientRect().top;
        var alturaTela = window.innerHeight;
        
        if (posicaoElemento1 < alturaTela) {
            elemento1.classList.add('aparecer');
        }
        
        var elemento2 = document.querySelector('.cursos-card-1');
        var posicaoElemento2 = elemento2.getBoundingClientRect().top;
        
        if (posicaoElemento2 < alturaTela) {
            elemento2.classList.add('aparecer');
        }
        
        var elemento3 = document.querySelector('.cursos-card-2');
        var posicaoElemento3 = elemento3.getBoundingClientRect().top;
        
        if (posicaoElemento3 < alturaTela) {
            elemento3.classList.add('aparecer');
        }
    });
});

function menuShow() {
    let menuMobile = document.querySelector('.mobile-menu');
    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
        document.querySelector('.icon').src = "{% static 'img/nav-home-page/menu_white_36dp.svg%}";
    } else {
        menuMobile.classList.add('open');
        document.querySelector('.icon').src = "{% static 'img/nav-home-page/close_white_36dp.svg}";
    }
}