/**
 * ItemCtrl
 * @namespace appSearch.item.controllers
 */

(function () {
    'use strict';

    angular
        .module('appSearch.item.controllers')
        .controller('ItemCtrl', ItemCtrl);

    ItemCtrl.$inject = ['$scope', 'ItemSearch', '$location', 'leafletEvents', 'leafletData', '$http', 'AlertNotification', 'ngDialog']; //

    /**
     * @namespace ItemCtrl
     */
    function ItemCtrl($scope, ItemSearch, $location, leafletEvents, leafletData, $http, AlertNotification, ngDialog) {
        var vm = this;

        // Defined vars ------------------------------------------------
        vm.items = []; //List items
        vm.orderings = [{'name': 'price', selected: false}]; // {'name': 'distance', selected: false}]; // Orderings
        var current_location = {}; // representa la posicion del usuario en el mapa
        var current_location_geo = {}; // representa la posicion obtenida por geo localizacion

        vm.selected_ordering = '';

        // Default value to params search.
        var params_search = {};

        vm.items = [];
        vm.facets = [];
        vm.item_count = 0;
        var page_nro = 0;
        vm.page_next = null;
        vm.page_previous = null;

        // map instance params
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
                tileLayer: 'http://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}',
                maxZoom: 15,
                minZoom: 12,
                zoomControl: false,
                tap: true
            },
            markers: {}
        };

        // Var to save result when select google place
        $scope.location_search_places = {};

        // User list location
        vm.user_locations = [];

        vm.refresh_result_on_move = true; // Bandera que indica si se actualizan los resultados cuando se mueve el mapa

        init();

        // Define el tipo de ubicacion que se usa para buscar por el momento hay dos tipos (point, bounds)
        var type_location_search = 'bounds';

        vm.flag_custom_radius = false;


        /**
         * Function initializate
         */
        function init(){
            vm.user_locations = user_locations;
            params_search = angular.copy($location.search());
            initMap();
        }

        var flag_count_dragend = 0; // Bandera para chequear cuando cambia la posicion desde el mapa
        var flag_count_dragend_compare = 0; // Bandera para chequear cuando cambia la posicion desde el mapa

        /**
         * Get instance to map.
         */
        function initMap(){
            leafletData.getMap("searchMap").then(function(map) {
                vm.map.instance = map;
                initSearch();

                $scope.$on('leafletDirectiveMap.drag', function(event, args){

                    if(vm.refresh_result_on_move){
                        flag_count_dragend ++;
                        setTimeout(function () {
                            flag_count_dragend_compare ++;
                            if(flag_count_dragend == flag_count_dragend_compare){
                                if(!vm.flag_custom_radius){
                                    set_params_bounds_to_map(true);
                                }else{
                                    if(args['modelName'] == 'user_current_location'){
                                        getItemsearch(get_query(1));
                                    }
                                }
                            }
                        }, 1000);
                    }
                });
                addEvenMarkerssMaps();
                addEventUserLocationSelected();
            });
        }

        function initSearch(){
            if(check_params(['selected_facets'])){
                vm.facets = [];
                var params_facets = params_search.selected_facets.split(',');
                angular.forEach(params_facets, function(param_facet) {
                    var facet = param_facet.split(":")[0];
                    var value = param_facet.split(":")[1];
                    var facet_name = facet.split("_")[0];
                    vm.facets.push({
                        "activated": true,
                        "name": facet_name,
                        "values": [ { "name": value,"activated": true} ]
                    });
                });
            }
            if(check_params(['order_by'])){
                angular.forEach(vm.orderings, function(order){
                    if(params_search.order_by == order.name){
                        vm.selected_ordering = angular.copy(order);
                    }
                })
            }

            if(check_params(['n', 's', 'e', 'w'])){
                changeTypeLocationSearch('bounds');

                var bounds = get_bounds_to_params();
                vm.map.bounds = angular.copy(bounds);
                setTimeout(function () {
                    changeCurrentLocation(vm.map.center, false);
                }, 500);
                getItemsearch($location.search());
            }else if(check_params(['lat', 'lng', 'm'])){

                setTimeout(function () {
                    vm.flag_custom_radius = true;
                    changeCurrentLocation(params_search, true);
                    toggleRangeSearch(params_search['m']);
                }, 500);

            }else{
                get_geo_location();
            }
        }

        $scope.$watch('location_search_places', function(val, old_val){
            if($scope.location_search_places.geometry){
                var location = {};
                location['lat'] = angular.copy($scope.location_search_places.geometry.location.lat());
                location['lng'] = angular.copy($scope.location_search_places.geometry.location.lng());
                if(type_location_search == 'point'){
                    changeCurrentLocation(location, true);
                }else{
                    vm.centerMap(location);
                    changeCurrentLocation(location, false);
                    setTimeout(function () {
                        set_params_bounds_to_map(true);
                    }, 500);
                }
            }
        });

        vm.changeFacet = function(facet, value, bool){
            facet.activated = bool;
            value.activated = bool;
            getItemsearch(get_query());
        };

        vm.selectItem = function(item){
            item.selected = true;
            setMarkerSelected(item);
        };

        vm.deselectItem = function(item){
            item.selected = false;
            setMarkerSelected(item);
        };

        vm.toggleFavorite = function(item){
            $http.post('/api/v1/favorites/', {target_object_id: item.id}).success(function(data){
                if (item.is_favorite){
                    item.is_favorite = false;
                    AlertNotification.error("Se quito de favoritos : " + item.title);
                }else{
                    item.is_favorite = true;
                    AlertNotification.success("Se agrego a favoritos : " + item.title);
                }
            }).error(function(error){
                AlertNotification.error("Error al intentar quitar de favoritos al aviso : " + item.title + " vuelva a intentarlo mas tarde");
            });
        };

        vm.centerMap = function(position){
            vm.map.center.lat = angular.copy(position.lat);
            vm.map.center.lng = angular.copy(position.lng);
        };

        vm.setGeoLocation = function(){
            get_geo_location();
        };

        function changeCurrentLocation(loc, commit){
            var lat = parseFloat(loc.lat);
            var lng = parseFloat(loc.lng);
            params_search.lat = angular.copy(lat);
            params_search.lng = angular.copy(lng);

            current_location.lat = angular.copy(lat);
            current_location.lng = angular.copy(lng);

            vm.map.center.lat = angular.copy(lat);
            vm.map.center.lng = angular.copy(lng);

            if(vm.map.markers['user_current_location']){
                vm.map.markers['user_current_location']['lat'] = angular.copy(lat);
                vm.map.markers['user_current_location']['lng'] = angular.copy(lng);
            }

            if(vm.flag_custom_radius && vm.map.radius){
                changeSearchRadiusPosition(lat, lng);
            }
            if(commit){
                changeTypeLocationSearch('point');
                getItemsearch(get_query(1));
            }
        }

        function get_geo_location(){
            // Si existe una posicion guardada...
            if(current_location_geo.lat && current_location_geo.lng){
                changeCurrentLocation(current_location_geo, true);
            }else{
                ngDialog.openConfirm({
                    className: 'ngdialog-theme-plain',
                    template: '<div class="dialog-contents">\
                            <p><i class="fa fa-question-circle"> </i> ¿Desea utilizar su ubicacion?</p>\
                            <div class="ngdialog-buttons">\
                                <button type="button" class="ngdialog-button ngdialog-button-secondary" ng-click="closeThisDialog(0)">CANCEL</button>\
                                <button type="button" class="ngdialog-button ngdialog-button-primary" ng-click="confirm(1)">OK</button>\
                            </div> </div>',
                    plain: true
                }).then(function (data) {
                    if (navigator.geolocation) {
                        navigator.geolocation.getCurrentPosition(function(position){
                            current_location_geo.lat = position.coords.latitude;
                            current_location_geo.lng = position.coords.longitude;
                            changeCurrentLocation({'lat': position.coords.latitude, 'lng': position.coords.longitude}, false);

                            if(!vm.flag_custom_radius){
                                set_params_bounds_to_map(true);
                            }
                        }, function(){
                            AlertNotification.error("Error al intentar recuperar su ubicacion, vuelva a intentarlo, asegurese de tener habilitada la opcion de compartir su ubicacion");
                        });
                    } else {
                        // TODO: Set to a proper Location
                        AlertNotification.info("Su navegador no tiene soporte  o no tiene activado la funcionalidad de geo localizacion");
                    }
                });
            }
        }

        var flag_change_range = 0;
        var flag_change_range_compare = 0;

        vm.changeRangeSearch = function(range){
            flag_change_range ++;

            vm.map.radius.setRadius(angular.copy(range));

            params_search.m = angular.copy(range);
            setTimeout(function () {
                flag_change_range_compare ++;
                if(flag_change_range == flag_change_range_compare){
                    changeTypeLocationSearch('point');
                    getItemsearch(get_query(1));
                }
            }, 1000);
        };

        function changeSearchRadiusPosition(lat, lng){
            vm.map.radius.setLatLng([ angular.copy(lat), angular.copy(lng)]);
        }

        vm.changeFlagCustomRadius = toggleRangeSearch;

        function toggleRangeSearch(range){
            $scope.radius = angular.copy(range);
            if(vm.flag_custom_radius){
                changeTypeLocationSearch('point');
                vm.map.radius = L.circle([angular.copy(current_location.lat), angular.copy(current_location.lng)], angular.copy(range)).addTo(vm.map.instance);
            }else{
                vm.map.instance.removeLayer(vm.map.radius);
                changeTypeLocationSearch('bounds');
            }
        }


        /**
         * Function to add some listener on events to map markers (this represent items on map)
         */
        function addEvenMarkerssMaps(){
            var current_event = ""; //Flag to current markers event on maps
            var current_event_id_item = ""; //Flag to current item id to markers event

            //var markerEvents = leafletEvents.getAvailableMarkerEvents();
            // Set listener to mouse out event on marker
            $scope.$on('leafletDirectiveMarker.mouseout', function(event, args){
                if(current_event != 'mouseout' && args['modelName'] != 'user_current_location'){
                    current_event = 'mouseout';
                    vm.map.markers[args['modelName']]['icon']['extraClasses'] = '';
                    for(var i=0; i < vm.items.length; i++){
                        if(String(vm.items[i]['id']) == args['modelName']){
                            vm.items[i]['selected'] = false;
                            break;
                        }
                    }
                }
            });

            // Set listener to mouse over event on marker
            $scope.$on('leafletDirectiveMarker.mouseover', function(event, args){
                if(current_event != 'mouseover' && args['modelName'] != 'user_current_location'){
                    current_event = 'mouseover';
                    vm.map.markers[args['modelName']]['icon']['extraClasses'] = 'selected';
                    for(var i=0; i < vm.items.length; i++){
                        if(String(vm.items[i]['id']) == args['modelName']){
                            vm.items[i]['selected'] = true;
                            break;
                        }
                    }
                }
            });

            // Set listener to click event on marker
            $scope.$on('leafletDirectiveMarker.click', function(event, args){
                if(current_event != 'click' && args['modelName'] != 'user_current_location'){
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

            $scope.$on('leafletDirectiveMarker.dragstart', function(event, args){
                if(args['modelName'] == 'user_current_location'){
                    vm.map.markers['user_current_location']['icon']['iconSize'] = [20, 20];
                    vm.map.markers['user_current_location']['icon']['shadowAnchor'] = [10, -8];
                }
            });


            $scope.$on('leafletDirectiveMarker.dragend', function(event, args){
                if(args['modelName'] == 'user_current_location'){
                    vm.map.markers['user_current_location']['icon']['iconSize'] = [25, 25];
                    vm.map.markers['user_current_location']['icon']['shadowAnchor'] = [10, -6];
                    if(vm.flag_custom_radius){
                        changeCurrentLocation(args['model'], true);

                    }else{
                        changeCurrentLocation(args['model'], false);
                        //if(vm.refresh_result_on_move){
                        getItemsearch(get_query());
                        //}
                    }
                }
            });
        }

        function addEventUserLocationSelected(){
            // Change select user's locations
            $scope.$watch('vm.user_location_selected',function(val,old){
                if (vm.user_location_selected &&
                    vm.user_location_selected.lat &&
                    vm.user_location_selected.lng &&
                    vm.user_location_selected.radius) {
                    params_search['m'] = angular.copy(vm.user_location_selected.radius);
                    $scope.radius = angular.copy(vm.user_location_selected.radius);
                    changeCurrentLocation(vm.user_location_selected, true);
                    if(vm.flag_custom_radius){
                        vm.map.radius.setRadius(angular.copy(vm.user_location_selected.radius));
                        changeSearchRadiusPosition(vm.user_location_selected.lat, vm.user_location_selected.lng);
                    }else{
                        vm.flag_custom_radius = true;
                        toggleRangeSearch(vm.user_location_selected.radius);
                    }
                }
            });
        }

        /**
         * Search items
         * @param q
         */
        function getItemsearch(q){
            vm.promiseRequestItems = ItemSearch.query(q, function(data){
                vm.items = data.results;
                vm.facets = data.facets;
                vm.item_count = data.count;
                page_nro = data.page;
                vm.page_next = data.next;
                vm.page_previous = data.previous;
                createMarkers();
                $location.search(q);
            }, function(error){
                AlertNotification.error("Error al intetar traer los datos, vuelva a intentarlo mas tarde");
            });
        }

        vm.refreshResults = function(){
            params_search.page = 1;
            getItemsearch(get_query());
        };

        vm.getItemByPage = function(page){
            params_search.page = page;
            getItemsearch(get_query());
        };

        /**
         * Create marker to represent search location
         */
        function createLocationSearchMarker(){
            vm.map.markers['user_current_location'] = {
                lat: angular.copy(current_location.lat),
                lng: angular.copy(current_location.lng),
                message: "Estoy aquí!",
                draggable:'true',
                focus: true,
                icon: {
                    iconUrl: '/static/image/custom_position_marker.svg',
                    shadowUrl: '/static/image/custom_position_marker_shadow.png',
                    iconSize: [25, 25],  // size of the icon
                    iconAnchor:   [12, 12], // point of the icon which will correspond to marker's location
                    popupAnchor: [0, -10], // point from whtich the popup should open relative to the iconAnchor
                    shadowAnchor: [10, -6], // the same for the shadow
                    shadowSize: [25, 10] // size of the shadow
                },
                zIndexOffset: 100,
                popupopen: true
            };
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
                marker['icon'] = {
                    type: 'awesomeMarker',
                    className: vm.items[i]['category'],
                    html: String(i + 1)

                };
                vm.map.markers[String(vm.items[i]['id'])] = marker;
            }
        }

        /**
         * Set style marker when item selected
         * @param item
         */
        function setMarkerSelected(item){
            if(item.selected){
                vm.map.markers[String(item.id)]['icon']['extraClasses'] = 'selected';
            }else{
                vm.map.markers[String(item.id)]['icon']['extraClasses'] = '';
            }
        }

        function changeTypeLocationSearch(type){
            if(vm.flag_custom_radius){
                type_location_search = 'point';
            }else{
                type_location_search = type;
            }
        }

        function get_query(page){
            var query = {};
            if(type_location_search =='point'){
                query.lat = params_search.lat;
                query.lng = params_search.lng;
                query.m = params_search.m;
            }else{
                query.n = params_search.n;
                query.s = params_search.s;
                query.e = params_search.e;
                query.w = params_search.w;
            }

            if(vm.facets){
                var selected_facets = '';
                for(var i=0; i < vm.facets.length; i++){

                    if(vm.facets[i] && vm.facets[i].activated){
                        var select_facet = '';
                        for(var iv=0; iv < vm.facets[i].values.length; iv++){
                            if(vm.facets[i].values[iv].activated == true){
                                if(select_facet != ''){
                                    select_facet += ',' + vm.facets[i].name + "_exact:" + vm.facets[i].values[iv].name;
                                }else{
                                    select_facet += vm.facets[i].name + "_exact:" + vm.facets[i].values[iv].name;
                                }
                                //break;
                            }
                        }
                        if(select_facet != ''){
                            if(selected_facets != ''){
                                selected_facets += "," + select_facet
                            }else{
                                selected_facets += select_facet
                            }
                        }
                    }
                }
                if(selected_facets != ''){
                    query.selected_facets = selected_facets;
                }
            }

            if(vm.selected_ordering){

                query.order_by=vm.selected_ordering.name;
            }

            if(params_search.q != ''){
                query.q = params_search.q;
            }

            if(page){
                query.page = page;
            }else{
                query.page = params_search.page;
            }
            return query;
        }

        /**
         * Get bounds with format to map
         * @returns {{}}
         */
        function get_bounds_to_params(){
            var bounds = {};
            bounds['northEast'] = {};
            bounds['southWest'] = {};
            bounds['northEast']['lat'] = params_search.n;
            bounds['southWest']['lat'] = params_search.s;
            bounds['northEast']['lng'] = params_search.e;
            bounds['southWest']['lng'] = params_search.w;

            return bounds;
        }

        function set_params_bounds_to_map(commit){
            params_search.n = angular.copy(vm.map.bounds['northEast']['lat']);
            params_search.s = angular.copy(vm.map.bounds['southWest']['lat']);
            params_search.e = angular.copy(vm.map.bounds['northEast']['lng']);
            params_search.w = angular.copy(vm.map.bounds['southWest']['lng']);

            if(commit){
                changeTypeLocationSearch('bounds');
                getItemsearch(get_query(1));
            }
        }

        /**
         * Chequea cada si cada uno de los valores -string- estan en la url
         * @param params
         */
        function check_params(params){
            for(var i=0; i < params.length; i ++){
                if(!params_search[params[i]]){
                    return false
                }
            }
            return true;
        }
    }
})();