
const box1 = document.querySelector('.box1');


box1.addEventListener('mouseover', function() {
    document.body.style.backgroundImage = "url('Assets2/Images/blood sugar levels.webp')";
    document.body.style.backgroundColor = "#373e40"
    document.body.style.backgroundRepeat = "no-repeat"; 
    document.body.style.backgroundSize = "fit";  
    document.body.style.backgroundPosition = "center";  
    document.body.style.zIndex = '10'; 
});

box1.addEventListener('mouseout', function() {
    document.body.style.backgroundImage = ''; 
    document.body.style.backgroundColor = '';
    document.body.style.backgroundRepeat = '';
    document.body.style.backgroundSize = '';
    document.body.style.backgroundPosition = '';
});
