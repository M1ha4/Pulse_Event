document.addEventListener('DOMContentLoaded', () => {
    // ======= Prime Slider =======
    const slider = document.querySelector('.prime-slider');
    const slides = document.querySelectorAll('.prime-slider .slide');
    const leftArrow = document.querySelector('.prime-arrow.left');
    const rightArrow = document.querySelector('.prime-arrow.right');
    let currentIndex = 0;
    const slidesToShow = 2;

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
    const slideWidth = slider.querySelector('.slide').offsetWidth + 10; // +gap
    slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    }



    // ======= Show More for Events =======
    const showMoreBtn = document.getElementById('show-more-btn');
    const events = document.querySelectorAll('.event-card');
    let visibleCount = 9;

    events.forEach((event, index) => {
        if (index >= visibleCount) event.style.display = 'none';
    });

    showMoreBtn.addEventListener('click', () => {
        events.forEach(event => event.style.display = 'flex');
        showMoreBtn.style.display = 'none';
    });
});
