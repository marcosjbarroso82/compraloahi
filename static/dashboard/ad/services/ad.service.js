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
        //return $resource('/api/v1/ads/:id/:page');
        return $resource(
            '/api/v1/ads/:id/', {}, {
                get: {
                    method: 'GET',
                    id: '@id',
                    transformResponse: function(data, headers){
                        data = angular.fromJson(data);

                        // Rewrite Next and Previous
                        data.next = data.next ? getPageFromUrl(data.next) : "";
                        data.previous = data.previous ? getPageFromUrl(data.previous) : "";

                        return data;
                    }
                }
            }
        );
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