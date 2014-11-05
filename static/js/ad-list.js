// Render List Function
function render_ad_list(data) {
    var ad_list = data.results;

    $("#list").html("");

    var ad_list_template = '<li class="media list-group-item" id="li-ad-{pk}" data-pk={pk}>'+
                              '<a id="ad-anchor-{pk}"</a>' +
                               '<a class="pull-left col-md-2" href="#">'+
                                '<img class="media-object img-thumbnail" width="100%" src="{thumbnail}" alt="post img">'+
                              '</a>'+
                              '<div class="media-body col-md-offset-2">'+
                                '<h3 class="media-heading">{title}</h3>'+
                                '<small> publish: {pub_date} </small>' +
                                '<p class="pull-right">${price}</p> ' +
                                '<p> {short_description} </p>' +
                                '<a class="btn btn-default pull-right"  href="/ad/{pk}"><span class="glyphicon glyphicon-eye-open"></span></a> ' +
                              '</div>'+
                            '</li>';

    var ad_list_paginator = '<span class="step-links">' +
                                '<a id="pag-previous" href="'+ data.previous +'"> << Previous</a>'+
                                '<span class="current" id="pag-inf" > Page {pag_number} of '+ data.count +'. </span>'+
                                '<a id="pag-next" href="' + data.next +'">Next >></a>'+
                            '</span>';

    /*
    ad_list_paginator.replace("{pag_number}", data.next)
    ad_list_paginator.replace("{pages}", data.count)
    ad_list_paginator.replace("{ref-previous}", data.previous);
    ad_list_paginator.replace("{ref-next}", data.next);
    */
    $('#pagination').append(ad_list_paginator);


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
                /* console.log("hover in " + $(this)[0].dataset.pk); */
                ad_position_areas[$(this)[0].dataset.pk].setMap(map);
                ad_position_areas[$(this)[0].dataset.pk].setOptions({strokeWeight: 2.0, fillColor: 'red'});
            },
            function(){
                /*ad_position_areas[$(this)[0].dataset.pk].setMap(null);*/
                ad_position_areas[$(this)[0].dataset.pk].setOptions({strokeWeight: 2.0, fillColor: 'green'});
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
            json_data =  data.results;
            render_ad_list(data);
            clearMapPositions();
            loadPositions(json_data);
        }
    });
}
