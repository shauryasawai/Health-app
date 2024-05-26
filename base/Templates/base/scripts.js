let slideIndex = 0;
const slides = document.querySelector('.slides');
const slideCount = slides.children.length;

function showSlide(index) {
    if (index >= slideCount) {
        slideIndex = 0;
    } else if (index < 0) {
        slideIndex = slideCount - 1;
    } else {
        slideIndex = index;
    }
    slides.style.transform = `translateX(-${slideIndex * 100}%)`;
}

function moveSlide(direction) {
    showSlide(slideIndex + direction);
}

setInterval(() => {
    moveSlide(1);
}, 3000);

document.querySelector('.prev').addEventListener('click', () => {
    moveSlide(-1);
});

document.querySelector('.next').addEventListener('click', () => {
    moveSlide(1);
});
