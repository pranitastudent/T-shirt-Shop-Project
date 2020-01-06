//  Recaptcha JS
grecaptcha.ready(function() {
    // 4
    $('#contactform').submit(function(e){
        var form = this;
        // 5
        e.preventDefault()
        grecaptcha.execute('reCAPTCHA_site_key', {action: 'contactform'}).then(function(token) {
            // 6
            $('#recaptcha').val(token)
            // 7
            form.submit()
        });
    })
});