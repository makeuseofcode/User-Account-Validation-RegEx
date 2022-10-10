function checkDateFormat(date) {
    if(/^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$/.test(date)) {
        console.log('Valid');
    } else {
        console.log('Not Valid');
    }
}
checkDateFormat('03/21/2002');
checkDateFormat('15/21/2002'); 