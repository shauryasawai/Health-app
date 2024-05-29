let slideIndex = 0;
const slides = document.querySelectorAll('.slide');
const leftArrow = document.querySelector('.left-arrow');
const rightArrow = document.querySelector('.right-arrow');

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.remove('active');
        if (i === index) {
            slide.classList.add('active');
        }
    });
}

function nextSlide() {
    slideIndex = (slideIndex + 1) % slides.length;
    showSlide(slideIndex);
}

function prevSlide() {
    slideIndex = (slideIndex - 1 + slides.length) % slides.length;
    showSlide(slideIndex);
}

rightArrow.addEventListener('click', nextSlide);
leftArrow.addEventListener('click', prevSlide);

// Initialize the slideshow
showSlide(slideIndex);







const leftArrow_2 = document.querySelector('.left-arrow_2');
const rightArrow_2 = document.querySelector('.right-arrow_2');
const cards = document.querySelector('.cards');

let currentIndex = 0;

leftArrow_2.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateCardPosition();
    }
});

rightArrow_2.addEventListener('click', () => {
    if (currentIndex < cards.children.length - 1) {
        currentIndex++;
        updateCardPosition();
    }
});

function updateCardPosition() {
    const cardWidth = cards.children[0].getBoundingClientRect().width;
    cards.style.transform = `translateX(${-currentIndex * (cardWidth + 20)}px)`;
}


document.addEventListener("DOMContentLoaded", function() {
    const cards_6 = document.querySelectorAll('.card_6');
    cards_6.forEach(card => {
        const img = card.querySelector('img');
        img.onload = function() {
            img.style.display = 'block';
        };
        img.onerror = function() {
            img.style.display = 'none';
        };
        img.src = img.src; // Trigger image load
    });
});