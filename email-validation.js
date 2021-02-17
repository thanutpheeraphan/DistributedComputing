function ValidateEmail(inputText) {
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if (inputText.value.match(mailformat)) {
        document.form1.text1.focus();

        return true;
    } else {
        alert("You have entered an invalid email address!");
        document.form1.text1.focus();
        return false;
    }
}

// const button = document.getElementById('post-btn');

// button.addEventListener('click', async _ => {
//     try {
//         const response = await fetch('file:///Users/orn/Desktop/DC/email.html', {
//             method: 'post',
//             body: {
//               text: text1
//             }
//         });
//         console.log('Completed!', response);
//     } catch (err) {
//         console.error(`Error: ${err}`);
//     }
// });