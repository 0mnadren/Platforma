// naucni_rad_profil
const btnPrikaziPitanja = document.getElementById('btn_prikazi_profil_pitanja');
const btnSakrijPitanja = document.getElementById('btn_sakrij_profil_pitanja');
const formPitanja = document.getElementById('profil_form_pitanja');

window.addEventListener('load', function() {
    btnSakrijPitanja.style.display = 'none';
    formPitanja.style.display = 'none';
});

btnPrikaziPitanja.addEventListener('click', function() {
    btnPrikaziPitanja.style.display = 'none';
    btnSakrijPitanja.style.display = 'block';
    formPitanja.style.display = 'block'
});

btnSakrijPitanja.addEventListener('click', function() {
    btnPrikaziPitanja.style.display = 'block';
    btnSakrijPitanja.style.display = 'none';
    formPitanja.style.display = 'none';
});
