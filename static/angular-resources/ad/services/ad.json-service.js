/**
 * Ad
 * @namespace App.ad.services
 */
(function () {
    'use strict';

    angular
        .module('App.ad.services')
        .factory('Ad', Ad);


    /**
     * @namespace Ad
     * @returns {Factory}
     */
    function Ad() {
        //return $resource('/api/v1/ads/:id/:page');
        return {
            get :function(callback){
                callback(json_data)

            }



        };
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