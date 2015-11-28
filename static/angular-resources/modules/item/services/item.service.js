/**
 * Item
 * @namespace appSearch.item.services
 */
(function () {
    'use strict';

    angular
        .module('appSearch.item.services')
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

        function search(q){
            return $http.get('/api/v1/item-search/?' + q);

        }

        return ItemSearch;
    }


})();