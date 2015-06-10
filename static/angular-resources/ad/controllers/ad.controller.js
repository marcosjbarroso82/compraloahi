/**
 * AdCtrl
 * @namespace App.ad.controllers
 */

(function () {
    'use strict';

    angular
        .module('App.ad.controllers')
        .controller('AdCtrl', AdCtrl);

    AdCtrl.$inject = ['$scope', 'Ad', 'AdSearch', '$location'];

    /**
     * @namespace AdCtrl
     */
    function AdCtrl($scope, Ad, AdSearch, $location) {
        $scope.ads = {};

        $scope.orderings = [{'name': 'price', selected: false}, {'name': 'distance', selected: false}];
        $scope.selected_ordering = {};

        $scope.facets = {};
        $scope.selected_facets = [];
        //$scope.selected_facets['facets'] = selected_facets;
        $scope.selected_facets['changed'] = false;

        $scope.search_location = search_location;
        $scope.search_location.changed = false;
        $scope.search_location.stroke = {color: '#1e617d', weight: 1, opacity: 0.4 };
        $scope.search_location.fill = {color: '#ececec', weight: 2, opacity: 0.08 };

        $scope.user_locations = user_locations;
        $scope.user_location_selected = {};

        $scope.collapsabled = false;

        $scope.page_nro = 1;

        //Var to save location when search on google places
        $scope.location_search_places = {};


        //var cache_history = [];

        // Initialize Controller
        activate();



        function activate(){
            //Get ads init
            $scope.q = getUrlParameter('q');
            getAdsearch(getUrlParams());

        }

        function getUrlParameter(sParam)
        {
            var sPageURL = window.location.search.substring(1);
            var sURLVariables = sPageURL.split('&');
            for (var i = 0; i < sURLVariables.length; i++)
            {
                var sParameterName = sURLVariables[i].split('=');
                if (sParameterName[0] == sParam)
                {
                    return sParameterName[1];
                }
            }
        }

// ############ SAVE LOCATION ##############
        $scope.existsLocationTitle = function (title) {
            for (var i=0; i < $scope.user_locations.length; i++) {
                if ($scope.user_locations[i].title === $scope.search_location.title) {
                    return true;
                }
            }
            return false;
        }

        $scope.submitNewLocation= function () {
            // TODO: How about validating the others fields?
            if ($scope.search_location.title && !$scope.existsLocationTitle($scope.search_location.title) ) {
                $.post("/api/v1/user-locations/",
                    {
                        title: $scope.search_location.title,
                        lat: $scope.search_location.location.latitude,
                        lng: $scope.search_location.location.longitude,
                        radius: $scope.search_location.radius,
                        csrfmiddlewaretoken: csrf
                    },
                    function(data) {
                        $scope.user_locations.push({
                            latitude: data.lat,
                            longitude: data.lng,
                            radius: data.radius,
                            pk: data.id,
                            title: data.title
                        });
                        $('#modalNewLocation').modal('hide');

                        $scope.user_location_selected = {};

                        // TODO: this should select the option in the html selct. Bu it's not working
                        $scope.$apply(function(){
                            // TODO: It would be better to use some kind of id
                            $('#user-locations-select option[label="'+ data.title +'"]').attr("selected", "selected");
                        });

                        $scope.search_location.changed = false;
                        $scope.search_location.title= "";
                        $("#search_location_name").val("");
                    })
                    .fail(function(){
                        $('#modalNewLocation .modal-body').html("Ocurrio un error al guardar su ubicación");
                    });
            } else {
                // TODO: manage this in a better way
                window.alert("Ingrese un nombre que no exista ya");
            }
        }
// ############ END SAVE LOCATION ##############


// ################## MAP ################################

        // Event to watch change search location find by google places
         $scope.$watch('location_search_places', function(val, old_val){
           if($scope.location_search_places.geometry){
               $scope.search_location.location.latitude = angular.copy($scope.location_search_places.geometry.location.lat());
               $scope.search_location.location.longitude = angular.copy($scope.location_search_places.geometry.location.lng());
               $scope.search_location.title = angular.copy($scope.location_search_places.formatted_address);
               $scope.search_location.location.center = {};
               $scope.search_location.location.center.latitude = angular.copy($scope.location_search_places.geometry.location.lat());
               $scope.search_location.location.center.longitude = angular.copy($scope.location_search_places.geometry.location.lng());
               $scope.search_location.changed = false;

           }
        });

        // Change select user's locations
        $scope.$watch('user_location_selected',function(val,old){
            //  this IF makes sure the code is no executed right when its loaded
            if ($scope.user_location_selected.latitude
                && $scope.user_location_selected.longitude
                && $scope.user_location_selected.radius) {

                $scope.search_location.location.latitude = $scope.user_location_selected.latitude;
                $scope.search_location.location.longitude = $scope.user_location_selected.longitude;
                $scope.search_location.radius = $scope.user_location_selected.radius;
                $scope.search_location.changed = false;

                getAdsearch(getUrlParams());
            }
        });

        // This watch is for range input which returns text instead of number
        $scope.$watch('search_location.radius',function(val,old){
            $scope.search_location.radius = parseInt(val);
            if ($scope.search_location.radius != $scope.user_location_selected.radius
                && $scope.search_location.changed != true) {
                // TODO: este evento se esta llamando dos veces por problemas de formato de entero y flotante en el radio
                searchLocationChanged();
            }
        });

        $scope.$watch('search_location.location.latitude',function(val,old){
            if ($scope.search_location.location.latitude != $scope.user_location_selected.latitude
                && $scope.search_location.changed!=true) {
                searchLocationChanged();
            }
        });
        $scope.$watch('search_location.location.longitude',function(val,old){
            if ($scope.search_location.location.longitude != $scope.user_location_selected.longitude
                && $scope.search_location.changed!=true) {
                searchLocationChanged();
            }
        });

        function searchLocationChanged() {
            if (typeof $scope.user_location_selected.latitude !== search_location.location.latitude
                && typeof $scope.user_location_selected.longitude !== search_location.location.longitude
                && typeof $scope.user_location_selected.radius !== search_location.location.radius ){
                $scope.search_location.changed = true;
                $scope.user_location_selected = {};
            }
        }

        $scope.map = {
            // TODO: define a proper location initialization
            center: {
                latitude: -31.4179952,
                longitude: -64.1890513
            },
            zoom: 13,
            options: {},
            control: {},
            circle_events: {
                click: function (marker, eventName, args) {
                    $('html, body').animate({
                        scrollTop: $("#ad-anchor-" + args.$parent.ad.id).offset().top - 70
                    }, 1000);
                },
                mouseover: function (marker, eventName, args) {
                    args.$parent.ad.selected = true;
                },
                mouseout: function (marker, eventName, args) {
                    args.$parent.ad.selected = false;
                }
            }
        };

        $scope.location_options = {
            draggable: false, // optional: defaults to false
            clickable: true, // optional: defaults to true
            editable: false, // optional: defaults to false
            visible: true // optional: defaults to true
        }

        // Define circle map event, when click on circle event vertical aling ad.
        $scope.circle_events = {
            click: function (marker, eventName, args) {
                var container = $("#container-ad-list");
                var item = $("#ad-anchor-" + args.$parent.ad.id);
                $('html, body, #container-ad-list').animate({
                    scrollTop: item.offset().top - container.offset().top + container.scrollTop() - 70
                }, 1000);

            },
            mouseover: function (marker, eventName, args) {
                args.$parent.ad.selected = true;
            },
            mouseout: function (marker, eventName, args) {
                args.$parent.ad.selected = false;
            }
        };

        /**
         * Define style to ad on map
         * @param ad
         */
        function setCircleStyle(ad){
            if (ad.selected) {
                ad.stroke = {color: '#1e617d', weight: 0, opacity: 0.9 };
                ad.fill = {color: '#1e617d', weight: 2, opacity: 0.9 };
            } else {
                ad.stroke = {color: '#ff6600', weight: 0, opacity:0.6 };
                ad.fill = {color: '#ff6600', weight: 2, opacity: 0.6 };
            }
        }
// ################## END MAP ################################




// ######## LIST ADS ##########

         // Function to center on location ad.
        $scope.centerMap = function(position) {
            $scope.map.control.getGMap().panTo(new google.maps.LatLng(position.latitude, position.longitude));
        }

        $scope.selectAd = function (ad) {
            ad.selected = true;
            setCircleStyle(ad);
        }

        $scope.deselectAd = function (ad) {
            ad.selected = false;
            setCircleStyle(ad);
        }

        function getAdsearch(q){
            $scope.adPromise = AdSearch.search(q).then(getAdSearchSuccess, getAdSearchError);

            function getAdSearchSuccess(data){
                $scope.ads = data.data.results;
                $scope.facets = data.data.facets;
                $scope.next_page = data.data.next;
                $scope.prev_page = data.data.previous;
                $scope.page_nro = 1;

                // Remplace path by new query path
                $location.search('q='+ q);
                //$location.replace();

                // set Circle style for each ad
                $.each($scope.ads,function(index, ad){
                    setCircleStyle(ad);
                });
            }
            function getAdSearchError(data){
                console.log("Error al traer los mensajes");
            }
        }

        $scope.get_ads_page = function(nro_page){
            $scope.page_nro = nro_page;
            getAdsearch(getUrlParams());
        }
// ######## END LIST ADS ##########



// ######## FACETS ##########

        /**
         * Function to change status facet
         * @param facet is Object Facet change
         * @param detail is Detail to facet
         * @param value is value to change activated= True, desactivated = false
         */
        $scope.changeFacet = function(facet, detail, value){
            facet.activated = value;
            detail.activated = value;
            getAdsearch(getUrlParams());
        }


        $scope.refreshResults = function(){
            getAdsearch(getUrlParams());
        };

// ######## END FACETS ##########



        /**
         * Function to make params url
         * @returns {string}
         */
        function getUrlParams(){
            var url = '&km=' + $scope.search_location.radius +
                '&lat=' + String($scope.search_location.location.latitude) +
                '&lng=' + $scope.search_location.location.longitude;

            if($scope.q != '' && $scope.q != undefined){
                url += '&q=' + $scope.q;
            }

            for(var i=0; i < $scope.facets.length; i++){
                if($scope.facets[i].activated){
                    url += '&selected_facets=';
                    for(var iv=0; iv < $scope.facets[i].values.length; iv++){
                        if($scope.facets[i].values[iv].activated == true){
                            url += $scope.facets[i].name + "_exact:" + $scope.facets[i].values[iv].name;
                        }
                    }
                }
            }
            if ($scope.selected_ordering && $scope.selected_ordering['name']) {
                url += '&order_by=' + $scope.selected_ordering['name'];
            }

            if($scope.page_nro > 0){
                url += '&page=' + String($scope.page_nro);
            }

            return url;
        }


 /**
         * Function to change location, selecting user location
         * @param location

        $scope.change_select_location = function(location){
            $scope.user_location_selected = location;
        }*/


        // Process Current URL to get the selected Facets and Ordering Parameter

        function processCurrentURL() {
            var url = decodeURIComponent(window.location.href);

            // Get Selected Facets
            var facet_re_process = url.match(/(selected_facets=)([^&]+)/gi);
            $scope.selected_facets['facets'] = [];
            if (facet_re_process) {
                facet_re_process.forEach(function(element, index, array) {
                    var re = /selected_facets=(.*):(.*)/;
                    var aux = element.match(re);
                    var facet = {};
                    facet['filter'] = aux[1];
                    facet['value'] = aux[2];
                    facet['enabled'] = true;
                    $scope.selected_facets['facets'].push(facet);
                });
            }
            // Get Ordering Parameter
            var ordering_process = url.match(/(order_by=)([^&]+)/i);
            if (ordering_process && ordering_process[2]) {
                $scope.selected_ordering = $scope.orderings.filter(function( obj ) {
                    return obj.name == ordering_process[2];
                })[0];
                $scope.selected_ordering.selected = true;
            }
        }


        //processCurrentURL();
    }
})();