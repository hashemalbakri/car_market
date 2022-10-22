document.addEventListener('DOMContentLoaded', function(){
    const toggleButton = document.querySelector('.toggle-button')
const navbarLinks = document.querySelector('.links')

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})


let images = document.querySelectorAll('.clickable_image')

for (let index = 0; index < images.length; index++) {
    images[index].addEventListener('click', function(){
        console.log(document.querySelector('#pic-1'))
        document.querySelector('#pic-1').querySelector('img').src = images[index].querySelector('img').src
    });
    
}



})


