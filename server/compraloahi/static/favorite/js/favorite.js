$(document).ready(function() {


    $('.btn-favit-favorite').click(function() {
        var $obj = $(this);
        var target_id = $obj.attr('id').split('_')[1];
        $obj.prop('disabled', true);
        var has_count = $obj.attr('count');
        $.ajax({
            url: $obj.attr('href'),
            type: 'POST',
            beforeSend: function(xhr, settings){
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            },
            data: {
                target_model: $obj.attr('model'),
                target_object_id: target_id
            },
            success: function(response) {
                if (response.status == 'added') {
                    $obj.children().removeClass('fa-heart-o').addClass('fa-heart');
                    toastr.success('Se ah agregado el aviso a favoritos.');
                }
                else {
                    $obj.children().removeClass('fa-heart').addClass('fa-heart-o');
                    toastr.info('Se ah quitado el aviso de favoritos.');
                }
                if(has_count == 'True'){
                    $obj.parent('.favit').children('.fav-count').text(response.fav_count);
                    $obj.prop('disabled', false);
                }
            }
        });
    });

    $('.btn-favit-unfave').click(function() {
        var $obj = $(this);
        $obj.prop('disabled', true);
        $.ajax({
            url: $obj.attr('href'),
            type: 'POST',
            data: {
                target_model: $obj.data('model'),
                target_object_id: $obj.data('id')
            },
            beforeSend: function(xhr, settings){
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            },
            success: function(response) {
                if (response.status == 'deleted') {
                    $obj.parent().parent().remove();
                }
            },
            complete: function(response) {
                $obj.prop('disabled', false);
            }
        });
    });
});
