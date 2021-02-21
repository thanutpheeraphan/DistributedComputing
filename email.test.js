const ValidateEmail = require('./email-validation');
var testMail="baba"
test('mail', () => {
    expect(ValidateEmail(testMail)).toBe(true);
  })


