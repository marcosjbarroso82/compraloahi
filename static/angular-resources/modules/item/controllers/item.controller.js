/**
 * ItemCtrl
 * @namespace App.item.controllers
 */

(function () {
    'use strict';

    angular
        .module('App.item.controllers')
        .controller('ItemCtrl', ItemCtrl);

    ItemCtrl.$inject = ['$scope', 'ItemSearch', '$location', 'leafletEvents', 'leafletData', '$http']; //

    /**
     * @namespace ItemCtrl
     */
    function ItemCtrl($scope, ItemSearch, $location, leafletEvents, leafletData, $http) {

        var vm = this;

        // Defined vars ------------------------------------------------

        vm.items = []; //List items

        vm.orderings = [{'name': 'price', selected: false}, {'name': 'distance', selected: false}]; // Orderings
        vm.selected_ordering = {};

        vm.search_location = {};
        vm.search_location.changed = false; // Flag to represent
        vm.search_location.radius = 6000; // Custom radius location
        vm.search_location.current_location = {}; // Center current location search location search
        vm.search_location.bounds = {}; // Bounds maps
        vm.search_location.geo_location = {}; // Represent to geo location

        vm.user_locations = [];
        vm.user_location_selected = {};

        vm.page_nro = 1;

        vm.result_count = 0;

        //Var to save location when search on google places
        $scope.location_search_places = {};


        vm.facets = [];
        vm.selected_facets = [];
        vm.selected_facets['changed'] = false;

        vm.map = {
            center: {
                autoDiscover: true, // Request locations by browser
                zoom: 14
            },
            events: {
                markers: {
                    enable: leafletEvents.getAvailableMarkerEvents()
                }
            },
            bounds: {},
            defaults: {
                tileLayer: "http://otile2.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png",
                maxZoom: 14,
                minZoom: 13,
                /*path: {
                 weight: 10,
                 color: '#800000',
                 opacity: 1
                 },*/
                zoomControl: false
            },
            markers: {}
        };

        // Vars to template
        vm.collapsabled = false; // Defined is list items collapse



        // Defined functions ------------------------------------------

        vm.getItemsByPage = getItemsByPage;
        // Functions items list
        vm.centerMap = centerMap;
        vm.selectItem = selectItem;
        vm.deselectItem = deselectItem;

        // Functions facets
        vm.changeFacet = changeFacet;

        vm.refreshResults = refreshResults;

        // User locations
        vm.submitNewLocation = submitNewLocation;

        vm.changeFlagCustomRadius = changeFlagCustomRadius;

        vm.setGeoLocation = setGeoLocation;

        vm.canSaveLocation = canSaveLocation;


        // Initialize Controller
        activate();

        function activate(){
            vm.q = getUrlParameter('q');

            vm.user_locations = user_locations;

            initMap();
        }

        vm.toggleFavorite = function(item){
            // TODO: Validate if authenticated before send toggle favorite
            $http.post('/api/v1/favorites/', {target_object_id: item.id}).success(function(data){
                if (item.is_favorite){
                    item.is_favorite = false;
                }else{
                    item.is_favorite = true;
                }
            }).error(function(error){
                console.log("removeFavorite Error");
            });
        };

        /**
         * Function show/hide radius on map.
         */
        function changeFlagCustomRadius(){
            if(vm.flag_custom_radius){
                vm.map.radius = L.circle([vm.search_location.current_location.lat, vm.search_location.current_location.lng], angular.copy(vm.search_location.radius)).addTo(vm.map.instance);
            }else{
                vm.map.instance.removeLayer(vm.map.radius);
            }
        }

        /**
         * Function to search if exist equals title locations and return boolean
         * @param title
         * @returns {boolean}
         */
        function existsLocationTitle(title) {
            for (var i=0; i < vm.user_locations.length; i++) {
                if (vm.user_locations[i].title === vm.search_location.title) {
                    return true;
                }
            }
            return false;
        }

        /**
         * Function to save new locations
         */
        function submitNewLocation() {
            // TODO: How about validating the others fields?
            if (vm.search_location.title && !existsLocationTitle(vm.search_location.title) ) {
                $.post("/api/v1/user-locations/",
                    {
                        title: vm.search_location.title,
                        lat: vm.search_location.current_location.lat,
                        lng: vm.search_location.current_location.lng,
                        radius: vm.search_location.radius,
                        csrfmiddlewaretoken: csrf
                    },
                    function(data) {
                        vm.user_locations.push({
                            lat: data.lat,
                            lng: data.lng,
                            radius: data.radius,
                            pk: data.id,
                            title: data.title
                        });
                        $('#modalNewLocation').modal('hide');

                        vm.user_location_selected = {};

                        // TODO: this should select the option in the html selct. Bu it's not working
                        $scope.$apply(function(){
                            // TODO: It would be better to use some kind of id
                            $('#user-locations-select option[label="'+ data.title +'"]').attr("selected", "selected");
                        });
                        vm.search_location.changed = false;
                        vm.search_location.title= "";
                    })
                    .fail(function(){
                        $('#modalNewLocation .modal-body').html("Ocurrio un error al guardar su ubicación");
                    });
            } else {
                // TODO: manage this in a better way
                window.alert("Ingrese un nombre que no exista ya");
            }
        }

        var flag_places_changed = false;

        // Event to watch change search location find by google places
        $scope.$watch('location_search_places', function(val, old_val){
            if($scope.location_search_places.geometry){
                vm.search_location.current_location.lat = angular.copy($scope.location_search_places.geometry.location.lat());
                vm.search_location.current_location.lng = angular.copy($scope.location_search_places.geometry.location.lng());

                flag_places_changed = true;
            }
        });

        function addEventUserLocationSelected(){
            // Change select user's locations

            $scope.$watch('vm.user_location_selected',function(val,old){
                if (vm.user_location_selected.lat
                    && vm.user_location_selected.lng
                    && vm.user_location_selected.radius) {

                    vm.search_location.current_location.lat = angular.copy(vm.user_location_selected.lat);
                    vm.search_location.current_location.lng = angular.copy(vm.user_location_selected.lng);
                    vm.search_location.radius = parseInt(angular.copy(vm.user_location_selected.radius));

                    getItemsearch(getUrlParams());
                }
            });
        }

        function addEventSearchLocationChange(){
            // This watch is for range input which returns text instead of number
            $scope.$watch('vm.search_location.radius',function(val,old){
                if(val != old){
                    vm.search_location.radius = parseInt(val);

                    if(vm.flag_custom_radius){
                        vm.map.radius.setRadius(vm.search_location.radius);
                    }

                    if (vm.search_location.radius != vm.user_location_selected.radius
                        && vm.search_location.changed != true) {
                        // TODO: este evento se esta llamando dos veces por problemas de formato de entero y flotante en el radio
                        searchLocationChanged();
                    }
                }
            });

            $scope.$watch('vm.search_location.current_location.lat',function(val,old){
                if(val != old){
                    vm.map.center.lat = angular.copy(vm.search_location.current_location.lat);

                    if(vm.flag_custom_radius){
                        vm.map.radius.setLatLng([vm.search_location.current_location.lat, vm.search_location.current_location.lng]);
                    }
                    if(vm.map.markers['center']){
                        vm.map.markers['center'].lat = angular.copy(vm.search_location.current_location.lat);
                    }

                    if (vm.search_location.current_location.lat != vm.user_location_selected.lat
                        && vm.search_location.changed !=true ) {
                        searchLocationChanged();
                    }
                }
            });
            $scope.$watch('vm.search_location.current_location.lng',function(val,old){
                if(val != old){
                    vm.map.center.lng = angular.copy(vm.search_location.current_location.lng);

                    if(vm.flag_custom_radius){
                        vm.map.radius.setLatLng([vm.search_location.current_location.lat, vm.search_location.current_location.lng]);
                    }

                    if(vm.map.markers['center']){
                        vm.map.markers['center'].lng = angular.copy(vm.search_location.current_location.lng);
                    }

                    if (vm.search_location.current_location.lng != vm.user_location_selected.lng
                        && vm.search_location.changed!=true) {
                        searchLocationChanged();
                    }
                }

            });
        }

        function searchLocationChanged() {
            if (typeof vm.user_location_selected.lat !== vm.search_location.current_location.lat
                && typeof vm.user_location_selected.lng !== vm.search_location.current_location.lng
                && typeof vm.user_location_selected.radius !== vm.search_location.current_location.radius ){
                vm.search_location.changed = true;
                vm.user_location_selected = {};
            }
        }

        /**
         * Function Event, execute when selected (mouse over) item on list.
         * @param item
         */
        function selectItem(item) {
            item.selected = true;
            setMarkerSelected(item);
        }

        /**
         * Function Event, excecute when deselected (mouse outer) item on list.
         * @param item
         */
        function  deselectItem(item) {
            item.selected = false;
            setMarkerSelected(item);
        }

        /**
         * Function Event, execute when click on item. Centered markers belong item selected on map
         * @param position
         */
        function centerMap(position) {
            vm.map.center.lat = angular.copy(position.lat);
            vm.map.center.lng = angular.copy(position.lng);
        }

        /**
         * Function to add event mouse over, mouse out and click on all markers
         */
        function addEvenMarkerssMaps(){
            var markerEvents = leafletEvents.getAvailableMarkerEvents();
            var current_event = ""; //Flag to current markers event on maps
            var current_event_id_item = ""; //Flag to current item id to markers event

            for (var k in markerEvents){
                $scope.$on('leafletDirectiveMarker.mouseout', function(event, args){
                    if(current_event != 'mouseout' && args['modelName'] != 'center'){
                        current_event = 'mouseout';
                        vm.map.markers[args['modelName']]['icon']['markerColor'] = 'red';
                        for(var i=0; i < vm.items.length; i++){
                            if(String(vm.items[i]['id']) == args['modelName']){
                                vm.items[i]['selected'] = false;
                                break;
                            }
                        }
                    }
                });

                $scope.$on('leafletDirectiveMarker.mouseover', function(event, args){
                    if(current_event != 'mouseover' && args['modelName'] != 'center'){
                        current_event = 'mouseover';
                        vm.map.markers[args['modelName']]['icon']['markerColor'] = 'blue';
                        for(var i=0; i < vm.items.length; i++){
                            if(String(vm.items[i]['id']) == args['modelName']){
                                vm.items[i]['selected'] = true;
                                break;
                            }
                        }
                    }
                });

                $scope.$on('leafletDirectiveMarker.click', function(event, args){
                    if(current_event != 'click' && args['modelName'] != 'center'){
                        current_event = 'click';
                        if(current_event_id_item != args['modelName']){
                            current_event_id_item = args['modelName'];
                            var scrollPane = $('#container-items');
                            var offsetTop = 120;
                            var scrollTarget = $("#item-anchor-" + args['modelName']);
                            scrollPane.animate({
                                scrollTop : scrollTarget.offset().top + scrollPane.scrollTop() - parseInt(offsetTop)
                            }, 1200);
                        }
                    }
                });

                /*$scope.$on('leafletDirectiveMarker.drag', function(event, args){
                 if(args['modelName'] == 'center'){
                 console.log("DRAGGGG");
                 }
                 });*/
            }
        }

        /**
         * Set style marker when item selected
         * @param item
         */
        function setMarkerSelected(item){
            if(item.selected){
                vm.map.markers[String(item.id)]['icon']['markerColor'] = 'blue';
            }else{
                vm.map.markers[String(item.id)]['icon']['markerColor'] = 'red';
            }
        }



        /**
         * Create marker to represents items
         */
        function createMarkers(){
            vm.map.markers = {};
            createLocationSearchMarker();

            for(var i=0; i < vm.items.length; i++){
                var marker = vm.items[i]['center'];
                marker['message'] = vm.items[i]['short_description'];
                //marker['layer'] = 'items';
                marker['icon'] = {
                    type: 'awesomeMarker',
                    html: String(i + 1),
                    markerColor: 'red'
                };
                vm.map.markers[String(vm.items[i]['id'])] = marker;
            }
        }

        /**
         * Create marker to represent search location
         */
        function createLocationSearchMarker(){
            vm.map.markers['center'] = {
                lat: angular.copy(vm.search_location.current_location.lat),
                lng: angular.copy(vm.search_location.current_location.lng),
                icon: {
                    iconUrl: '/static/image/map52.svg',
                    shadowUrl: '/static/image/markers-shadow.png',
                    iconSize: [35, 45],  // size of the icon
                    iconAnchor:   [17, 42], // point of the icon which will correspond to marker's location
                    popupAnchor: [1, -32], // point from whtich the popup should open relative to the iconAnchor
                    shadowAnchor: [10, 12], // the same for the shadow
                    shadowSize: [36, 16] // size of the shadow
                }
            };
        }


        function setGeoLocation(){
            vm.search_location.current_location = angular.copy(vm.search_location.geo_location);
            getItemsearch(getUrlParams());
        }



        /**
         * Get instance to map.
         */
        function initMap(){
            leafletData.getMap("searchMap").then(function(map) {
                vm.map.instance = map;

                vm.search_location.current_location = {};

                if(map._initialCenter){
                    vm.search_location.geo_location['lat'] = angular.copy(map._initialCenter.lat);
                    vm.search_location.geo_location['lng'] = angular.copy(map._initialCenter.lng);

                }else{
                    // TODO: Quitar ubicacion por defecto en caso que no tenga acceso a la ubicacion del navegador y
                    // en caso de seleccionar geoLocation volver a preguntar pedir permisos al navegador si aun no lo tiene.
                    vm.search_location.geo_location['lat'] = -31.4179952;
                    vm.search_location.geo_location['lat'] = -64.1890513;
                }

                var bounds = vm.map.instance.getBounds();

                vm.map.bounds['northEast'] = angular.copy(bounds['_northEast']);
                vm.map.bounds['southWest'] = angular.copy(bounds['_southWest']);
                vm.search_location.bounds = angular.copy(vm.map.bounds);

                $scope.$watch('vm.map.bounds', function(new_val, old_val){
                    console.log("MAP BOUNDS");
                    vm.search_location.bounds = angular.copy(vm.map.bounds);
                    vm.search_location.changed_bounds = true;

                    if(flag_places_changed){
                        flag_places_changed = false;
                        refreshResults();
                    }
                    //vm.search_location.changed = true;
                });

                initSearch();
            });
        }



        function canSaveLocation(){
            for(var i=0; i < vm.user_locations.length; i++){
                if(vm.user_locations[i].lat == vm.search_location.current_location.lat &&
                    vm.user_locations[i].lng == vm.search_location.current_location.lng &&
                    vm.user_locations[i].radius == vm.search_location.radius){
                    return false;
                }
            }
            return true;
        }

        function initSearch(){
            var lat = 0;
            var lng = 0;
            var m = 0;

            var sPageURL = window.location.search.substring(1);
            var sURLVariables = sPageURL.split('&');

            var has_param_bounds = 0;
            var has_current_location = 0;

            for (var i = 1; i < sURLVariables.length; i++){
                var sParameterName = sURLVariables[i].split('=');
                switch(sParameterName[0]){
                    case "lat":
                        lat = Number(sParameterName[1]);
                        has_current_location ++;
                        break;
                    case "lng":
                        lng = Number(sParameterName[1]);
                        has_current_location ++;
                        break;
                    case "m":
                        m = Number(sParameterName[1]);
                        has_current_location ++;
                        break;
                    case "q":
                        vm.q = sParameterName[0];
                        break;
                    case "n":
                        vm.map.bounds['northEast']['lat'] = sParameterName[0];
                        has_param_bounds ++;
                        break;
                    case "s":
                        vm.map.bounds['southWest']['lat'] = sParameterName[0];
                        has_param_bounds ++;
                        break;
                    case "e":
                        vm.map.bounds['northEast']['lng'] = sParameterName[0];
                        has_param_bounds ++;
                        break;
                    case "w":
                        vm.map.bounds['southWest']['lng'] = sParameterName[0];
                        has_param_bounds ++;
                        break;
                }
            }

            if(has_param_bounds == 4){

                if(lat != '' && lng != ''){
                    vm.search_location.current_location.lat = angular.copy(lat);
                    vm.search_location.current_location.lng = angular.copy(lng);
                }else{
                    var map_center = vm.map.instance.getCenter();

                    vm.search_location.current_location.lat = angular.copy(map_center.lat);
                    vm.search_location.current_location.lng = angular.copy(map_center.lng);
                }

                getItemsearch(sPageURL.substring(2));
            }else if(has_current_location == 3){
                vm.search_location.current_location.lat = lat;
                vm.search_location.current_location.lng = lng;
                vm.search_location.radius = m;
                getItemsearch(sPageURL.substring(2));
            }else{
                setGeoLocation();
            }

            addEvenMarkerssMaps();
            addEventUserLocationSelected();
            addEventSearchLocationChange();

        }

        /**
         * Search items
         * @param q
         */
        function getItemsearch(q){
            vm.promiseRequestItems =  ItemSearch.search(q).then(getItemSearchSuccess, getItemSearchError);
            function getItemSearchSuccess(data){
                vm.items = data.data.results;

                createMarkers();

                vm.facets = data.data.facets;

                vm.next_page = data.data.next;
                vm.prev_page = data.data.previous;
                vm.page_nro = 1;

                vm.result_count = data.data.count;

                vm.search_location.changed = false;

                // Remplace path by new query path
                $location.search('q='+ q);

            }
            function getItemSearchError(data){
                console.log("Error al traer los mensajes");
            }
        }

        /**
         * Function to get items by page
         * @param nro_page
         */
        function getItemsByPage(nro_page){
            vm.page_nro = nro_page;
            getItemsearch(getUrlParams());
        }

        /**
         * Function to refresh result..
         */
        function refreshResults(){
            if(vm.search_location.changed_bounds && !vm.search_location.changed){
                var map_center = vm.map.instance.getCenter();

                vm.search_location.current_location.lat = angular.copy(map_center.lat);
                vm.search_location.current_location.lng = angular.copy(map_center.lng);
            }

            getItemsearch(getUrlParams());
        }


        /**
         * Function to change status facet
         * @param facet is Object Facet change
         * @param detail is Detail to facet
         * @param value is value to change activated= True, desactivated = false
         */
        function changeFacet(facet, detail, value){
            facet.activated = value;
            detail.activated = value;
            getItemsearch(getUrlParams());
        }

        /**
         * Function to make params url
         * @returns {string}
         */
        function getUrlParams(){
            var url = "";
            if(!vm.flag_custom_radius){
                url = '&n=' + String(vm.search_location.bounds['northEast']['lat']) + '&s=' +
                    String(vm.search_location.bounds['southWest']['lat']) + '&e=' +
                    String(vm.search_location.bounds['northEast']['lng']) + '&w=' +
                    String(vm.search_location.bounds['southWest']['lng']);
            }else{
                url = '&m=' + vm.search_location.radius;
            }

            url += '&lat=' + String(vm.search_location.current_location.lat) +
                '&lng=' + vm.search_location.current_location.lng;

            if(vm.q != '' && vm.q != undefined){
                url += '&q=' + vm.q;
            }

            for(var i=0; i < vm.facets.length; i++){
                if(vm.facets[i].activated){
                    url += '&selected_facets=';
                    for(var iv=0; iv < vm.facets[i].values.length; iv++){
                        if(vm.facets[i].values[iv].activated == true){
                            url += vm.facets[i].name + "_exact:" + vm.facets[i].values[iv].name;
                        }
                    }
                }
            }
            if (vm.selected_ordering && vm.selected_ordering['name']) {
                url += '&order_by=' + vm.selected_ordering['name'];
            }

            if(vm.page_nro > 0){
                url += '&page=' + String(vm.page_nro);
            }

            return url;
        }


        function getUrlParameter(sParam){
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
            return "";
        }

        // Process Current URL to get the selected Facets and Ordering Parameter

        function processCurrentURL() {
            var url = decodeURIComponent(window.location.href);

            // Get Selected Facets
            var facet_re_process = url.match(/(selected_facets=)([^&]+)/gi);
            vm.selected_facets['facets'] = [];
            if (facet_re_process) {
                facet_re_process.forEach(function(element, index, array) {
                    var re = /selected_facets=(.*):(.*)/;
                    var aux = element.match(re);
                    var facet = {};
                    facet['filter'] = aux[1];
                    facet['value'] = aux[2];
                    facet['enabled'] = true;
                    vm.selected_facets['facets'].push(facet);
                });
            }
            // Get Ordering Parameter
            var ordering_process = url.match(/(order_by=)([^&]+)/i);
            if (ordering_process && ordering_process[2]) {
                vm.selected_ordering = vm.orderings.filter(function( obj ) {
                    return obj.name == ordering_process[2];
                })[0];
                vm.selected_ordering.selected = true;
            }
        }
    }
})();