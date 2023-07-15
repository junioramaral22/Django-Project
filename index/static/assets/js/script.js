
window.addEventListener('load', () => {
    aos_init();
});


function aos_init() {
    AOS.init({
        duration: 1000,
        easing: "ease-in-out",
        once: true,
        mirror: false
    });
}



function openModal() {
    const modal = document.querySelector('#modal');
    modal.style.display = 'block';
}

function closeModal() {
    const modal = document.querySelector('#modal');
    modal.style.display = 'none';
}

