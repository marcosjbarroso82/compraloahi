/**
 * Favorite
 * @namespace dashBoardApp.favorite.services
 */
(function () {
    'use strict';

    angular
        .module('dashBoardApp.ad.services')
        .factory('Favorite', Favorite);

    Favorite.$inject = ['$resource', 'djResource'];

    /**
     * @namespace Favorite
     * @returns {Factory}
     */
    function Favorite($resource, djResource) {

        return $resource(
            '/api/v1/favorites/:id/', {}, {
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