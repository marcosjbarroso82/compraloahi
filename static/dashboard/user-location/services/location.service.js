/**
 * Ad
 * @namespace dashBoardApp.location.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.userLocation.services')
        .factory('UserLocations', UserLocations);

    UserLocations.$inject = ['$http'];

    /**
     * @namespace UserLocation
     * @returns {Factory}
     */
    function UserLocations($http) {

        var userLocation = {
            create: create,
            update: update,
            destroy: destroy,
            list: list
        };

        function create(location){
            return $http.post('/api/v1/user-locations/', location);
        }

        function update(location){
            return $http.put('/api/v1/user-locations/' + location.id + "/", location)
        }

        function destroy(location){
            return $http.delete('/api/v1/user-locations/' + location.id + "/");
        }

        function list(){
            return $http.get('/api/v1/user-locations/');
        }

        return userLocation;
    }
})()