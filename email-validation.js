function ValidateEmail(inputText) {
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if (inputText.match(mailformat)) {
        return true;
    } else {
        return false;
    }
}
module.exports = ValidateEmail;

function myFunction() {
    var email;
    email = document.getElementById("textEmail").value;
    var a =ValidateEmail(email);
    //var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

    if (a == false) {
        document.getElementById("demo").style.color = "red";
        document.getElementById("demo").innerHTML = "Invalid EMail ->" + email;
        alert('Invalid Email Address ->' + email);
        return false;
    } else {
        document.getElementById("demo").style.color = "DarkGreen";
        document.getElementById("demo").innerHTML = "Valid Email ->" + email;

        $textEmail = $('#textEmail').val();
        payload = {
            email: $textEmail
        }

        $.ajax({
            url: "http://0.0.0.0:8080/email",
            //the data to send to
            data: JSON.stringify(payload),
            type: "POST",
            dataType: 'json',
            contentType: 'application/json',
            success: function(data) {
                console.log('Completed!');
            },
            error: function() {
                console.log('Error!');
            }
        });
    }
    return true;
}