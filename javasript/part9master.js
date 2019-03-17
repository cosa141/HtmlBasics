
var comrade = 0;

var firstName = prompt('What is your first name?');

var lastName = prompt('What is your last name?');
if (firstName[0]===lastName[0]) {
  comrade+=2
}
var age = prompt('What is your Age?');
if (age>20 && age<30) {
  comrade++
}
var height = prompt('What is your height in centimeters?');
if (height>170) {
  comrade++
}
var pet = prompt('What is your pets name?');
if (pet[-1]=='y') {
  comrade++
}
// use the ifs to make comrade reach 5 if all statements are good

if (comrade==4) {
  console.log('Hello there Comrade! Welcome');
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
