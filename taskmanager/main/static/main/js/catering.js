document.addEventListener("DOMContentLoaded", () => {
    const slider = document.querySelector(".services-slider");
    const leftArrow = document.querySelector(".service-arrow.left");
    const rightArrow = document.querySelector(".service-arrow.right");

    const cardWidth = 320 + 20; // ширина карточки + gap

    function updateArrows() {
        const maxScrollLeft = slider.scrollWidth - slider.clientWidth;

        if (slider.scrollLeft <= 0) {
            leftArrow.classList.add("hidden");
        } else {
            leftArrow.classList.remove("hidden");
        }

        if (slider.scrollLeft >= maxScrollLeft - 5) {
            rightArrow.classList.add("hidden");
        } else {
            rightArrow.classList.remove("hidden");
        }
    }

    leftArrow.addEventListener("click", () => {
        slider.scrollBy({ left: -cardWidth, behavior: "smooth" });
    });

    rightArrow.addEventListener("click", () => {
        slider.scrollBy({ left: cardWidth, behavior: "smooth" });
    });

    slider.addEventListener("scroll", updateArrows);

    // Проверяем сразу при загрузке
    updateArrows();
});

document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById("orderModal");
    const closeBtn = modal.querySelector(".close");
    const orderBtns = document.querySelectorAll(".order-btn");
    const serviceInput = document.getElementById("service");

    // Открытие модального окна
    orderBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const serviceTitle = btn.closest(".service-detail").querySelector("h2").textContent;
            serviceInput.value = serviceTitle;
            modal.classList.add("show");
        });
    });

    // Закрытие модального окна
    closeBtn.addEventListener('click', () => {
        modal.classList.remove("show");
    });

    window.addEventListener('click', (e) => {
        if (e.target == modal) {
            modal.classList.remove("show");
        }
    });

    // Отправка формы
    const form = document.getElementById("orderForm");
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        alert(`Ваш заказ на услугу "${serviceInput.value}" отправлен! Скоро с вами свяжется оператор.`);
        form.reset();
        modal.classList.remove("show");
    });
});
