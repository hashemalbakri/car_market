const toggleButton = document.querySelector('.toggle-button')
const navbarLinks = document.querySelector('.links')

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})

