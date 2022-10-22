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


consoleText(['EXPLORE CARS FOR SALE'], 'text',['black']);

function consoleText(words, id, colors) {
  if (colors === undefined) colors = ['#fff'];
  var letterCount = 1;
  var x = 1;
  var waiting = false;
  var target = document.getElementById(id)
  target.setAttribute('style', 'color:' + colors[0])
  window.setInterval(function() {
    if (letterCount === 0 && waiting === false) {
      waiting = true;
      target.innerHTML = words[0].substring(0, letterCount)
      window.setTimeout(function() {
        x = 1;
        target.setAttribute('style', 'color:' + colors[0])
        letterCount += x;
        waiting = false;
      }, 600)
    } else if (waiting === false) {
      target.innerHTML = words[0].substring(0, letterCount)
      letterCount += x;
    }
  }, 120)
  
}
  

})


