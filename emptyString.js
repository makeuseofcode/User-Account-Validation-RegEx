function checkEmptyString(str) {
    if(/^$/.test(str)) {
        console.log('The given string is empty');
    } else {
        console.log('The given string is not empty');
    }
}
checkEmptyString('');
checkEmptyString('This is not an empty string'); 