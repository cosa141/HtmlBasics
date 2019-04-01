$('input').eq(0).keypress(function(event) {
  if (event.which === 13) {
    $('h3').toggleClass('turnRed')
  }
})
$('h1').on('dblclick', function() {
  $(this).toggleClass('turnBlue')
})
// $('li').on('mouseenter', function() {
//   $('.container').hide(3000)
// })
// $('body').on('mouseenter', function() {
//   $('body').hide(3000)
// })     //prank 1000
