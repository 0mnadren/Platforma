// naucni_rad_admin
const btnPrikazi = document.getElementById('btn_prikazi');
const btnSakrij = document.getElementById('btn_sakrij');
const divPitanja = document.getElementById('programski_poziv_pitanja');

window.addEventListener('load', function() {
    btnSakrij.style.display = 'none';
    divPitanja.style.display = 'none';
});

btnPrikazi.addEventListener('click', function() {
    btnPrikazi.style.display = 'none';
    btnSakrij.style.display = 'block';
    divPitanja.style.display = 'block'
});

btnSakrij.addEventListener('click', function() {
    btnPrikazi.style.display = 'block';
    btnSakrij.style.display = 'none';
    divPitanja.style.display = 'none';
});
