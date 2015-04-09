/**
 * Ad
 * @namespace dashBoardApp.ad.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.services')
        .factory('Ad', Ad);

    Ad.$inject = ['$resource'];

    /**
     * @namespace Ad
     * @returns {Factory}
     */
    function Ad($resource) {

        return $resource(
            '/api/v1/my-ads/:id/', {}, {
                get: {
                    method: 'GET',
                    id: '@id',
                    transformResponse: function(data, headers){
                        data = angular.fromJson(data);


                        return data;
                    }
                }
            }
        );
    }

})()