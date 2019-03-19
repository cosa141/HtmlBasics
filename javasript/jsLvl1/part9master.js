
var comrade = 0;

var firstName = prompt('What is your first name?');

var lastName = prompt('What is your last name?');
if (firstName[0]===lastName[0]) {
  comrade++
}
var age = prompt('What is your Age?');
if (age>20 && age<30) {
  comrade++
}
var height = prompt('What is your height in centimeters?');
if (height>=170) {
  comrade++
}
var pet = prompt('What is your pets name?');
if (pet[pet.length-1]==='y') {
  comrade++
}
alert('Thank you for this information!')
// use the ifs to make comrade reached 4 if all statements are good

if (comrade===4) {
  console.log("Hello there Comrade! You've passed the Spy test!");
}else {
  console.log('Nothing to see here my friend...');
}

///////////////////////////////////////////
//               MADE BY                 //
//  ▄████▄   ▒█████    ██████  ▄▄▄       //
// ▒██▀ ▀█  ▒██▒  ██▒▒██    ▒ ▒████▄     //
// ▒▓█    ▄ ▒██░  ██▒░ ▓██▄   ▒██  ▀█▄   //
// ▒▓▓▄ ▄██▒▒██   ██░  ▒   ██▒░██▄▄▄▄██  //
// ▒ ▓███▀ ░░ ████▓▒░▒██████▒▒ ▓█   ▓██▒ //
// ░ ░▒ ▒  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ //
//   ░  ▒     ░ ▒ ▒░ ░ ░▒  ░ ░  ▒   ▒▒ ░ //
// ░        ░ ░ ░ ▒  ░  ░  ░    ░   ▒    //
// ░ ░          ░ ░        ░        ░  ░ //
// ░               141                   //
///////////////////////////////////////////
