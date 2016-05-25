/**
 * Item
 * @namespace appSearch.item.services
 */
(function () {
    'use strict';

    angular
        .module('appSearch.item.services')
        .factory('ItemSearch', ItemSearch);

    ItemSearch.$inject = ['$resource'];

    /**
     * @namespace Item
     * @returns {Factory}
     */
    function ItemSearch($resource) {
        return $resource("/api/v1/item-search/:id", {id: '@id'}, {
            query: {method: 'get', isArray: false }
        });
    }


})();