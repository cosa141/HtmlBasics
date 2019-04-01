var topLeft= document.querySelector('#topLeft')
var bottomLeft= document.querySelector('#bottomLeft')
var middleLeft= document.querySelector('#middleLeft')
var middle= document.querySelector('#middle')
var topMiddle= document.querySelector('#topMiddle')
var bottomMiddle= document.querySelector('#bottomMiddle')
var topRight= document.querySelector('#topRight')
var bottomRight= document.querySelector('#bottomRight')
var middleRight= document.querySelector('#middleRight')

topLeft.addEventListener('click', function() {
  if (topLeft.textContent === '') {
    topLeft.textContent = 'X';
  }else if (topLeft.textContent === 'X') {
    topLeft.textContent = 'O';
  }else {
    topLeft.textContent ='';
  }
})
middleLeft.addEventListener('click', function() {
  if (middleLeft.textContent === '') {
    middleLeft.textContent = 'X';
  }else if (middleLeft.textContent === 'X') {
    middleLeft.textContent = 'O';
  }else {
    middleLeft.textContent ='';
  }
})
bottomLeft.addEventListener('click', function() {
  if (bottomLeft.textContent === '') {
    bottomLeft.textContent = 'X';
  }else if (bottomLeft.textContent === 'X') {
    bottomLeft.textContent = 'O';
  }else {
    bottomLeft.textContent ='';
  }
})
middle.addEventListener('click', function() {
  if (middle.textContent === '') {
    middle.textContent = 'X';
  }else if (middle.textContent === 'X') {
    middle.textContent = 'O';
  }else {
    middle.textContent ='';
  }
})
topMiddle.addEventListener('click', function() {
  if (topMiddle.textContent === '') {
    topMiddle.textContent = 'X';
  }else if (topMiddle.textContent === 'X') {
    topMiddle.textContent = 'O';
  }else {
    topMiddle.textContent ='';
  }
})
bottomMiddle.addEventListener('click', function() {
  if (bottomMiddle.textContent === '') {
    bottomMiddle.textContent = 'X';
  }else if (bottomMiddle.textContent === 'X') {
    bottomMiddle.textContent = 'O';
  }else {
    bottomMiddle.textContent ='';
  }
})
topRight.addEventListener('click', function() {
  if (topRight.textContent === '') {
    topRight.textContent = 'X';
  }else if (topRight.textContent === 'X') {
    topRight.textContent = 'O';
  }else {
    topRight.textContent ='';
  }
})
bottomRight.addEventListener('click', function() {
  if (bottomRight.textContent === '') {
    bottomRight.textContent = 'X';
  }else if (bottomRight.textContent === 'X') {
    bottomRight.textContent = 'O';
  }else {
    bottomRight.textContent ='';
  }
})
middleRight.addEventListener('click', function() {
  if (middleRight.textContent === '') {
    middleRight.textContent = 'X';
  }else if (middleRight.textContent === 'X') {
    middleRight.textContent = 'O';
  }else {
    middleRight.textContent ='';
  }
})

//
//
// topLeft.addEventListener('dblclick', function() {
//   topLeft.textContent= 'O';
// })
// middleLeft.addEventListener('dblclick', function() {
//   middleLeft.textContent= 'O';
// })
// bottomLeft.addEventListener('dblclick', function() {
//   bottomLeft.textContent= 'O';
// })
// middle.addEventListener('dblclick', function() {
//   middle.textContent= 'O';
// })
// topMiddle.addEventListener('dblclick', function() {
//   topMiddle.textContent= 'O';
// })
// bottomMiddle.addEventListener('dblclick', function() {
//   bottomMiddle.textContent= 'O';
// })
// topRight.addEventListener('dblclick', function() {
//   topRight.textContent= 'O';
// })
// bottomRight.addEventListener('dblclick', function() {
//   bottomRight.textContent= 'O';
// })
// middleRight.addEventListener('dblclick', function() {
//   middleRight.textContent= 'O';
// })
