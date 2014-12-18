/**
 * Ad
 * @namespace dashBoardApp.location.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.location.services')
        .factory('UserLocations', UserLocations);

    UserLocations.$inject = ['$resource'];

    /**
     * @namespace Location
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