/**
 * Ad
 * @namespace dashBoardApp.location.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.userLocation.services')
        .factory('UserLocations', UserLocations);

    UserLocations.$inject = ['$resource'];

    /**
     * @namespace UserLocation
     * @returns {Factory}
     */
    function UserLocations($resource) {
        return $resource('/api/v1/user-locations/:id', { id: '@id' }, {
            update: {
                method: 'PUT' // this method issues a PUT request
            }
        });
    }
})()