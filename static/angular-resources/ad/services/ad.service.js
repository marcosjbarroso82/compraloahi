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

    /**
     * Gets a page parameter from url
     * @param {String} url
     * @return {String} page
     */
    function getPageFromUrl(url) {
        url = url.split(/\?|\&/);
        //previous = previous.split(/\?|\&/);
        var params = [];
        var page = "";
        url.forEach( function(str_param) {
            if (str_param) {
                var param = str_param.split("=");
                if (param[0] == 'page') {
                    page = param[1];
                }
            }
        });
        return page;
    }
})()