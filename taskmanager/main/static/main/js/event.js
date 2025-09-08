document.addEventListener('DOMContentLoaded', () => {
    const slider = document.querySelector('.media-slider');
    const slides = document.querySelectorAll('.media-slider .media-item');
    const leftArrow = document.querySelector('.media-arrow.left');
    const rightArrow = document.querySelector('.media-arrow.right');
    let currentIndex = 0;
    const slidesToShow = 3; // Показываем 3 медиа одновременно

    rightArrow.addEventListener('click', () => {
        if (currentIndex < slides.length - slidesToShow) {
            currentIndex++;
            updateSlider();
        }
    });

    leftArrow.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateSlider();
        }
    });

    function updateSlider() {
        const slideWidth = slides[0].offsetWidth + 15; // 15px gap
        slider.style.transform = `translateX(-${slideWidth * currentIndex}px)`;
    }
});
