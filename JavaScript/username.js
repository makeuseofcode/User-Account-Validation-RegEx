function checkUsername(user) {
    if(/^[A-Za-z][A-Za-z0-9_]{4,14}$/.test(user)) {
        console.log('Valid');
    } else {
        console.log('Not Valid');
    }
}
checkUsername('yuvraj_chandra');
checkUsername('ja7&^%87'); 