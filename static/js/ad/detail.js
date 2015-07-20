// TODO: Im not so sure of this. Check de docs for a proper implementation: http://www.starplugins.com/cloudzoom/quickstart
// TODO: Apply better effects
$(".ad-image-gallery").click(function(){ $(".cloud-zoom").data("zoom").destroy();
    $("#main-image").attr("src", $(this).data().image);
    $("#main-image-link").attr("href", $(this).data().image);
    $("#main-image-link").CloudZoom();
});

// Script to modal contact
$('#btn-contact').click(function(){
    $.get("/message/ajax-can-write/"+ ad.id + "/", function(data){
        console.log(data);
        if(data.message == 'OK'){
            console.log("Entro");
            $.get("/message/ajax-write", function(data){
                $('#modalMessage').html(data);
                $('#submitMessage').click(function() {
                    console.log($('#id_recipient').val());
                    recipient = $('#id_recipient').val();
                    subject = $('#id_subject').val();
                    body = $('#id_body').val();
                    ad_id = ad.id;
                    csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
                    $.post("/api/v1/msgs/", {body: body, subject: subject, object_id: ad_id, content_type: 27, csrfmiddlewaretoken: csrfmiddlewaretoken},
                        function(data) {
                            var content_modal = '<div class="modal-dialog">' +
                                '<div class="modal-content">' +
                                '<div class="modal-header">' +
                                '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>' +
                                '<h4 class="modal-title">Contactar al anunciante</h4>' +
                                '</div>' +
                                '<div class="modal-body">' +
                                '<p> El mensaje fue enviado con exito</p>' +
                                '</div></div></div>';
                            $('#modalMessage').html(content_modal);
                        }
                    ).done(function(){
                        //$('#modalMessage').class = 'modal';
                    });
                });
            });
        }else{
            var content_modal = '<div class="modal-dialog">' +
                '<div class="modal-content">' +
                '<div class="modal-header">' +
                '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>' +
                '<h4 class="modal-title">Contactar al anunciante</h4>' +
                '</div>' +
                '<div class="modal-body">' +
                '<p> El canal de comunicacion se encuentra bloqueado, <a href="#">PAGA </a></p>' +
                '</div></div></div>';
            $('#modalMessage').html(content_modal);
        }
    })
});

// SCRIPT TO SHARE SOCIAL
$('.popup').click(function(event) {
    var width  = 500,
        height = 400,
        left   = ($(window).width()  - width)  / 2,
        top    = ($(window).height() - height) / 2,
        url    = this.href,
        opts   = 'status=1' +
            ',width='  + width  +
            ',height=' + height +
            ',top='    + top    +
            ',left='   + left;
    window.open(url, 'twitter', opts);
    return false;
});


function setImageZoom() {
    var zoom_width;
    if ($(window).width() < 800) {
      // change Image Zoome Attributes
      $("#main-image-link").attr("rel", "adjustY:0, adjustX:0, position:'inside'");
      $('.cloud-zoom, .cloud-zoom-gallery').CloudZoom();
  } else {
      zoom_width = $("#summery-section").width();
      $("#main-image-link").attr("rel", " adjustY:0, adjustX:30, zoomWidth:" + zoom_width);
      $('.cloud-zoom, .cloud-zoom-gallery').CloudZoom();
  }
}

// Make Image Zoom Responsive
$(window).resize(function() {
  // TODO: This should be static, since screen doesn't change dinamically
  setImageZoom();

});
setImageZoom();