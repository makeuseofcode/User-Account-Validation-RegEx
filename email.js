function checkEmailId(email) {
    if(/^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
        console.log('Valid');
    } else {
        console.log('Not Valid');
    }
}
checkEmailId('abc@gmail.com');
checkEmailId('abc@def@gmail.kahscg'); 