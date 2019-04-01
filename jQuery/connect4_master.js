var playerOne = prompt('Player One: Enter Your Name, you will be Blue');
var playerTwo = prompt('Player Two: Enter Your Name, you will be Red');
var playerOneColor = 'rgb(249, 4, 21)';
var playerTwoColor = 'rgb(3, 101, 249)';

var game_on = true;
var table = $('table tr');

function reportWin(rowNum, colNum) {
  console.log(rowNum);
  console.log(colNum);
}
function changeColor(rowIndex, colIndex, color) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}
























// function playing() {
//   var playerOne = prompt('Player One: Enter Your Name, you will be Blue')
//   var playerTwo = prompt('Player Two: Enter Your Name, you will be Red')
//   if (playerOne != null){
//     txt=playerOne+': its your turn'
//     document.getElementsById("#poo")=txt
//   }
// }
// playing()
//
// $('h3').text(playerOne+": it is your turn, please pick a column to drop your blue chip.");
