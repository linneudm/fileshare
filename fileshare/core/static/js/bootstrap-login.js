function showPassword() {
    
    var key_attr = $('#id_password').attr('type');
    
    if(key_attr != 'text') {
        
        $('.checkbox').addClass('show');
        $('#id_password').attr('type', 'text');
        
    } else {
        
        $('.checkbox').removeClass('show');
        $('#id_password').attr('type', 'password');
        
    }
    
}