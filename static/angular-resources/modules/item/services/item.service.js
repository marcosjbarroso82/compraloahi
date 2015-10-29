/**
 * Item
 * @namespace App.item.services
 */
(function () {
    'use strict';

    angular
        .module('App.item.services')
        .factory('ItemSearch', ItemSearch);

    ItemSearch.$inject = ['$http'];

    /**
     * @namespace Item
     * @returns {Factory}
     */
    function ItemSearch($http) {
       var ItemSearch = {
            search: search
        };

        return ItemSearch;

        function search(q){
            return $http.get('/api/v1/item-search/?' + q);

        }
    }


})()