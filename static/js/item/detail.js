// TODO: Im not so sure of this. Check de docs for a proper implementation: http://www.starplugins.com/cloudzoom/quickstart
// TODO: Apply better effects
$(".item-image-gallery").click(function(){ $(".cloud-zoom").data("zoom").destroy();
    $("#main-image").attr("src", $(this).data().image);
    $("#main-image-link").attr("href", $(this).data().image);
    $("#main-image-link").CloudZoom();
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