// ################################## SUPPORT TO REQUEST AJAX WITH CSRF ON COOKIES ############################ //

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



$(document).ready(function() {
  $('.btn.favorite').click(function() {
      var $obj = $(this);
      var target_id = $obj.attr('id').split('_')[1];
      $obj.prop('disabled', true);
      $.ajax({
      url: $obj.attr('href'),
      type: 'POST',
      data: {target_model: $obj.attr('model'),
             target_object_id: target_id},
      success: function(response) {
          if (response.status == 'added') {
            $obj.children().removeClass('glyphicon-heart-empty').addClass('glyphicon-heart');}
          else {
            $obj.children().removeClass('glyphicon-heart').addClass('glyphicon-heart-empty');
          }
          $obj.parent('.favit').children('.fav-count').text(response.fav_count);
          $obj.prop('disabled', false);
      }
      });
  });

  $('.btn.unfave').click(function() {
    var $obj = $(this);
    $obj.prop('disabled', true);
    $.ajax({
      url: $obj.attr('href'),
      type: 'POST',
      data: {
        target_model: $obj.data('model'),
        target_object_id: $obj.data('id')
      },
      success: function(response) {
        if (response.status == 'deleted') {
          $obj.parent().remove();
        }
      },
      complete: function(response) {
        $obj.prop('disabled', false);
      }
    });
  });
});