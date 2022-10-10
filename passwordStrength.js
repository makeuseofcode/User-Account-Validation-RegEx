function checkPasswordStrength(password) {
    if(/(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})/.test(password)) {
        console.log('Strong Password');
    } else {
        console.log('Weak Password');
    }
}
checkPasswordStrength('Hiuahd$5jawd');
checkPasswordStrength('my_password'); 