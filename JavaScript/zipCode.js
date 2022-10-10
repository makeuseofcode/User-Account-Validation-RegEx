function validateZIPCode(code) {
    if(/^[0-9]{5}(?:-[0-9]{4})?$/.test(code)) {
        console.log('Valid');
    } else {
        console.log('Not Valid');
    }
}
validateZIPCode('76309');
validateZIPCode('83468-2348'); 
validateZIPCode('234445'); 