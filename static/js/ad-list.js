// Render List Function
function render_ad_list(ad_list) {
    $("#list").html("");
    var ad_list_template = "<li>" +
            "<time datetime='2014-07-20'><span class='day'>10</span>"+
                "<span class='month'>11</span>"+
                "<span class='year'>2014</span>"+
                "<span class='time'>ALL DAY</span>"+
            "</time>"+
                    "<img src='{thumbnail}' width='100' height='100'>"+
            "<div class='info'>"+
                "<h2 class='title'>{title}</h2>"+
                "<ul>"+
                    "<li style='width:50%;'><a href='#'><span class='fa fa-fw fa-eye'></span> Show</a></li>"+
                    "<li style='width:50%;'><span class='fa fa-money'></span> $39.99</li>"+
                "</ul>"+
            "</div>"+
            "<div class='social'>"+
                "<ul>"+
                    "<li class='facebook' style='width:33%;'><a href='#facebook'><span class='fa fa-facebook'></span></a></li>"+
                    "<li class='twitter' style='width:34%;'><a href='#twitter'><span class='fa fa-twitter'></span></a></li>"+
                    "<li class='google-plus' style='width:33%;'><a href='#google-plus'><span class='fa fa-google-plus'></span></a></li>"+
                "</ul>"+
            "</div>"+
        "</li>"+
    "<hr>";
    for (var i=0; i < ad_list.length; i++) {
        var row = ad_list_template;
        row = row.replace("{title}", ad_list[i].title);
        row = row.replace("{body}", ad_list[i].body);
        row = row.replace("{thumbnail}", ad_list[i].thumbnail);
        $("#list").append(row);
    }
}
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
    $.ajax({
        //data: {'tags':tags, 'lat':lat, 'lng':lng, 'radius':radius},
        data: temp,
        url: "/ad/search/",
        type: "get",
        success: render_ad_list,
    });
}
