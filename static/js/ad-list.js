// Render List Function
function render_ad_list(ad_list) {
    $("#list").html("");

    var ad_list_template = '<li class="media list-group-item" id="li-ad-{pk}" data-pk={pk}>'+
                              '<a class="pull-left col-md-3" href="#">'+
                                '<img class="media-object img-thumbnail" width="100%" src="{thumbnail}" alt="post img">'+
                              '</a>'+
                              '<div class="media-body col-md-offset-3">'+
                                '<h3 class="media-heading">{title}</h3>'+
                                '<small> publish: {pub_date} </small>' +
                                '<p class="pull-right">${price}</p> ' +
                                '<p> {short_description} </p>' +
                                '<a class="btn btn-default pull-right"  href="/ad/{pk}"><span class="glyphicon glyphicon-eye-open"></span></a> ' +
                              '</div>'+
                            '</li>';


    var ad_list_template2= "<div class='blogShort' id='li-ad-{pk}' data-pk={pk}>"+
                                "<h1></h1>" +
                                "<img src='' alt='post img' class='pull-left img-responsive thumb margin10 img-thumbnail'> " +
                                "<em> Price : $ {price} | Date : {pub_date} | <span class='lat'>{lng}</span> | <span class='lat'>{lat}</span> </em> " +
                                "<article><p>{body}</p></article>" +
                                "<a class='btn btn-blog pull-right marginBottom10' href='/ad/{pk}'>DETAIL</a> " +
                            "</div>";


    for (var i=0; i < ad_list.length; i++) {
        var row = ad_list_template;
        row = row.replace("{title}", ad_list[i].title);
        row = row.replace("{short_description}", ad_list[i].short_description);
        row = row.replace("{thumbnail}", ad_list[i].thumbnail);
        row = row.replace("{lat}", ad_list[i].lat);
        row = row.replace("{lng}", ad_list[i].lng);
        row = row.replace("{price}", ad_list[i].price);
        row = row.replace("{pub_date}", ad_list[i].pub_date);
        row = row.replace(/{pk}/gi, ad_list[i].pk);

        $("#list").append(row);
        $("#li-ad-" + ad_list[i].pk).hover(
            function(){
                console.log("hover in " + $(this)[0].dataset.pk);
                ad_position_areas[$(this)[0].dataset.pk].setMap(map);
            },
            function(){
                ad_position_areas[$(this)[0].dataset.pk].setMap(null);
            })
    }
}
// TODO: Choose proper variable
var temp;
// Search Form
$("#search_btn").click(search);
function search() {
    var tags    = $("#tags").val();
    var lat     = $("#lat").val();
    var lng     = $("#lng").val();
    var radius  = $("#radius").val();
    console.log("click" );
    console.log('tags:' + tags + 'lat:' + lat + 'lng: ' + lng + 'radius: ' + String(radius) );
    temp = {'tags':tags, 'lat':lat, 'radius':radius, 'lng':lng};
    console.log("request data:" + temp);
    $.ajax({
        //data: {'tags':tags, 'lat':lat, 'lng':lng, 'radius':radius},
        data: temp,
        url: "/ad/search/",
        type: "get",
        success: function(data){
            console.log("succcess 66:" + data);
            json_data =  data;
            render_ad_list(data);
            loadPositions(json_data);
        },
    });
}
