const box1 = document.querySelector('.box1');

box1.addEventListener('mouseover', function() {
    document.body.style.backgroundImage = "url(/static/Images/blood-sugar-levels.webp)";
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


const box2 = document.querySelector('.box2');

box2.addEventListener('mouseover', function() {
    document.body.style.backgroundImage = "url(/static/Images/mood-predictor.png)";
    document.body.style.backgroundColor = "#0d173f"
    document.body.style.backgroundRepeat = "no-repeat"; 
    document.body.style.backgroundSize = "fit";  
    document.body.style.backgroundPosition = "top";  
    document.body.style.zIndex = '10'; 
});

box2.addEventListener('mouseout', function() {
    document.body.style.backgroundImage = ''; 
    document.body.style.backgroundColor = '';
    document.body.style.backgroundRepeat = '';
    document.body.style.backgroundSize = '';
    document.body.style.backgroundPosition = '';
});


const box3 = document.querySelector('.box3');

box3.addEventListener('mouseover', function() {
    document.body.style.backgroundImage = "url(https://media.geeksforgeeks.org/wp-content/uploads/20231206171725/BMI-2.png)";
    document.body.style.backgroundColor = "#ffff94"
    document.body.style.backgroundRepeat = "no-repeat"; 
    document.body.style.backgroundSize = "contain";  
    document.body.style.backgroundPosition = "top";  
    document.body.style.zIndex = '10'; 
});

box3.addEventListener('mouseout', function() {
    document.body.style.backgroundImage = ''; 
    document.body.style.backgroundColor = '';
    document.body.style.backgroundRepeat = '';
    document.body.style.backgroundSize = '';
    document.body.style.backgroundPosition = '';
});
