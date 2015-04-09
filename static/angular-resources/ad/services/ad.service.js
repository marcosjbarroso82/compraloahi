/**
 * Ad
 * @namespace App.ad.services
 */
(function () {
    'use strict';

    angular
        .module('App.ad.services')
        .factory('AdSearch', AdSearch);

    AdSearch.$inject = ['$http'];

    /**
     * @namespace Ad
     * @returns {Factory}
     */
    function AdSearch($http) {
       var AdSearch = {
            search: search
        };

        return AdSearch;

        function search(q){
            return $http.get('/api/v1/ad-search/?' + q);

        }
    }


})()