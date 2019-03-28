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
  topLeft.textContent= 'X';
})
middleLeft.addEventListener('click', function() {
  middleLeft.textContent= 'X';
})
bottomLeft.addEventListener('click', function() {
  bottomLeft.textContent= 'X';
})
middle.addEventListener('click', function() {
  middle.textContent= 'X';
})
topMiddle.addEventListener('click', function() {
  topMiddle.textContent= 'X';
})
bottomMiddle.addEventListener('click', function() {
  bottomMiddle.textContent= 'X';
})
topRight.addEventListener('click', function() {
  topRight.textContent= 'X';
})
bottomRight.addEventListener('click', function() {
  bottomRight.textContent= 'X';
})
middleRight.addEventListener('click', function() {
  middleRight.textContent= 'X';
})



topLeft.addEventListener('dblclick', function() {
  topLeft.textContent= 'O';
})
middleLeft.addEventListener('dblclick', function() {
  middleLeft.textContent= 'O';
})
bottomLeft.addEventListener('dblclick', function() {
  bottomLeft.textContent= 'O';
})
middle.addEventListener('dblclick', function() {
  middle.textContent= 'O';
})
topMiddle.addEventListener('dblclick', function() {
  topMiddle.textContent= 'O';
})
bottomMiddle.addEventListener('dblclick', function() {
  bottomMiddle.textContent= 'O';
})
topRight.addEventListener('dblclick', function() {
  topRight.textContent= 'O';
})
bottomRight.addEventListener('dblclick', function() {
  bottomRight.textContent= 'O';
})
middleRight.addEventListener('dblclick', function() {
  middleRight.textContent= 'O';
})
