// const ValidateEmail = require('./email-validation');
// var testMail="b@gmail.com"
// test('mail', () => {
//     expect(ValidateEmail(testMail)).toBe(true);
//   })


test('Check email', () => {
  document.body.innerHTML = `
    <input id="textEmail" />
    <input id="submitBtn"/>
    <p id="demo" />
  `;
  require('./email-validation.js');

  const textEmail = document.getElementById('textEmail');
  const submitBtn = document.getElementById('submitBtn');
  const demo=document.getElementById("demo");
  textEmail.value = "n@mail.com";
 // submitBtn. //find how to simulate check
 expect(textEmail.value).toBe("n@mail.com");
  //expect(demo.innerHTML).toBe("Valid Email ->n@mail.com");


});