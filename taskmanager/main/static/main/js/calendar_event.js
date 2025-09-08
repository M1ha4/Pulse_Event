document.addEventListener('DOMContentLoaded', () => {
    // ===== PRIME SLIDER =====
    const slider = document.querySelector('.prime-slider');
    const slides = document.querySelectorAll('.prime-slider .prime-slide');
    const leftArrow = document.querySelector('.prime-arrow.left');
    const rightArrow = document.querySelector('.prime-arrow.right');
    let currentIndex = 0;
    const slidesToShow = 2;

    function updateSlider() {
        if (slides.length <= slidesToShow) {
            leftArrow.style.display = 'none';
            rightArrow.style.display = 'none';
            return;
        }
        const slideWidth = slider.querySelector('.prime-slide').offsetWidth;
        slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    }

    if (rightArrow) {
        rightArrow.addEventListener('click', () => {
            if (currentIndex < slides.length - slidesToShow) {
                currentIndex++;
                updateSlider();
            }
        });
    }

    if (leftArrow) {
        leftArrow.addEventListener('click', () => {
            if (currentIndex > 0) {
                currentIndex--;
                updateSlider();
            }
        });
    }

    updateSlider();

    // ===== SHOW MORE EVENTS =====
    const showMoreBtn = document.getElementById('show-more-btn');
    const events = document.querySelectorAll('.event-card');
    let visibleCount = 9;

    events.forEach((event, index) => {
        if (index >= visibleCount) event.style.display = 'none';
    });

    if (showMoreBtn) {
        showMoreBtn.addEventListener('click', () => {
            events.forEach(event => event.style.display = 'flex');
            showMoreBtn.style.display = 'none';
        });
    }
});
