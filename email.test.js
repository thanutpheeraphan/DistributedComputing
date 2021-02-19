const ValidateEmail = require('./email-validation');
var testMail="b@gmail.com"
test('mail', () => {
    expect(ValidateEmail(testMail)).toBe(true);
  })


// test('Check email', () => {
//   document.body.innerHTML = `
//     <input id="textEmail" />
//     <input id="btn"/>
//     <p id="demo" />
//   `;
//   myFunction=require('./email-validation.js');
//   const textEmail = document.getElementById('textEmail');
//   const btn = document.getElementById('btn');
//   const demo=document.getElementById("demo");

//   textEmail.value = "n@mail.com";

//  expect(textEmail.value).toBe("n@mail.com");
//   // expect(demo.innerHTML).toBe("Valid Email ->n@mail.com");


// });