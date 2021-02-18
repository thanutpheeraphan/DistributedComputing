const ValidateEmail = require('./email-validation');
var testMail="b@gmail.com"
test('mail', () => {
    expect(ValidateEmail(testMail)).toBe(true);
  })